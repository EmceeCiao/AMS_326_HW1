import numpy as np  
def f(x):   
    """Function defined for f(x) evaluating the function for the x_value passed in"""
    # The FLOPS of the below equation is around 17, 4 for sin, 4 for e, 3 for -x^3 and 3 for x^4, 2 for -
    return np.exp(-x**3) - x**4 - np.sin(x)
 
def bisection_method(a, b, f, tolerance, actual_root):  
    """ 
    Inputs: 
    - a: Left starting point 
    - b: Right starting point 
    - f: function we are finding the root of 
    - tolerance: The error we are tolerating for our break point 
    - actual_root: The actual root of the function 

    Output: 
    - [(a+b)/2, flops, iterations] 
    - (a+b)/2: root found 
    - flops: Floating Point Operations done 
    - iterations: The number of iterations the method took to find the answer
    """  
    flops = 0 
    iterations = 0 
    while (b-a)/2 > tolerance: 
        flops += 2 
        iterations += 1 
        c = (a+b)/2 
        flops += 2 
        val = f(c) 
        flops += 18 # One more for the check right below
        if abs(c-actual_root) < tolerance:  
            return [c, flops, iterations]   
        
        # If f(c) * f(a) < 0, it lies in [a, c] range
        elif val * f(a) < 0: 
            flops +=18 
            b = c  
        # Otherwise it lies in [c, b]
        else: 
            flops += 18  
            a = c  
    return [(a+b)/2, flops, iterations] 

# Using Bisection Method and Printing Formatted Results
results = (bisection_method(-1, 1, f, 0.5*10**-4, 0.641583)) 
print("Root: ", results[0]) 
print("Flops: ", results[1]) 
print("Iterations: ", results[2])