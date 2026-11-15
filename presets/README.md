# Registry và hợp đồng timeline

Ba JSON được trích từ [06 — AI Editing Automation Roadmap & Data Contract v0.1](https://docs.google.com/document/d/1ISUjRrF3zk3QBC59Eh5Po_VSva0bUvlDJdKg3HdHsPA/edit), đối chiếu ngày 15/11/2026.

- `registry.json`: T01–T13, M01–M19, S01–S20 và tổ hợp P01–P12.
- `text-event.schema.json`: schema tối thiểu của một text event; không mô tả toàn bộ renderer.
- `timeline-example.json`: ví dụ có keyword pop; asset audio đang pending và bị tắt. Không tự bật audio khi chưa chọn asset có quyền dùng và marker được kiểm.

Các thông số là REC — đề xuất, không phải keyframe được trích từ MP4. Các JSON này là dữ liệu cấu hình/kiểm tra, chưa phải bộ renderer hiện thực đủ 12 pattern.

Chạy `python scripts/validate_reference_presets.py` từ gốc repo để kiểm registry, component, timing và điều kiện audio của ví dụ. Script không thay thế JSON Schema validator đầy đủ, layout checking, xem playback hoặc nghe kiểm.

Để nghiên cứu video mới: `python scripts/analyze_reference.py /path/video.mp4 --out /path/evidence --contact-sheet`. Thư mục output phải tách khỏi nguồn. Script không sửa video. Contact sheet giới hạn 36 mẫu/108 giây; video dài hơn cần chia thêm đoạn để kiểm đủ hình.
