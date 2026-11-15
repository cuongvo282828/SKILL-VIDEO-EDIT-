#!/usr/bin/env python3
"""Check registry references and sample timeline constraints, not rendered quality."""
import argparse
import json
from pathlib import Path

def validate(registry, timeline):
    ids = registry['effectIds']
    flat = [x for group in ids.values() for x in group]
    assert len(set(flat)) == len(flat), 'Duplicate effect ID'
    patterns = {p['id']: p for p in registry['patterns']}
    assert len(patterns) == len(registry['patterns']), 'Duplicate pattern ID'
    for p in patterns.values():
        assert all(c in flat for c in p['components']), 'Unknown component'
    effects = {x['id']: x for x in timeline['effects']}
    assert len(effects) == len(timeline['effects']), 'Duplicate effect definition'
    for e in effects.values():
        assert e['id'] in ids[e['kind']], 'Effect kind mismatch'
        frames = [k['f'] for k in e.get('keyframes', [])]
        assert frames == sorted(set(frames)), 'Invalid keyframe order'
        assert all(0 <= f < e['durationFrames'] for f in frames), 'Keyframe out of bounds'
    project = timeline['project']
    assert project['fps'] > 0 and project['durationFrames'] > 0, 'Invalid project timing'
    assets = {a['id']: a for a in timeline.get('audioAssets', [])}
    seen = set()
    for e in timeline['events']:
        assert e['id'] not in seen, 'Duplicate event ID'
        seen.add(e['id'])
        a, b = e['startFrame'], e['endFrameExclusive']
        assert type(a) is int and type(b) is int and 0 <= a < b <= project['durationFrames'], 'Invalid event range'
        assert e['patternId'] in patterns and e['effectId'] in effects, 'Unknown event reference'
        assert e['effectId'] in patterns[e['patternId']]['components'], 'Pattern/effect mismatch'
        assert 0 <= e['visualAnchorOffsetFrames'] < b - a, 'Anchor outside event'
        assert all(0 <= e['positionNorm'][v] <= 1 for v in ['x', 'y']), 'Position outside canvas'
        assert e['text'].strip(), 'Empty text'
        assert e['evidenceStatus'] in ['OBS', 'MEAS', 'DOC', 'REC', 'UNKNOWN'], 'Invalid evidence status'
        audio = e['audio']
        assert audio['startMs'] >= 0 and -60 <= audio['gainDb'] <= 12, 'Invalid audio parameters'
        if audio['enabled']:
            asset = assets[audio['assetId']]
            assert asset.get('uri') and asset.get('licenseId') and asset.get('reviewStatus') == 'approved', 'Unapproved audio'
            assert not asset.get('commercialUse') is False, 'Asset excludes commercial use'
            expected = (a + e['visualAnchorOffsetFrames']) * 1000 / project['fps'] - asset['anchorMs']
            assert abs(expected - audio['startMs']) < 1, 'Audio marker mismatch'

def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeline', type=Path, default=root / 'presets/timeline-example.json')
    args = parser.parse_args()
    validate(json.loads((root / 'presets/registry.json').read_text()), json.loads(args.timeline.read_text()))
    print('PASS: registry/components, keyframes, event timing and enabled-audio preconditions. Layout, listening and full JSON Schema validation remain separate.')

if __name__ == '__main__':
    main()
