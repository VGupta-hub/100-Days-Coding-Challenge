def square(x):
    y = x*x
    return y

def sum_of_squares(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a+b+c

a = -5
b = 2
c = 10
result = sum_of_squares(a,b,c)
print(result)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

print(most_common_letter("aaaaaanksfklnfksanfllllllllllfknifhiwhfsannnnnnnnnnnnnkokioqyyyyyyyyyyyy"))

# Exercises

Question 1 : Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(integer):
    return integer

int_return(5)

Question 2 : Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(integer):
    sum = integer + 2
    return sum

add(4)

Question 3: Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

def change(s):
    new_string = s + "Nice to meet you!"
    return new_string

change("Hello Bob. ")

Question 4: Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum

lst = [2,3,5,2,1,2]
accum(lst)

Question 5: Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.

def length(lst):
    if len(lst) >= 5:
        return("Longer than 5")
    else:
        return("Less than 5")
    
lst = [5,6,7,8,9,5,6]
length(lst)

Question 6: You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.

def divide(n):
    return n/2
def sum(n):
    return n/2+6

sum(divide(10))

