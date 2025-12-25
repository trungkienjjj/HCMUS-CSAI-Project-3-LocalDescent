# Đồ án 3: Local Descent (Tối ưu hóa Cục bộ)
**Môn học:** Cơ sở Trí tuệ Nhân tạo (CSAI) - HCMUS  
**Chủ đề:** Chương 4 - Algorithms for Optimization (Kochenderfer & Wheeler)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📌 Giới thiệu
Đồ án này tập trung nghiên cứu và hiện thực các thuật toán **Local Descent** để tìm cực tiểu địa phương của hàm mục tiêu. Dự án bao gồm việc trình bày lại lý thuyết Chương 4, giải bài tập và so sánh hiệu quả thực nghiệm giữa các chiến lược chọn bước nhảy (Step Size) và hướng đi (Direction).

**Các thuật toán được hiện thực:**
1.  **Gradient Descent cơ bản** (Fixed Step Size).
2.  **Backtracking Line Search** (Chiến lược bước nhảy thích nghi - Chương 4).
3.  **Trust Region Methods** (Phương pháp vùng tin cậy - Chương 4).
4.  **Momentum** (Mở rộng - Giúp vượt điểm yên ngựa).
5.  **Adam Optimizer** (Mở rộng - State-of-the-art trong Deep Learning).

---

## 👥 Thành viên Nhóm
| STT | Họ và Tên | MSSV | Vai trò |
|-----|-----------|------|---------|
| 1   | Nguyễn Trần Trung Kiên | [MSSV] | [Vai trò] |
| 2   | [Tên thành viên 2] | [MSSV] | [Vai trò] |
| 3   | [Tên thành viên 3] | [MSSV] | [Vai trò] |
| 4   | [Tên thành viên 4] | [MSSV] | [Vai trò] |

---

## 📂 Cấu trúc Thư mục
```text
CSAI_Project3_LocalDescent/
│
├── main.py                     # Script chính chạy so sánh tổng quan 4 thuật toán
├── requirements.txt            # Danh sách thư viện cần thiết
├── README.md                   # Hướng dẫn sử dụng
│
├── src/                        # Mã nguồn chính (Source Code)
│   ├── algorithms.py           # Cài đặt GD, Line Search, Trust Region, Adam, Momentum
│   ├── functions.py            # Định nghĩa hàm Rosenbrock và Gradient
│   ├── visualization.py        # Module vẽ đồ thị và Contour map
│   ├── experiment_rosenbrock.py # Script thực nghiệm so sánh Fixed Step vs Backtracking
│   └── exercises_check.py      # Script kiểm chứng bài tập toán học (Bài 4.2)
│
└── report/                     # Báo cáo và Kết quả
    ├── main.tex                # Source LaTeX báo cáo
    └── images/                 # Chứa ảnh kết quả thực nghiệm
        ├── result_chart.png
        └── result_experiment.png
