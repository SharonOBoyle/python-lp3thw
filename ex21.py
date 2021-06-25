def add(a, b):
    print(f">>> add: a={a}, b={b}")
    print(f"ADDING {a} + {b}")
    print(f"<<< add: a={a}, b={b}")
    return a + b

def subtract(a, b):
    print(f">>> subtract: a={a}, b={b}")
    print(f"SUBTRACTING {a} - {b}")
    print(f"<<< subtract: a={a}, b={b}")
    return a - b

def multiply(a, b):
    print(f">>> multiply: a={a}, b={b}")
    print(f"MULTIPLYING {a} * {b}")
    print(f"<<< multiply: a={a}, b={b}")
    return a * b

def divide(a, b):
    print(f">>> divide: a={a}, b={b}")
    print(f"DIVIDING {a} / {b}")
    print(f"<<< divide: a={a}, b={b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
print(">>>> age=", age)
height = subtract(78, 4)
print(">>>> height=", height)
weight = multiply(90, 2)
print(">>>> weight=", weight)
iq = divide(100, 2)
print(">>>> iq=", iq)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("here is a puzzle.")

# what = age + (height - (weight * iq/2))
#      = 35 + (74 - (180 * 50/2))
#      = 35 - (74 - 4500)
#      = 35 - 4426 = 4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Another puzzlie
print("here is my own puzzle.")

# why = height / weight - age * iq = -1749.588888888889
why = subtract(divide(height, weight), multiply(age, iq))
print("height / weight - age * iq= ", why)

# another example: 24 + 34 / 100 -1023 = -998.66
print(subtract(add(24, divide(34, 100)), 1023))
