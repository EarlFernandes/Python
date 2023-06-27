def factorial(n):
    y = 1
    for i in range(int(n)):
        y = y*(i+1)
    return y

print(factorial(input()))