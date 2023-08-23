def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 10
print(f"{number}-е число Фибоначчи = {fibonacci(number)}")
