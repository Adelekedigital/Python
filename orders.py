# A fast-food restaurant takes customer orders and stores them in a tuple to ensure they remain unchanged once confirmed.

# Instructions:

# Create a tuple named order that contains the following items: ("Burger", "Fries", "Soda").

order = (
    "Burger",
    "Fries",
    "Soda"
    )
    
# The restaurant now offers a "Super Meal" combo, which includes an additional "Ice Cream". However, tuples are immutable

# Convert the tuple into a list

super_meal = list(order)

# add "Ice Cream"

super_meal.append("Ice Cream")

# convert it back into a tuple.

update_meal = tuple(super_meal)

# Print the modified tuple to confirm the update.

print(update_meal)

# Retrieve and print the first using the index positions

print(update_meal[0])

# Retrieve and print the last using the index positions

print(update_meal[3])
