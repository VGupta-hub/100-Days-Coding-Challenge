# Optional Parameters

def f(a, L=[]):
    L.append(a)
    return L

f(1)

f(2)

f(3)

f(4)

f(5)

# Keyword Parameters

initial = 7
def f(x, y=3, z = initial):
    print("x, y, z, are: " + str(x) + ", "+ str(y)+ ", "+ str(z))

f(2)

f(x=2,z=8)

# Exercises

Question 1: Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.

initial = 6
def mult(x=3, y=initial):
    return x*y
    

mult(4)

Question 2: The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

def greeting(greeting="Hello ", name, excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

Question 3: Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.

def sum(intz=5, intx):
    return intz + intx

def sum( intx, intz=5):
    return intz + intx

sum(4)

Question 4: Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.

boolean = True
def test(x=3, y=boolean, dict1= {2:3, 4:5, 6:8}):
   return y and dict1.get(x,False)

test(5, dict1 = {5:4, 2:1}) 

Question 5: Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.

But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return True 
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False

checkingIfIn("Carrots")

checkingIfIn("Carrots",False)
