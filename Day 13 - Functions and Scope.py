# Defining a new function

The round brackets or parentheses () and colon : after the function's name. Both are essential parts of the syntax. 

def say_hello():
    print("Hello There")
    print("How are you?")
    print("How is it going?")

say_hello()

# Defining a function with arguments

def say_hi(name):
    print("Hi {}!".format(name))
    

say_hi("John")

say_hi("Jane")

Functions can return a result that can be stored in a variable or used in other expressions.

Here's a function that filters out the even numbers from a list and returns a new list using the return keyword.

def filter_even(number_list):
    result_list = []
    for i in number_list:
        if i % 2 == 0:
            result_list.append(i)
    return result_list

even_list = filter_even([1,2,3,4,5,6,7,8,9])
even_list

filter_even([5,9,11,13])
