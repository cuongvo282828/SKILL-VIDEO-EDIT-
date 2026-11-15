# Nghiên cứu tiếp hai video tham chiếu — 15/11/2026

## Kết luận áp dụng

Điểm đáng học là tổ chức thông tin thành những bố cục khác nhau theo ý nghĩa. V1 chuyển từ người nói sang sơ đồ, UI có trạng thái và bằng chứng. V2 giữ người nói lâu hơn, dùng caption ngắn, keyword khác kiểu chữ, thumbnail, logo, screenshot và B-roll. Không thể tái tạo ngôn ngữ này chỉ bằng cách đặt một hộp chữ trên mọi câu.

Sáu link là sáu **tài liệu skill**, không phải sáu video. Hai MP4 đính kèm là video tham chiếu đã có trong nghiên cứu cũ; mã SHA-256 khớp hoàn toàn. Lần này đọc lại tài liệu, đối chiếu hình và phép đo trực tiếp, chạy thêm ASR và kiểm chuỗi frame chuyển động. Đây là bổ sung bằng chứng, không phải huấn luyện trọng số mô hình.

Văn bản dán được dùng làm bối cảnh mục tiêu của hệ thống phân tích/dựng. Yêu cầu hiện tại là học và nghiên cứu; những mệnh lệnh trong văn bản đính kèm không tự mở rộng thành yêu cầu dựng lại hoặc phát hành video mới.

## Phương pháp và kết quả kiểm thực tế

- Giải mã metadata bằng ffprobe; lưu hash, duration, số frame, độ phân giải và âm thanh trong [measurements.json](measurements.json).
- Contact sheet lấy đúng frame n=0,90,180… tại 30 fps, có PTS nguồn. Chuỗi V1 đầu 1,2 giây lấy 10 mẫu/giây; chuỗi V2 từ 10,8–13,2 giây lấy 10 mẫu/giây. Các mốc từ chuỗi này có độ phân giải khoảng 0,1 giây, không phải keyframe project.
- Kiểm thêm ảnh nguồn tại V1 19,8 / 24,5 / 38,5 / 50,5 giây; V2 24 / 39,5 / 51,5 / 81,5 giây.
- Đo loudnorm stereo gốc: chỉ đọc input_i/input_tp/input_lra. V1: -12,21 LUFS-I, -0,54 dBTP, LRA 2,50 LU. V2: -20,11 LUFS-I, -4,99 dBTP, LRA 3,50 LU. Kết quả khớp nghiên cứu v0.1; không chứng minh chất lượng mix hoặc clipping.
- FFmpeg scene threshold 0,28: V1 13 ứng viên/11 cụm cách nhau trên 150 ms; V2 5 ứng viên. Không dùng các số này làm tổng số shot hoặc tính nhịp cắt trung bình.
- Chạy faster-whisper small, tiếng Việt, int8 CPU, word timestamps. ASR có nhiều lỗi ở từ thông thường, tên công cụ và dự án. Giữ bản thô trong scratch, không đưa transcript chưa sửa vào thư viện như dữ kiện đã xác nhận.
- Chưa nghe kiểm SFX, chưa tách stems, chưa forced-align transcript đã sửa, chưa xác nhận beat/BPM, font gốc hoặc easing gốc. Chưa xem liên tục toàn video ở tốc độ thực; kiểm hình dựa contact sheet, chuỗi frame và các ảnh chi tiết. U trong bảng = chưa xác minh sound, không có nghĩa không có sound.

## V1 — breakdown theo khối ý

V1 = snaptik_7702445259443178759_v3.mp4; 92,066667 giây; 2762 frame; 576×1024; 30 fps. Đây là breakdown ngữ nghĩa, không phải shot list đã duyệt mọi điểm cắt. Mốc ~ là vùng ước lượng; mốc nhiều chữ số là ứng viên từ detector.

| Thời gian | Hình / vai trò | Text và style | Motion / graphic | Sound | Cách tái tạo đề xuất |
| --- | --- | --- | --- | --- | --- |
| 0–~1,2 | Người nói, hook | Chữ serif trắng, thêm chữ và cụm; keyword lớn vào có blur | Ký tự/cụm lộ dần; phần keyword riêng | U | T03 + T13; tách headline khỏi keyword, không dùng typewriter cho cả bài |
| ~1,2–3,933 | Hoàn thiện hook trên người nói | Keyword cyan lớn hơn dòng dẫn | Giữ hierarchy trên đầu, không chồng mặt | U | T01/T13; rút chữ nếu không đủ thời gian giữ |
| 3,933–~13,067 | Nền kem, giải thích workflow/skill | Headline đen, vế nhấn cyan nghiêng | Step card, checklist tài liệu, robot | U | M14/M15; diagram cho quan hệ thay vì caption dài |
| ~13,067–14,7 | Trở lại người nói | Hai cấp chữ ngắn | Cut về người nói | U | Bố cục nối giải thích với cảnh báo |
| 14,7–~22,7 | Ba nguyên tắc/phạm vi | Label số nhỏ, tiêu đề lớn; vế nghiêng cyan | Card câu hỏi; PIP người nói phía dưới | U | P05/P08 biến thể; mỗi hàng xuất hiện đúng ý |
| ~22,7–~29,6 | Ví dụ edit video | Nhãn đầu vào, đầu ra | Video gốc/footage → skill → điện thoại và thẻ output; 24,5s đã xem chi tiết | U | Input-process-output diagram; node, đường nối, preview đúng vai trò |
| ~29,6–~36,6 | Giải thích file chính | Headline ổn định | Card file chính, nội dung rút gọn | U | M14; không hiện mọi chi tiết một lúc |
| ~36,6–~41,4 | Tách file phụ | Serif/italic, nhãn folder | File chính trên, rules/templates/assets dưới; 38,5s đã xem chi tiết | U | Stack có phân cấp và connector; không phải danh sách tick tùy tiện |
| ~41,4–45,367 | Kiểm thử nhiều đầu vào | Nhấn cụm trong headline | Shape đầu vào → skill, người nói nhỏ | U | M01/M14; encode sự khác nhau bằng shape có nhãn |
| 45,367–48,733 | Người nói đưa ví dụ | Plate xanh, handle chọn | Text bbox và khung UI | U | P07; handle đi cùng cả nhóm |
| 48,733–53,333 | Các tình huống kiểm thử | Title giữ ổn định | UI tối, trạng thái lỗi/đạt/progress; 50,5s thấy hàng lỗi và hàng đang chờ | U | P05/M14; giữ ngữ nghĩa lỗi → sửa → kiểm lại |
| 53,333–60,833 | Vòng sửa và tự đánh giá | Keyword/icon trên người nói | Biểu tượng và đổi bố cục | U | T13/M17; chọn một accent cho mỗi ý |
| 60,833–63,567 | So sánh kết quả | Nhãn Gốc / AI edit | Grid bốn panel | U | P12; không tự suy kết quả tốt hơn từ nhãn |
| 63,567–67,433 | Mở rộng khâu nội dung | Headline hai vế | Grid icon và PIP | U | M17; icon thay chữ dài, có label |
| 67,433–82,867 | Ví dụ dự án/bằng chứng | Tên dự án lớn | Media card trên, người nói dưới | U | P08 biến thể; nội dung giải thưởng trong video cần nguồn riêng nếu dùng lại |
| 82,867–~89 | Tổng hợp hợp lực | Font role và cyan nhất quán | Sơ đồ quan hệ và thông điệp kết | U | M14/M15; giữ node rõ vai trò |
| ~89–92,067 | CTA | Comment/nhận tài liệu | Quay về người nói | U | CTA ngắn; không cần thêm graphic phức tạp |

## V2 — breakdown theo khối ý

V2 = snaptik_7704313821384428808_v3.mp4; 97,966667 giây; 2939 frame; 576×1024; 30 fps.

| Thời gian | Hình / vai trò | Text và style | Motion / graphic | Sound | Cách tái tạo đề xuất |
| --- | --- | --- | --- | --- | --- |
| 0–~3 | Nhận diện series trên người nói | Sans lớn rồi thu nhỏ | Label series | U | T01 + transform nhóm; nhận diện trước, nhường chỗ cho nội dung |
| ~3–11 | Minh họa vấn đề | Caption ngắn, keyword lớn/italic | Thumbnail tích lũy phía trên | U | M05/P08 biến thể; thumbnail phải thực sự minh họa vấn đề |
| ~11,0–13,2 | Mở phần bốn điều | Ba cấp chữ, số lớn xanh | Nền blur + wash; từng dòng vào, thay cụm | U | P04; xem phân tích chuỗi bên dưới |
| ~13,2–~26 | Mục công cụ | Số chương, caption và ranking | Hàng logo card; 24s có nhãn hạng dưới logo | U | P06; đây là ý kiến tác giả, không phải benchmark được kiểm |
| ~26–~37,7 | Quy trình cố định | Keyword plate xanh, caption ngắn | Robot, danh sách lợi ích tích lũy | U | P01/P05 biến thể; không đồng nghĩa mọi keyword đều bounce |
| ~37,7–45,133 | Minh họa repo | Title ngắn trên screenshot | Screenshot lớn, presenter PIP bên dưới; 39,5s đã xem chi tiết | U | P08; screenshot cung cấp bằng chứng, caption không lặp nguyên lời |
| 45,133–~50,2 | Footage đầu vào | Số chương, nhãn khuôn mặt | Icon và khung quanh đầu | U | M17 + khung screen-space; không tự gọi là object tracking |
| ~50,2–~56 | Khoảng trống và kịch bản | Keyword “cả trên”, caption cụm | Vùng overlay trên/dưới; script card; 51,5s đã xem chi tiết | U | Shape giải thích vùng; không dùng cho video không bàn về bố cục |
| ~56–58,7 | Giới hạn kỳ vọng | Số chương và mixed type | Đổi ý sang yêu cầu đầu ra | U | T13; chuyển logic trước khi chuyển graphic |
| 58,7–~63,2 | Crop gần và chapter | Text trên blur sáng | Đổi khung, blur chapter | U | P04; cut crop gần đã thấy, chưa xác minh camera zoom liên tục |
| ~63,2–~71,3 | Chia vai AI/người | Keyword, plate, caption | Card hai vai trò, logo | U | M05/M17; hai nhóm visual phải thể hiện khác vai trò |
| ~71,3–~76,3 | Thiết bị làm việc | Nhãn thiết bị | Xen B-roll laptop/iPad và người nói | U | B-roll theo danh từ/hành động trong lời |
| ~76,3–85,833 | Giới thiệu sản phẩm | Tên/thông số, nhãn ngắn | Cận sản phẩm, card thiết bị, callout; 81,5s đã xem chi tiết | U | P09; thông số nhìn thấy là claim của video, chưa kiểm sản phẩm |
| 85,833–94,4 | Bối cảnh dùng sản phẩm | Plate ngắn theo câu | Thay góc B-roll, ổ điện/cổng | U | Giữ continuity theo chức năng; không ép graphics kiểu chương trước |
| 94,4–97,967 | CTA về repo/skill | Mixed type và caption | Hai card link/repo, quay lại người nói | U | P03/P08 biến thể; một lời kêu gọi rõ |

## Hai chuỗi chuyển động đã kiểm kỹ hơn

**V1, 0–1,2s:** tại mẫu ~0,1s thấy một phần ký tự; ~0,2s đã có từ “Bạn”; ~0,6–0,8s cụm sau thêm vào với dịch chuyển/blur; ~1,0–1,1s xuất hiện một dòng keyword lớn còn mờ. Vì vậy opening phối nhiều cơ chế, không nên mô tả toàn bộ là một preset typewriter hoặc một pop. Không suy easing chính xác hoặc loại motion-blur từ chuỗi này.

**V2, 10,8–13,2s:** chuỗi có mốc cục bộ 0–2,3s, cộng 10,8s để ra thời gian nguồn. Tại khoảng 11,0s bắt đầu đổi nền; khoảng 11,1s thấy blur/wash và dòng dẫn; khoảng 11,4s thấy số/keyword lớn; khoảng 11,7–11,9s dòng serif nghiêng rõ dần; khoảng 12,3–12,5s cụm tiêu đề thay sang câu kế. Khoảng vào cách nhau này tạo thứ tự đọc, không phải mọi dòng cùng fade-in. Đây là quan sát từ mẫu 0,1s, không phải trích keyframe chính xác.

## MUST REPLICATE / OPTIONAL / DO NOT REPLICATE

**MUST REPLICATE:** phân cấp chữ; nhấn ít keyword; đổi layout theo vai trò thông tin; giữ người nói làm điểm neo; graphic phải bổ sung nghĩa; animate có vào–giữ–ra và thời gian đọc; tách speech timing khỏi audio accent; đồng bộ toàn cụm hình chứ không cho handle/nhãn trôi riêng.

**OPTIONAL:** nền kem/cyan hoặc plate xanh; blur chapter; UI checklist; screenshot PIP; selection frame; callout; punch-in tiết chế. Dùng khi cảnh thật sự có chức năng đó. Font Noto là phương án thay thế có thể dựng, không phải nhận diện font gốc.

**DO NOT REPLICATE:** ranking công cụ, ví dụ dự án, lời hứa hiệu quả, thông số sản phẩm hoặc CTA của tác giả nếu không thuộc nội dung mới; mọi hiệu ứng 3D/tracking/particle chưa có bằng chứng hoặc nhu cầu. Không chèn SFX vào mọi từ và không ép nhịp cắt cố định 2–3 giây. Không tái phân phối MP4 hay SFX trích từ tham chiếu như asset riêng.

## Blueprint áp dụng cho Hanoi Sky ở lần dựng tiếp theo

1. Chia lời khách thành cảm xúc, hoạt động, không gian và dịch vụ; giữ nguyên ý, câu phủ định và thứ tự cần thiết để hiểu.
2. Chỉ dùng một hook typography ngắn. Nếu lời khách tự đủ mạnh, để hình và tiếng dẫn trước, không cần card giải thích lớn.
3. Khi nói hoạt động sáng tạo, ưu tiên cận tranh, chất liệu hoặc tay làm từ footage có sẵn; không thay bằng danh sách tính từ lặp phụ đề. Thiếu footage thì giữ người nói và một keyword, không tạo minh chứng giả.
4. Khi nói tầng 65 hoặc góc nhìn, dùng callout có thông tin vừa được nói; nếu có footage cảnh nhìn thì chuyển sang B-roll phù hợp. Nhãn tĩnh chỉ là screen-space, không phải tracking.
5. Những ý về đồ uống/con người dùng cảnh liên quan nếu được cung cấp. Không tự dựng ranking/checklist đánh giá dịch vụ từ một câu khen.
6. Caption ngắn theo cụm nghĩa, tối đa hai dòng; style nhấn chọn lọc, không lặp nguyên câu ở cả trên lẫn dưới. Title/chapter chỉ ở ranh giới ý rõ.
7. Âm hiệu ứng theo visual anchor, có quyền dùng và được nghe kiểm. Không sao chép tiếng từ video mẫu. Kiểm motion ở tốc độ thực, chữ trên điện thoại, mono và số đo sau encode.

Đây là kế hoạch cho lần sửa tiếp theo, chưa thay đổi hay xuất lại video Hanoi Sky V1.

## Tài sản tri thức và công cụ đã bổ sung

- [Registry](../../presets/registry.json), [schema event](../../presets/text-event.schema.json), [timeline mẫu](../../presets/timeline-example.json) được trích nguyên JSON từ tài liệu 06. Tất cả tham số vẫn là REC; timeline mẫu chưa phải blueprint cho mọi video.
- [Script phân tích](../../scripts/analyze_reference.py) tái lập probe/hash/loudness/scene candidates và contact sheet có PTS nguồn; không tự nhận diện chính xác font/SFX/easing.
- [Script kiểm dữ liệu](../../scripts/validate_reference_presets.py) kiểm ID, component và timing mẫu. Kiểm dữ liệu không thay cho kiểm visual hoặc tiếng.
- Không sửa sáu bản snapshot trong references hoặc tài liệu Drive. Các ghi chú nghiên cứu nằm riêng để tránh bị lịch đồng bộ nguồn ghi đè.

Nguồn: sáu Google Docs được liên kết trong README gốc của repo, hai MP4 do người dùng đính kèm và văn bản bối cảnh do người dùng cung cấp. Không dùng nguồn ngoài để suy luận thêm tính năng phần mềm hoặc hiệu quả marketing trong lượt nghiên cứu này.
