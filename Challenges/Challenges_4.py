mySet = {"baseball", "hockey", "football"}
print(mySet)

mySet.add("Soccer")
print(mySet)

mySet.remove("football")
print(mySet)

mySet2 = {"baseball", "golf"}

mySet3 = mySet.difference(mySet2)

print(mySet3)
