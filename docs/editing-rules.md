# Quy tắc vận dụng bộ nghiên cứu video

Ngày đối chiếu: 15/11/2026. Bản hướng dẫn này được đúc rút từ tài liệu 01, 05 và 06; không thay thế bản nguồn. Mục đích là chuyển kiến thức thành cách ra quyết định khi dựng.

## 1. Bắt đầu bằng ý nghĩa của cảnh

Trước mỗi hiệu ứng, xác định cảnh là hook, định nghĩa, ví dụ, so sánh, bằng chứng hay CTA. Chọn hình thức giúp người xem hiểu ý đó. Talking head giữ vai trò điểm neo; graphics giải thích quan hệ, đối tượng hoặc kết quả. Không mặc định thêm hộp chữ vào mọi câu. Không áp nguyên phong cách video giải thích công nghệ lên phỏng vấn khách hoặc nội dung trải nghiệm khi không phù hợp.

Thứ tự sửa: nội dung và nhịp kể → bố cục và thời gian đọc → keyframe → blur → sound → loudness. Nếu thiếu thời gian đọc, rút chữ hoặc tăng thời gian giữ trước khi thêm hiệu ứng.

## 2. Phối chữ, motion và âm thành một sự kiện

Mỗi vùng hình chỉ có một điểm nhấn chính. Phụ đề chuyển tải lời nói; graphic cung cấp thông tin bổ sung, tránh hai nơi cùng lặp nguyên câu. Giữ nhất quán font role, màu, khoảng cách, bo góc, hướng vào và khoảng stagger. Chọn bố cục theo loại thông tin, thay vì giữ một card cố định cho mọi ý.

Ease-out hãm lúc vào; ease-in tăng tốc lúc ra. Bounce phải thật sự vượt đích rồi trở lại. Reveal phải có mask nếu được mô tả là mask reveal. Không gọi fade là reveal bằng mask hoặc keyframe tĩnh là tracking.

Âm thanh nhấn vào sự kiện có nghĩa: pop ở lúc chữ đọc rõ hoặc scale peak; whoosh gần vận tốc lớn nhất; tick tại thay đổi trạng thái. Chọn một anchor nhất quán. Tránh hai transient cạnh tranh trong khoảng ±150 ms quanh một accent. Nhịp lời và thời gian đọc có ưu tiên hơn nhịp nhạc.

## 3. Chọn đúng công thức P01–P12

| Mục đích | Pattern phù hợp | Điều kiện cần |
| --- | --- | --- |
| Nhấn keyword | P01 | Chọn từ và thời điểm; pop tiết chế |
| Prompt/lệnh ngắn | P02 | Reveal theo grapheme; không áp cho đoạn dài |
| Giới thiệu mục | P03 | Slide/mask reveal, giữ rõ sau khi vào |
| Chuyển chương | P04 | Blur/wash nền rồi title; không làm mờ thông tin cần đọc |
| Quy trình hoặc checklist | P05 | Hàng vào theo lời; trạng thái có dữ liệu |
| So sánh logo/xếp hạng | P06 | Có căn cứ hoặc ghi rõ là ý kiến |
| Khung chọn nhấn chữ | P07 | Bbox theo chữ, padding, viền và handle |
| Tài liệu và người trình bày | P08 | Asset đọc được, PIP không che bằng chứng |
| Thông số/callout | P09 | Anchor → line → label; thông tin có nguồn |
| Chữ sau chủ thể | P10 | Matte sạch và kiểm tóc, tay, motion blur |
| Nhấn một phát biểu | P11 | Crop còn đủ không gian và độ nét |
| So sánh trước/sau | P12 | Cùng nội dung, label nhất quán, so sánh công bằng |

Không cần dùng hết 12 pattern. Khi chỉ dùng một phần hoặc điều chỉnh cơ chế, ghi là “biến thể lấy cảm hứng từ Pxx”; không tuyên bố đã triển khai đầy đủ pattern.

## 4. Timeline có thể kiểm và dựng lại

Luồng làm việc: ingest/probe/hash → ASR và sửa transcript → chia đoạn theo nghĩa → bố cục và vùng mặt → chọn pattern → timeline JSON → preview → kiểm hình/âm → xuất bản theo yêu cầu người dùng.

Mỗi event lưu ID, pattern/effect/version, startFrame, endFrameExclusive, nội dung, vị trí, visual anchor, audio marker, bằng chứng và trạng thái cần review. Khung bắt đầu được tính, khung kết thúc không được tính. Khi trim hoặc đổi tốc độ, lưu time map nguồn → đầu ra. Dùng sample/ms cho âm khi cần, tránh cộng dồn sai số làm tròn frame.

Kiểm cả quy tắc nghiệp vụ ngoài JSON Schema: end > start; end không vượt duration; anchor nằm trong event; ID có trong registry; asset có quyền dùng; bbox và safe area hợp lệ. Khi thiếu asset hoặc confidence thấp, fallback về footage và caption đơn giản, ghi lý do.

## 5. Phân biệt bằng chứng và đề xuất

OBS = quan sát trực tiếp; MEAS = phép đo; DOC = nguồn tài liệu; REC = công thức đề xuất; UNKNOWN = chưa xác minh. Render thành công không biến REC thành bằng chứng creator đã dùng preset đó. Scene detector chỉ cho ứng viên thay đổi hình; spectral flux không tự chứng minh SFX/BPM. Không suy font, phần mềm, easing hoặc keyframe gốc từ vài ảnh tĩnh. Không khẳng định viral/retention khi chưa có dữ liệu phù hợp.

## 6. Kiểm bản xuất thực tế

Kiểm chữ Việt, tên riêng, phủ định, thời gian đọc, safe area và vùng mặt. Xem preview ở tốc độ thật ngoài việc kiểm frame. Nghe kiểm tiếng và mono nếu công cụ cho phép; phép đo âm lượng hoặc ASR không thay cho nghe kiểm và phải ghi rõ nếu chưa nghe được.

Mục tiêu thử trong tài liệu: -16 LUFS-I, true peak ≤ -1.5 dBTP; accent–sound ±1 frame; caption word alignment ±2 frame trên transcript đã sửa. Đây là mục tiêu dự án, không phải chuẩn nền tảng hoặc kết quả mặc nhiên đạt được. Đo lại sau encode; báo số thực tế và giới hạn. Chỉ gọi một bước là đã kiểm khi có bằng chứng tương ứng.

## Nguồn

- [01 — Nghiên cứu và phân tích tham chiếu](https://docs.google.com/document/d/1gFz02GSi8kUWgWb0I6JnrgHgpapYnzqKYLke8LCitXU/edit)
- [05 — Thư viện tổ hợp dựng](https://docs.google.com/document/d/11N5qq2xRmyhXliaVZ3TdACaBry1JIWVhCcA_lGLkZr4/edit)
- [06 — Roadmap và data contract](https://docs.google.com/document/d/1ISUjRrF3zk3QBC59Eh5Po_VSva0bUvlDJdKg3HdHsPA/edit)
