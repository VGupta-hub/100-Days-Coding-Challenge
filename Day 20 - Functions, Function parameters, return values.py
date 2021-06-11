def hello():
    print("Hello!")
    print("Glad to meet you.")

hello()

def hello(s):
    print("Hello " + s)
    print("Glad to meet you.")

hello("Iman")

hello("Ankush")

def hello3(s, n):
    greeting = "Hello {} ".format(s)
    print(greeting*n)

hello3("Ankush",2)

hello3("Ankush",2)
hello3("",1)
hello3("Kitty",10)

def square(x):
    y = x*x
    #return y
    print("The result of {} squared is {}.".format(x,y))

square(10)

def total(lst):
    tot = 0
    for num in lst:
        tot += num
    return tot

total([4,5,6])

