import numpy as np
import matplotlib.pyplot as plt
from src.functions import rosenbrock, rosenbrock_grad

# --- Cài đặt lại GD Fixed Step & GD Backtracking riêng cho thực nghiệm này ---

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
    beta = 1e-4 # Tham số trong báo cáo
    p = 0.5     # Step reduction factor
    
    for i in range(n_iter):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-4: break
        
        # Backtracking Line Search logic
        d = -g
        alpha = 1.0 # Reset alpha mỗi bước (hoặc giữ lại tùy chiến lược)
        current_f = rosenbrock(x)
        
        # Vòng lặp tìm alpha thỏa mãn Armijo
        while rosenbrock(x + alpha * d) > current_f + beta * alpha * np.dot(g, d):
            alpha *= p
            if alpha < 1e-8: break
            
        x = x + alpha * d
        path.append(x)
    return np.array(path)

def run_experiment():
    start_point = np.array([-1.2, 1.0]) # Điểm khởi tạo theo báo cáo
    
    print("Đang chạy thực nghiệm...")
    
    # 1. Chạy Fixed Step
    path_fixed = gd_fixed_step(start_point, lr=0.002)
    print(f"- Fixed Step (lr=0.002): {len(path_fixed)} steps. Final: {path_fixed[-1]}")
    
    # 2. Chạy Backtracking
    path_backtrack = gd_backtracking(start_point)
    print(f"- Backtracking: {len(path_backtrack)} steps. Final: {path_backtrack[-1]}")
    
    # 3. Vẽ biểu đồ (Visualization)
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-0.5, 1.5, 400)
    X, Y = np.meshgrid(x, y)
    Z = (1 - X)**2 + 100 * (Y - X**2)**2 # Rosenbrock

    plt.figure(figsize=(10, 6))
    plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 40), cmap='jet', alpha=0.6)
    plt.plot(1, 1, 'k*', markersize=15, label='Global Min (1,1)') # Đích
    
    # Vẽ đường đi Fixed Step
    plt.plot(path_fixed[:, 0], path_fixed[:, 1], 'r-', linewidth=1.5, label=f'Fixed Step (lr=0.002)')
    
    # Vẽ đường đi Backtracking
    plt.plot(path_backtrack[:, 0], path_backtrack[:, 1], 'b-o', markersize=3, linewidth=1.5, label='Backtracking Line Search')
    
    plt.title('Comparison: Fixed Step vs Backtracking on Rosenbrock')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Lưu ảnh vào thư mục report
    save_path = 'report/images/result_experiment.png'
    plt.savefig(save_path, dpi=300)
    print(f"Đã lưu ảnh kết quả tại: {save_path}")
    plt.show()

if __name__ == "__main__":
    run_experiment()