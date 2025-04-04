# Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables.
# But let’s write a program that enables users to do math, even without knowing Python.

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates
# and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z,
# with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!




#  prompt users for an arithmetic expression and then calculates and outputs the result as a floating-point value
expression = input("Expression: ")


# using split function, separated input response using space between input response content

x, y, z = expression.split(" ")

# called out the splitted input response and assigned an integer data types to both x and z
x = int(x)
y = y
z = int(z)


# conditional checking if y meets set operation criteria. If all criterias are met, operation can continue

if y != "+" and y != "-" and y != "/" and y != "*":
    print("wrong operator")
elif z == 0 and y == "/":
    print ("0 can't be divided")
else:
    if y == "+":
        sum=(x + z)
        print(float(sum))
    elif y == "-":
        sum=float(x - z)
        print(sum)
    elif y == "/":
        sum=float(x / z)
        print(sum)
    elif y == "*":
        sum=float(x * z)
        print(sum)



# First attempt

# x = input()
# # x = int(x)
# # print(type(x))
# # x = float(x)

# y = input()

# z = input()
# # z = int(z)
# # print(type(z))
# # z = float(z)

# # sum = (f"{x} {y} {z}")

# # print(sum)



# 2nd attempt works but with limited conditional check

# if y == "+":
#     sum=(x + z)
#     print(float(sum))
# elif y == "-":
#     sum=(x - z)
#     print(float(sum))
# elif y == "/":
#     sum=(x / z)
#     print(float(sum))
# elif y == "*":
#     sum=(x * z)
#     print(float(sum))


# if y == "+":
#     sum=float(int(x) + int(z))
#     print(sum)
# elif y == "-":
#     sum=float(int(x) - int(z))
#     print(sum)
# elif y == "/":
#     sum=float(int(x) / int(z))
#     print(sum)

# elif y == "*":
#     sum=float(int(x) * int(z))
#     print(sum)


