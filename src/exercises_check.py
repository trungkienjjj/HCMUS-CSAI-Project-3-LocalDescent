import numpy as np

def check_exercise_4_2():
    print("=== CHECKING EXERCISE 4.2 ===")
    
    # Đề bài
    def f(x): return 5 + x[0]**2 + x[1]**2
    x_k = np.array([-1.0, -1.0])
    d = np.array([1.0, 0.0])
    beta = 1e-4
    
    # Lý thuyết tính tay ra alpha <= 1.9998
    alpha_theory = 1.9998
    
    # Kiểm tra điều kiện Wolfe 1 (Sufficient Decrease)
    # f(x + alpha*d) <= f(x) + beta * alpha * (grad^T * d)
    
    fx = f(x_k) # f(x) = 7
    grad = np.array([2*x_k[0], 2*x_k[1]]) # [-2, -2]
    slope = np.dot(grad, d) # -2
    
    # Vế trái (LHS)
    lhs = f(x_k + alpha_theory * d)
    
    # Vế phải (RHS)
    rhs = fx + beta * alpha_theory * slope
    
    print(f"Alpha check: {alpha_theory}")
    print(f"LHS (Actual f): {lhs:.6f}")
    print(f"RHS (Armijo condition): {rhs:.6f}")
    
    if lhs <= rhs:
        print("-> KẾT QUẢ: Thỏa mãn điều kiện giảm đủ!")
    else:
        print("-> KẾT QUẢ: Không thỏa mãn!")

if __name__ == "__main__":
    check_exercise_4_2()
