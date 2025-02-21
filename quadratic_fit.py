import numpy as np

def quadratic_fit(t_values, y_values, point_value): 
    """ 
    Function to both create the quadratic fit function and print out the results achieved when evaluating the function at a specific point_value 

    Input: 
    t_values: Array of t values passed in for the points (A point is of the form (t, y))
    y_values: Array of y values passed in for the points of the form (A point is of the form (t, y))
    point: t value we are evaluating our quadratic fit for 

    Output: 
    prints the quadratic fit equation and the value of computing the quadratic fit for the t value passed in 
    """ 

    t_values = np.array(t_values) 
    y_values = np.array(y_values) 

    n = len(t_values) 

    A = np.vstack([np.ones(n), t_values, t_values**2]).T

    # Need to create A^TA and A^Tb and then solve these 

    A_TA = np.dot(A.T, A) 

    A_Ty = np.dot(A.T, y_values)  

    #Solves for the coefficients
    coeffs = np.linalg.solve(A_TA, A_Ty)    

    a_0 = coeffs[0] 
    a_1 = coeffs[1] 
    a_2 = coeffs[2] 

    print(f"Q_2(t) = {a_0} + {a_1}t + {a_2}t^2\n")   
    ans = a_0 + (a_1*point_value) + (a_2 * point_value**2)
    print(f"Q_2(t = {point_value}) = {ans}") 

t_values = [5, 4, 3, 2, 1]  
y_values = [417, 398, 397, 407, 412]    

quadratic_fit(t_values, y_values, 6)