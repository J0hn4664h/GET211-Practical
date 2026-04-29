def ratio(a, b):  # Division defined function
    return a / b

def product(a, b): # Multiplication defined function
    return a * b

voltage = 10
current = 2

# Applying multiplication based function
power = product(voltage, current)
print("Power =",power,"W")

# Applying division based function
resistance = ratio(voltage, current)
print("Resistance =",resistance,"Ω")
