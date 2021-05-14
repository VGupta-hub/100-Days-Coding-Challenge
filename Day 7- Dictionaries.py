# Dictionary is an unordered collection of data values.
# Unlike other data types, Dictionary holds key:value pair.
# Values in dictionary can be of any datatype and can be duplicated, whereas keys can't be repeated and must be immutable.

# Creating a Dictionary
# with Integer Keys
Dict = {1 : "Geeks", 2: "For", 3: "Geeks"}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {"Name" : "Geeks", 1: [1,2,3,4]}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Dictionary can also be created by the built-in function dict().
# An empty dictionary can be created by just placing to curly braces{}.
Dict = {}
print("\nEmpty dictionary: ")
print(Dict)

# Creating a dictionary with dict() method
Dict = dict({1: "Geeks", 2 : "for", 3 : "Geeks"})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a dictionary with each item as a pair
Dict = dict([(1,"Geeks"), (2, "For")])
print("\nDictionary with the use of dict(): ")
print(Dict)

# Adding elements to a Dictionary

# Adding elements one at a time
Dict = {}
Dict[0] = "Geeks"
Dict[1] = "For"
Dict[2] = "geeks"
Dict["Value set"] = 2,3,4
print("\nNew Dictionary: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated Dictionary: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {"Fifth" : {"1": "Live", "2": "Life"}}
print("\nAdding a Nested Key: ")
print(Dict)

# accessing a element using key
Dict = {1: "Geeks", 2 : "for", 3 : "Geeks"}
print("\n")
print(Dict[2])

# accessing a element using get()
# method
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\n")
print(Dict.get(4, "Not found"))

arr = {12,10,9,45,2,10,10,45}
for i in arr:
    if i ==12 or i ==2:
        continue
    print(i, end= "")



