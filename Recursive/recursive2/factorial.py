def factorial(num):
    if num == 0:
        return 1
    if num > 0:
        return num*factorial(num-1)

inp =int(input("Enter Number : "))
print(f'{inp}! = {factorial(inp)}')     