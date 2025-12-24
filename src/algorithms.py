import numpy as np
from src.functions import rosenbrock, rosenbrock_grad



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

# --- ALGORITHM 3: BACKTRACKING LINE SEARCH ---
def backtracking_line_search(x, d, f, grad, alpha=1.0, p=0.5, beta=1e-4):
    y = f(x)
    g = grad(x)
    while f(x + alpha * d) > y + beta * alpha * np.dot(g, d):
        alpha *= p
        if alpha < 1e-8: break 
    return alpha

def zoom(alpha_lo, alpha_hi, phi, derphi, c1, c2):
    """
    Ham Zoom de tim alpha trong khoang [alpha_lo, alpha_hi]
    phi: ham muc tieu f(x_k + alpha * p_k)
    derphi: dao ham cua phi theo alpha
    """
    while True:
        # Noi suy (Interpolation) - o day dung Bisection don gian
        alpha_j = 0.5 * (alpha_lo + alpha_hi)
        
        phi_j = phi(alpha_j)
        phi_lo = phi(alpha_lo)
        
        # Kiem tra Armijo (Sufficient Decrease)
        if (phi_j > phi(0) + c1 * alpha_j * derphi(0)) or (phi_j >= phi_lo):
            alpha_hi = alpha_j
        else:
            derphi_j = derphi(alpha_j)
            
            # Kiem tra Strong Curvature
            if abs(derphi_j) <= -c2 * derphi(0):
                return alpha_j
            
            # Cap nhat khoang tim kiem
            if derphi_j * (alpha_hi - alpha_lo) >= 0:
                alpha_hi = alpha_lo
            alpha_lo = alpha_j

# --- ALGORITHM 4: BACKTRACKING LINE SEARCH ---
def strong_backtracking_line_search(f, grad_f, xk, pk, c1=1e-4, c2=0.9, max_iter=100):
    """
    f: ham muc tieu, grad_f: gradient
    xk: diem hien tai, pk: huong tim kiem
    """
    alpha_max = 2.0
    alpha = 1.0 # Buoc nhay khoi tao
    alpha_prev = 0.0
    
    # Dinh nghia ham phi(alpha) va dao ham cua no
    def phi(a): return f(xk + a * pk)
    def derphi(a): return np.dot(grad_f(xk + a * pk), pk)
    
    phi_0 = phi(0)
    derphi_0 = derphi(0)
    phi_prev = phi_0

    for i in range(1, max_iter):
        phi_curr = phi(alpha)
        
        # 1. Kiem tra dieu kien giam hoac gia tri ham tang len
        if (phi_curr > phi_0 + c1 * alpha * derphi_0) or \
           (i > 1 and phi_curr >= phi_prev):
            return zoom(alpha_prev, alpha, phi, derphi, c1, c2)
        
        derphi_curr = derphi(alpha)
        
        # 2. Kiem tra Strong Curvature
        if abs(derphi_curr) <= -c2 * derphi_0:
            return alpha
        
        # 3. Neu dao ham duong, diem toi uu nam ben trai
        if derphi_curr >= 0:
            return zoom(alpha, alpha_prev, phi, derphi, c1, c2)
            
        # Tang buoc nhay cho lan lap sau
        alpha_prev = alpha
        phi_prev = phi_curr
        alpha = min(2 * alpha, alpha_max)
        
    return alpha # Tra ve gia tri tot nhat tim duoc

# --- ALGORITHM 5: TRUST REGION ---
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

