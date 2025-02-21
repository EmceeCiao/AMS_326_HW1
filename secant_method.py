import numpy as np 
import math  

def f(x): 
# The FLOPS of the below equation is around 17
    return np.exp(-x**3) - x**4 - np.sin(x) 

def secant_method(x0, x1, actual_root, f, tolerance, max_iterations): 
    """ 
    Inputs:  
    - x0: one of two intial guesses for root used in secant method 
    - x1: one of two intial guesses for root used in secant method 
    - actual_root: actual root of the function 
    - f: function that secant method is being called on 
    - tolerance: Our tolerance for error from the actual root
    - max_iterations: Iteration Limit set to prevent infinite looping

    Outputs:  
    - [x1, flops, iterations] 
    - x1: root found by secant's method 
    - flops: Floating Point Operations done 
    - iterations: The number of iterations the method took to find the answer
    """ 
    x0 = x0 
    x1 = x1 
    iterations = 0 
    flops = 0 
    while(iterations < max_iterations):   
        iterations += 1
        temp = x1  

        # Formula
        x1 = x1 - ((x1-x0) * (f(x1)/(f(x1)-f(x0)))) 
        x0 = temp  
        flops += 56  

        # Break when reacing desired tolerance
        if(abs(x1 - actual_root) < tolerance): 
            break 
    return [x1, flops, iterations] 

results = secant_method(-1, 1, 0.641583, f, 0.5*10**-4, 100) 
print("Root: ", results[0]) 
print("Flops: ", results[1]) 
print("Iterations: ", results[2])
        
    