import numpy as np
from src.algorithms import gradient_descent, momentum_descent, adam_descent, trust_region
from src.visualization import plot_comparison

if __name__ == "__main__":
    # Điểm bắt đầu khó (xa điểm cực tiểu 1,1)
    start_point = np.array([-1.5, 2.0])
    
    print(f"Bắt đầu tối ưu từ điểm: {start_point}")
    print("-" * 50)
    
    # 1. Chạy Gradient Descent (Sách GK)
    path_gd, name_gd = gradient_descent(start_point)
    print(f"Xong {name_gd}: {len(path_gd)} bước.")
    
    # 2. Chạy Trust Region (Sách GK)
    path_tr, name_tr = trust_region(start_point)
    print(f"Xong {name_tr}: {len(path_tr)} bước.")

    # 3. Chạy Momentum (Mở rộng)
    path_mom, name_mom = momentum_descent(start_point)
    print(f"Xong {name_mom}: {len(path_mom)} bước.")
    
    # 4. Chạy Adam (Mở rộng SOTA)
    path_adam, name_adam = adam_descent(start_point)
    print(f"Xong {name_adam}: {len(path_adam)} bước.")
    
    print("-" * 50)
    print("Đang vẽ biểu đồ...")
    
    # Vẽ và lưu ảnh
    results = [
        (path_gd, name_gd),
        (path_tr, name_tr),
        (path_mom, name_mom),
        (path_adam, name_adam)
    ]
    plot_comparison(results, filename='report/images/result_chart.png') # Lưu thẳng vào thư mục report