

print("")

# request response from users using the input function
response=input("what is the answer to the great question of life, the universe, and everything? " )


# carried out text operation, allowing input response to accept any form of input style
newresponse=response.strip().casefold()

# conditional to check if input response falls in the range of 42, forty-two, or forty two
if newresponse == "42":
    print("yes")
elif newresponse == "forty-two":
    print("yes")
elif newresponse == "forty two":
    print("yes")
else:
    print("No")






# if response == ("42") or ("forty-two") or ("forty two"):
#     print("Yes")
# else:
#     print("No")



