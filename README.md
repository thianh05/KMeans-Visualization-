# Interactive K-Means Clustering Visualizer

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![PyPI - pygame](https://img.shields.io/badge/pygame-black?style=for-the-badge&logo=pygame)

Một ứng dụng trực quan hóa thuật toán **K-Means Clustering** được xây dựng bằng Python. Dự án này giúp người dùng dễ dàng hiểu và quan sát cách thuật toán học không giám sát phân cụm dữ liệu theo từng bước thông qua giao diện đồ họa tương tác.

---

## Tính năng nổi bật
* * **Tương tác trực tiếp:** Thêm các điểm dữ liệu (data points) cực kỳ dễ dàng bằng cách click chuột trực tiếp lên không gian vẽ.
* * **Tùy chỉnh linh hoạt:** Thay đổi số lượng cụm (K) mong muốn thông qua các nút `+` và `-`.
* * **Chạy từng bước (Step-by-step):** Quan sát trực quan quá trình thuật toán tính toán khoảng cách Euclidean, gán nhãn dữ liệu và cập nhật lại vị trí các tâm cụm (centroids) mỗi khi nhấn nút `Run`.
* * **Khởi tạo ngẫu nhiên:** Nút `Random` giúp chọn lại vị trí ngẫu nhiên cho các tâm cụm để quan sát cách thuật toán hội tụ từ nhiều điểm xuất phát khác nhau.
* * **Đối chiếu với thư viện chuẩn:** Nút `Algorithm` gọi trực tiếp module `KMeans` từ thư viện `scikit-learn` để trả về kết quả phân cụm tối ưu ngay lập tức. Tính năng này rất hữu ích để so sánh với thuật toán tự triển khai.
* * **Đo lường sai số:** Tự động tính toán và hiển thị trực tiếp giá trị **Error** (tổng khoảng cách từ các điểm dữ liệu đến tâm cụm tương ứng) ngay trên giao diện.

---

##  Công nghệ & Thư viện sử dụng

| Công nghệ / Thư viện | Vai trò trong dự án |
| :--- | :--- |
| <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="20" height="20" alt="Python"> **Python** | Ngôn ngữ lập trình cốt lõi của toàn bộ dự án. |
| **Pygame** | Xây dựng giao diện UI/UX, xử lý đồ họa trực quan và các sự kiện click chuột. |
| **Scikit-learn** | Sử dụng module `sklearn.cluster.KMeans` để làm chuẩn đối chiếu (baseline) cho thuật toán. |
| **Math** | Thư viện toán học tiêu chuẩn dùng để tính toán khoảng cách Euclidean giữa các điểm dữ liệu. |
