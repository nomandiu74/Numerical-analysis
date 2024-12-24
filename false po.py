def f(x):
    return x**3 - x - 1

e = 0.001  # Tolerance level

def false(a, b):
    if f(a) * f(b) >= 0:
        print("Function has the same signs at the endpoints a and b. Choose different a and b.")
        return
    i = 1
    while True:
        # Calculate the point using the false position formula
        x0 = a - (f(a) * (b - a)) / (f(b) - f(a))
        print("n={}, a={:.3f}, b={:.3f}, x0={:.3f}, f(x0)={:.3f}".format(i, a, b, x0, f(x0)))
        
        if abs(f(x0)) < e:  # Check if the root is found
            print(f"Root found: {x0}")
            return
        
        # Update bounds based on the function value at x0
        if f(x0) > 0:
            b = x0
            print("update: b=x0")
        else:
            a = x0
            print("update: a=x0")
        
        i += 1

# Input values
a = float(input("Enter value of a: "))  # Use float for more precision
b = float(input("Enter value of b: "))  # Use float for more precision
false(a, b)