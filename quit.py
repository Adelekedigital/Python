

mellow=1
melt=str(mellow)

print("")

message= ""
response={}

print("")

while message != "quit":
    response.append(message)
    message=input("Type something here. Watch out for quit. ")
    print("")
else:
    print(f"you quit but entered the following, {response}")
    
    
