import numpy as np  
import random

def monte_carlo_method(actual_root, lower_bound, upper_bound, tolerance):   
    """
    Monte Carlo Method of producing root through known actual root 

    Input: 
    - actual_root: Known root of function we are trying to approximate to 
    - lower_bound: Inclusive lower bound of random number generation 
    - upper_bound: Inclusive upper bound of random number generation 
    - tolerance: tolerance given for difference between guess and actual_root 

    Output: 
    - [guess, flops, iterations] 
    - guess: Successful guess/approximation of root 
    - flops: Floating Point Operations Used for the method 
    - iterations: Total number of iterations the method used
    """ 
    iterations = 0  
    flops = 0 
    guess = 0 
    lower_bound = int(lower_bound * 1000000) 
    upper_bound = int(upper_bound * 1000000) 
    flops += 2
    while True:    
        flops+= 6 # according to ChatGPT the PRNG of Python randrange takes around 6 flops
        iterations += 1  
        guess = random.randrange(lower_bound, upper_bound, 1)/1000000
        if (abs(guess-actual_root) < tolerance): 
            break
        
    return [guess, flops, iterations]

results = monte_carlo_method(0.641583, 0.50, 0.75, 0.5*10**-4) 

print("Root: ", results[0]) 
print("Flops: ", results[1]) 
print("Iterations: ", results[2])