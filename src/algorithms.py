import numpy as np
from src.functions import rosenbrock, rosenbrock_grad

# --- HELPER: BACKTRACKING LINE SEARCH (CHƯƠNG 4) ---
def backtracking_line_search(x, d, f, grad, alpha=1.0, p=0.5, beta=1e-4):
    y = f(x)
    g = grad(x)
    while f(x + alpha * d) > y + beta * alpha * np.dot(g, d):
        alpha *= p
        if alpha < 1e-8: break 
    return alpha

# --- ALGORITHM 1: BASIC GRADIENT DESCENT ---
def gradient_descent(start_x, n_iter=2000):
    path = [start_x]
    x = start_x.copy()
    
    for i in range(n_iter):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-6: break
        
        d = -g
        alpha = backtracking_line_search(x, d, rosenbrock, rosenbrock_grad)
        x = x + alpha * d
        path.append(x)
        
    return np.array(path), "Gradient Descent (Basic)"

# --- ALGORITHM 2: MOMENTUM (EXTENSION) ---
def momentum_descent(start_x, lr=0.001, gamma=0.9, n_iter=2000):
    path = [start_x]
    x = start_x.copy()
    v = np.zeros_like(x)
    
    for i in range(n_iter):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-6: break
        
        v = gamma * v + lr * g
        x = x - v
        path.append(x)
        
    return np.array(path), "Momentum (Extension)"

# --- ALGORITHM 3: ADAM (EXTENSION - STATE OF THE ART) ---
def adam_descent(start_x, lr=0.2, beta1=0.9, beta2=0.999, epsilon=1e-8, n_iter=2000):
    path = [start_x]
    x = start_x.copy()
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    
    for t in range(1, n_iter + 1):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-6: break
        
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g**2)
        
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        
        x = x - lr * m_hat / (np.sqrt(v_hat) + epsilon)
        path.append(x)
        
    return np.array(path), "Adam (Extension)"

# --- ALGORITHM 4: TRUST REGION (CHƯƠNG 4) ---
def trust_region(start_x, n_iter=1000, max_radius=1.0):
    path = [start_x]
    x = start_x.copy()
    radius = 0.5
    
    for i in range(n_iter):
        g = rosenbrock_grad(x)
        if np.linalg.norm(g) < 1e-6: break
        
        # 1. Solve Subproblem (Cauchy Point)
        d = -g
        d_norm = np.linalg.norm(d)
        if d_norm == 0: break
        
        # Cauchy step bi gioi han boi radius
        step_len = min(d_norm, radius) / d_norm
        step = step_len * d
        
        # 2. Evaluate Rho
        pred_red = -np.dot(g, step) 
        actual_red = rosenbrock(x) - rosenbrock(x + step)
        
        rho = 0
        if pred_red > 0:
            rho = actual_red / pred_red
            
        # 3. Update Radius
        if rho < 0.25:
            radius *= 0.5
        elif rho > 0.75 and np.linalg.norm(step) >= radius * 0.99:
            radius = min(2 * radius, max_radius)
            
        # 4. Accept Step
        if rho > 0:
            x = x + step
            path.append(x)
            
    return np.array(path), "Trust Region (Basic)"