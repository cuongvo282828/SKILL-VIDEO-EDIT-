---
name: editor-lotte-hanoi-sky
description: Nghiên cứu video tham chiếu, chọn công thức text/motion/audio và lập kế hoạch dựng video LOTTE Hanoi Sky từ thư viện đã lưu.
---

# Editor LOTTE Hanoi Sky

Skill này được tạo ngày 15/11/2026 để kết nối sáu tài liệu nghiên cứu trên Drive với repo. Đây không phải bản SKILL.md cũ được khôi phục.

## Quy trình
1. Đọc [ngữ cảnh dự án](docs/project-context.md); xác định footage, lời thoại, mục tiêu, thời lượng và định dạng đầu ra theo yêu cầu hiện tại.
2. Khi nghiên cứu video, đọc [phân tích tham chiếu](references/01-reference-analysis.txt). Gắn nhận xét với timestamp; phân biệt OBS (quan sát), MEAS (đo), DOC (nguồn), REC (đề xuất), UNKNOWN (chưa xác minh).
3. Chọn kỹ thuật từ [text](references/02-text-animation.txt), [motion](references/03-motion-graphics.txt) và [sound](references/04-sound-effects.txt) theo ý nghĩa nội dung.
4. Chọn P01–P12 trong [thư viện tổ hợp](references/05-editing-combinations.txt). Lập timeline gồm thời gian, nội dung, footage, pattern, text, motion, audio và nguồn/giới hạn.
5. Khi triển khai tự động hóa, đọc [roadmap và data contract](references/06-automation-roadmap.txt). Không coi roadmap là renderer đã hoạt động.
6. Dựng bằng công cụ có sẵn phù hợp với dự án; kiểm hình, chữ, thời gian đọc, sync và tiếng trên file xuất thực tế trước khi gọi là final.

## Nguyên tắc
- Ưu tiên nội dung và nhịp lời, bố cục/thời gian đọc, rồi mới animation và âm thanh.
- Mỗi vùng chỉ một accent chính; giữ style nhất quán; tránh che mặt hoặc chi tiết cần nhìn.
- Không suy font, preset, easing hoặc keyframe gốc từ ảnh tĩnh. Thông số REC là đề xuất tái tạo.
- Không khẳng định hiệu quả viral/retention khi thiếu dữ liệu; không gán tên SFX nếu chưa nghe kiểm.
- Khi thiếu asset hoặc độ tin cậy thấp, dùng caption đơn giản với footage gốc và ghi rõ giới hạn.
- Kiểm quyền sử dụng từng asset, font và âm thanh trước khi dùng.
- Video Hanoi Sky được người dùng xác nhận là final được liên kết trong ngữ cảnh dự án. Chưa xác minh nó đã áp dụng toàn bộ thư viện nghiên cứu.

## Nguồn và cập nhật
[sources.json](sources.json) lưu ID, URL và thời gian sửa nguồn. Các file references là snapshot văn bản; ảnh minh chứng và bố cục bảng gốc nằm ở Google Docs. Kết nối này chưa tự đồng bộ và không tự cài skill vào ChatGPT.
