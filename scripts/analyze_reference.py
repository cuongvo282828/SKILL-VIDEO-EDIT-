#!/usr/bin/env python3
"""Read-only media analysis; writes derived evidence to a separate directory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--contact-sheet', action='store_true')
    args = parser.parse_args()
    source = args.video.resolve(strict=True)
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    if source.parent == out:
        parser.error('Use a separate output directory to protect source files.')
    probe = json.loads(run(['ffprobe', '-v', 'quiet', '-show_format',
        '-show_streams', '-of', 'json', str(source)]).stdout)
    sha = hashlib.sha256()
    with source.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            sha.update(chunk)
    probe['sha256'] = sha.hexdigest()
    (out / 'probe.json').write_text(json.dumps(probe, indent=2) + '\n')
    loud = run(['ffmpeg', '-hide_banner', '-i', str(source), '-vn', '-af',
        'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-']).stderr
    raw = json.loads(loud[loud.rfind('{'):loud.rfind('}') + 1])
    (out / 'loudness.json').write_text(json.dumps({
        k: raw[k] for k in ['input_i', 'input_tp', 'input_lra', 'input_thresh']}, indent=2) + '\n')
    # Metadata goes to stdout, avoiding filter-path interpolation/escaping.
    scenes = run(['ffmpeg', '-hide_banner', '-threads', '1', '-i', str(source),
        '-vf', r'select=gt(scene\,0.28),metadata=print:file=-',
        '-an', '-f', 'null', '-']).stdout
    (out / 'scene-candidates.txt').write_text(scenes)
    candidates = [float(t) for t in re.findall(r'pts_time:([0-9.]+)', scenes)]
    if args.contact_sheet:
        # select preserves source PTS; fps resampling would relabel selected frames.
        vf = (r"select=isnan(prev_selected_t)+gte(t-prev_selected_t\,3),"
            "scale=192:342,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:"
            r"text='%{pts\:hms}':fontsize=16:fontcolor=white:box=1:boxcolor=black@0.8:"
            "x=5:y=h-24,tile=6x6")
        run(['ffmpeg', '-v', 'error', '-threads', '1', '-i', str(source),
            '-vf', vf, '-frames:v', '1', '-y', str(out / 'contact.jpg')])
    print(json.dumps({'sha256': sha.hexdigest(), 'scene_candidates': candidates,
        'warning': 'Candidates are not total shots. A 6x6 contact sheet covers at most 108 seconds.'}))

if __name__ == '__main__':
    main()
