import numpy as np

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Implements the bisection method to find a root of a function.

    Args:
        func (function): The function for which to find the root.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The tolerance for the root approximation.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The approximate root of the function.
        None: If a root is not found within the maximum iterations or interval issues.
    """
    if func(a) * func(b) >= 0:
        print("Bisection method requires f(a) and f(b) to have opposite signs.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("Root not found within the maximum number of iterations.")
    return None

# Example usage: Find the root of f(x) = x^3 - 2x^2
my_function = lambda x: x**3 - 2*x**2


root = bisection_method(my_function, 1.5, 3)
print(f"Approximate root: {root}")