#  Interactive K-Means Clustering Visualizer

Một ứng dụng trực quan hóa thuật toán **K-Means Clustering** được xây dựng bằng Python. Dự án này giúp người dùng dễ dàng hiểu và quan sát cách thuật toán học không giám sát phân cụm dữ liệu theo từng bước thông qua giao diện đồ họa tương tác.

---

##  Tính năng nổi bật

* 1. **Tương tác trực tiếp:** Thêm các điểm dữ liệu (data points) dễ dàng bằng cách click chuột lên không gian vẽ.
* 2. **Tùy chỉnh linh hoạt:** Thay đổi số lượng cụm (K) mong muốn thông qua các nút `+` và `-`.
* 3. **Chạy từng bước (Step-by-step):** Quan sát trực quan quá trình thuật toán tính toán khoảng cách Euclidean, gán nhãn dữ liệu và cập nhật lại vị trí các tâm cụm (centroids) khi nhấn nút `Run`.
* 4. **Khởi tạo ngẫu nhiên:** Nút `Random` giúp chọn lại vị trí ngẫu nhiên cho các tâm cụm để quan sát cách thuật toán hội tụ từ các điểm xuất phát khác nhau.
* 5. **Đối chiếu với thư viện chuẩn:** Nút `Algorithm` gọi trực tiếp module `KMeans` từ thư viện `scikit-learn` để trả về kết quả phân cụm tối ưu ngay lập tức, dùng để so sánh với thuật toán tự triển khai.
* 6. **Đo lường sai số:** Tự động tính toán và hiển thị trực tiếp giá trị Error (tổng khoảng cách từ các điểm dữ liệu đến tâm cụm tương ứng) trên giao diện.

---

## Công nghệ & Thư viện sử dụng

* **Ngôn ngữ:** Python 
* **Giao diện & Đồ họa:** Pygame 
* **Machine Learning:** Scikit-learn (`sklearn.cluster.KMeans`) 
* **Toán học:** Thư viện `math` (tính khoảng cách Euclidean) 
