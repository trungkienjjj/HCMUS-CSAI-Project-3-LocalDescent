import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# --- [FIX 1] TỰ ĐỘNG SỬA LỖI IMPORT ---
# Thêm thư mục cha (project root) vào đường dẫn tìm kiếm của Python
# Giúp chạy file này trực tiếp mà không bị lỗi ModuleNotFoundError
current_dir = os.path.dirname(os.path.abspath(__file__)) # Lấy đường dẫn thư mục src/
parent_dir = os.path.dirname(current_dir)              # Lấy đường dẫn thư mục dự án
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from src.functions import rosenbrock, rosenbrock_grad

# --- Cài đặt thuật toán ---

def gd_fixed_step(start_x, lr=0.002, n_iter=5000):
    path = [start_x]
    x = start_x.copy()
    for i in range(n_iter):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-4: break
        x = x - lr * g
        path.append(x)
    return np.array(path)

def gd_backtracking(start_x, n_iter=1000):
    path = [start_x]
    x = start_x.copy()
    alpha = 1.0
    beta = 1e-4
    p = 0.5
    
    for i in range(n_iter):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-4: break
        
        d = -g
        alpha = 1.0 # Reset alpha
        current_f = rosenbrock(x)
        
        while rosenbrock(x + alpha * d) > current_f + beta * alpha * np.dot(g, d):
            alpha *= p
            if alpha < 1e-8: break
            
        x = x + alpha * d
        path.append(x)
    return np.array(path)

def run_experiment():
    start_point = np.array([-1.2, 1.0])
    print("Đang chạy thực nghiệm...")
    
    # 1. Chạy thuật toán
    path_fixed = gd_fixed_step(start_point, lr=0.002)
    print(f"- Fixed Step: {len(path_fixed)} steps.")
    
    path_backtrack = gd_backtracking(start_point)
    print(f"- Backtracking: {len(path_backtrack)} steps.")
    
    # --- [FIX 2] CẢI THIỆN BIỂU ĐỒ ---
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-0.5, 1.5, 400)
    X, Y = np.meshgrid(x, y)
    Z = (1 - X)**2 + 100 * (Y - X**2)**2

    plt.figure(figsize=(12, 8))
    
    # Dùng màu xám (gray) và làm mờ (alpha=0.3) để nền không lấn át đường đi
    plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 50), cmap='gray', alpha=0.3)
    
    plt.plot(1, 1, 'k*', markersize=18, label='Global Min (1,1)', zorder=10)
    
    # Đường Fixed Step: Màu ĐỎ
    plt.plot(path_fixed[:, 0], path_fixed[:, 1], 
             color='#D62728', linewidth=2, label=f'Fixed Step ({len(path_fixed)} steps)')
    
    # Đường Backtracking: Màu XANH DƯƠNG (Nổi bật trên nền xám)
    plt.plot(path_backtrack[:, 0], path_backtrack[:, 1], 
             color='#1F77B4', linewidth=2, marker='o', markersize=4, markevery=30,
             label=f'Backtracking ({len(path_backtrack)} steps)', zorder=5)
    
    plt.title('Comparison: Fixed Step vs Backtracking Line Search', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.4)
    
    # Tự động tạo thư mục nếu chưa có (Tránh lỗi FileNotFoundError)
    save_path = os.path.join(parent_dir, 'report', 'images', 'result_experiment.png')
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Đã lưu ảnh kết quả tại: {save_path}")
    plt.show()

if __name__ == "__main__":
    run_experiment()