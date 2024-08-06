import sys

num1 = int(input("> "))
num2 = int(input("> "))

if num1 <= 0 or num2 <= 0:
    print("Os números devem ser inteiros positivos")
    sys.exit()

while num2 != 0:
    num1, num2 = num2, num1 % num2
    print(num1)

