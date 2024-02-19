## String input with Python

# name = input("Say your name: ")
# print("My name is " + name)

## Integer inputs with python
# print("Provide the values of A and B. It will calculate A + B = Output")
# num1, num2 = input().split()
# num1 = int(num1)
# num2 = int(num2)
# sum = num1 + num2
# print(f"{num1} + {num2} = {sum}")

## Floating point inputs with python
print("Provide the values of A and B as floating point numbers.\n"
      + " It will calculate A + B = Output")
num1, num2 = input().split()
num1 = float(num1)
num2 = float(num2)
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")

## Python doesn't have double types separately