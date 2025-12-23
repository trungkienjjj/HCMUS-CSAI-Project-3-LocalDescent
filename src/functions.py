import numpy as np

def rosenbrock(x):
    """
    Hàm Rosenbrock (Hàm thung lũng)
    f(x, y) = (1 - x)^2 + 100 * (y - x^2)^2
    Minima toàn cục tại (1, 1) với f(x) = 0
    """
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def rosenbrock_grad(x):
    """
    Đạo hàm (Gradient) của hàm Rosenbrock
    """
    df_dx = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
    df_dy = 200 * (x[1] - x[0]**2)
    return np.array([df_dx, df_dy])