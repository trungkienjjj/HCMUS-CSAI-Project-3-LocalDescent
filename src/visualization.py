import numpy as np
import matplotlib.pyplot as plt
from src.functions import rosenbrock

def plot_comparison(results, filename='comparison_result.png'):
    # Tạo lưới điểm để vẽ contour
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-1, 3, 400)
    X, Y = np.meshgrid(x, y)
    Z = (1 - X)**2 + 100 * (Y - X**2)**2 # Rosenbrock formula inline

    plt.figure(figsize=(12, 8))
    # Vẽ contour map
    plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 30), cmap='gray', alpha=0.4)
    
    colors = ['red', 'blue', 'green', 'purple']
    markers = ['o', 'v', 's', '*']
    
    for idx, (path, name) in enumerate(results):
        plt.plot(path[:, 0], path[:, 1], 
                 marker=markers[idx], 
                 color=colors[idx], 
                 label=f'{name} - Steps: {len(path)-1}', 
                 markersize=4, alpha=0.8, linewidth=1.5, markevery=5) # Markevery cho đỡ rối
        
        # Đánh dấu điểm đầu và cuối
        plt.plot(path[0,0], path[0,1], 'kX', markersize=12) # Start
        plt.plot(path[-1,0], path[-1,1], 'X', color=colors[idx], markersize=12) # End

    plt.title('Comparison of Local Descent Algorithms on Rosenbrock Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    
    plt.savefig(filename, dpi=300)
    print(f"Đã lưu biểu đồ vào file: {filename}")
    plt.show()