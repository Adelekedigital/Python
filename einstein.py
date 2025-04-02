

# Even if you haven’t studied physics (recently or ever!), you might have heard that
# , wherein
#  represents energy (measured in Joules),
#  represents mass (measured in kilograms), and
#  represents the speed of light (measured approximately as 300000000 meters per second),
#  per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.


# store value of mass(kg) in a "m" variable
m = input("Tell your mass and check your energy ")

# data type conversion from string to integer
m = int(m)

# return the input value of "m" and store in the "e" value as energy(joules)
e = m * pow(3 * pow(10, 8), 2)


# print the value of "e"
print(e)


