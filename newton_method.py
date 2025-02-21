import numpy as np 
import math  

def f(x):  
    # The FLOPS of the below equation is around 17
    return np.exp(-x**3) - x**4 - np.sin(x)

def f_prime(x):   
    # The FLOPS of the below equations is around 19
    # 4 for e, 4 for cos, 2 for 3x^2, 3 for -x^3, 3 for 4x^3, 3 for - and * between 3x^2 and e^-x^3
    return -3 * x**2 * np.exp(-x**3) - 4*x**3 - np.cos(x)

def newton_method(x0, actual_root, f, f_prime, tolerance, max_iterations): 
    """ 
    Inputs: 
    - x0: Initial root used for Newton's Method 
    - actual_root: Actual root of the function used to break early
    - f : function that newton's method is being called on
    - f_prime: derivative of function that newton's method is being called on 
    - tolerance: Our tolerance for error from the actual root
    - max_iterations: Iteration limit set to prevent infinite looping
    
    Outputs: 
    - [x_n, flops, iterations] 
    - x_n: root found by newton's method 
    - flops: Floating Point Operations done 
    - iterations: The number of iterations the method took to find the answer
    """ 
    x_n = x0 
    iterations = 0 
    flops = 0 
    while(iterations < max_iterations): 
        iterations += 1 
        x_n = x_n - (f(x_n)/f_prime(x_n)) 
        flops += 38 # 2 more flops from subtraction and division! (17 + 19 + 2)   

        # Check if guess is close enough 
        if(abs(x_n - actual_root) < tolerance):   
            break

    return [x_n, flops, iterations]

results = newton_method(0, 0.641583, f, f_prime, 0.5*10**-4, 100) 
print("Root: ", results[0]) 
print("Flops: ", results[1]) 
print("Iterations: ", results[2])