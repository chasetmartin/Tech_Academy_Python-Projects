mydict = {'user1': {'fname': 'Chase', 'lname': 'Martin', 'contact': 'email'}, 'user2': {'fname': 'Molly', 'lname': 'Hayes', 'contact': 'phone'}}

print(mydict.get('user2'))

mydict['user1']['contact'] = 'phone'
print(mydict.get('user1'))

mydict['user1']['email'] = 'cats@gmail.com'
print(mydict.get('user1'))


