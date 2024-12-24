def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

e = 0.001

def raphson(a, b):
    x0 = (a + b) / 2  # Correctly calculate the midpoint
    x1 = x0 - f(x0) / df(x0)
    i = 1

    while abs(f(x1)) > e:
        print("n={}; x0={:.4f}; f(x0)={:.4f}; df(x0)={:.4f}; x1={:.4f}; f(x1)={:.4f}".format(i, x0, f(x0), df(x0), x1, f(x1)))

        x0 = x1  # Update x0 for the next iteration
        x1 = x0 - f(x0) / df(x0)  # Calculate the next approximation

        i += 1

    print("Approximate root is: {:.4f}".format(x1))

a = float(input("Enter the values of a: "))
b = float(input("Enter the values of b: "))
raphson(a, b)