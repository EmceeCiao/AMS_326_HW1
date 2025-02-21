import numpy as np 

def lagrange_interpolate(t_values, y_values, point):  
    """
    Function to use create and use a lagrange interpolation  

    Inputs: 
    t_values: Array of t values passed in for the points (A point is of the form (t, y))
    y_values: Array of y values passed in for the points of the form (A point is of the form (t, y))
    point: t value we are attempting to interpolate for 

    Outputs:  
    - prints the FLOPS, Interpolating Function along with the value for it at the point passed in 
    - result: the result of the point found by the interpolating function 
    - flops: the number of Floating Point Operations done
    """ 
    n = len(t_values) 
    terms = []     
    result = 0 
    flops = 0  

    for i in range(len(t_values)):   
        coeff = y_values[i]   
        str = f"{y_values[i]}"
        for j in range(len(t_values)): 
            if i != j: 
                coeff *= (point - t_values[j])/(t_values[i]-t_values[j]) 
                str += f" * (t - {t_values[j]} / {t_values[i]} - {t_values[j]})"  
                flops += 4 # Conservatively, there are 4 operations here which may be done on floats
        terms.append(str) 
    
        result += coeff   

    print(f"Final Lagrange Polynomial of Order {n}:") 
    print(" +\n".join(terms))   

    print(f"\nP(t = {point}) = {result}") 
    print(f"Floating Point Operations: {flops}")
    return result, flops 

t_values = [5, 4, 3, 2, 1] 
y_values = [417, 398, 397, 407, 412]    

lagrange_interpolate(t_values, y_values, 6) 
print("")
