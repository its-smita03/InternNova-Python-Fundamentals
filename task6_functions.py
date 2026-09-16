def square(n):
    return n * n

def average(a, b, c):
    return (a + b + c) / 3

n = int(input("Enter a number: "))
print("Square:", square(n))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Average:", average(a, b, c))
