a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

# Function: f(x) = x^3 - x - 1
def f(x):
    return x**3 - x - 1

# Bisection method loop
iteration = 1
while abs(b - a) > 0.0001:
    c = (a + b) / 2  # Update midpoint
    print(f"Step {iteration}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")  # Print each step

    if f(c) == 0:    # If we found the root exactly
        break
    elif f(c) > 0:   # The root is in the left half
        b = c
    else:            # The root is in the right half
        a = c

    iteration += 1  # Increment iteration count

# Print the approximate root
print(f"\nThe approximate root is: {c}")
