


# test = {
#     "name" : "Junior",
#     "age" : 32,
#     "country" : "Nigeria"
# }

# print(test["name"])


test2 = (
    country := ("nigeria", "ghana", "england"),
    state := ("abuja", "accra", "london")
)

print(type(test2))

test2 = dict(zip(country,state))

print(test2)
print(type(test2))