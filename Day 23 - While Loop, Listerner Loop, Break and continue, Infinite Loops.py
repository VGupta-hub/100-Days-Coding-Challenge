# Defining a function with While Loop

def sumTo(n):
    """Return the sum of 1+2+3+.....+n"""
    
    the_sum = 0 #current sum
    a_number = 1 #where we are
    while a_number <= n:
        the_sum += a_number
        a_number += 1
    return the_sum

print(sumTo(5))

Question : Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.

count = 0
eve_nums = []
while count <=15:
    if count%2 == 0:
        eve_nums.append(count)
    count += 1
print(eve_nums)

Question : Below we've provided a for loop that sums all the elements of list1.
            Write a code that accomplishes the same task but instead uses a while loop. 
            Assign the accumulator variable to the name accum.

list1 = [8,3,4,5,6,7,9]

tot = 0
for elem in list1:
    tot = tot + elem

list1 = [8,3,4,5,6,7,9]
accum = 0
index = 0
while index < len(list1):
    accum = accum + list1[index]
    index += 1
print(accum)

# The Listener Loop : ENCOUNTERED ONLY USING WHILE LOOPS

PRINTING THE SUM OF ANY NUMBER WHICH IS CALLED AND ENDING THE LOOP IF THERE IS NO NUMBER LEFT 

the_sum = 0
x = -1
while x!= 0:
    x = int(input("The next number to add up(enter 0 if no more numbers): "))
    the_sum += x
print("The sum of given numbers is {}.".format(the_sum))

def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            print("Please enter Y for Yes or N for No")
        return answer

response = get_yes_or_no("Do you like water surfing? Y for yes or N for no.")
if response == "Y":
    print("Great! It is an exciting experience.")
else:
    print("Too Bad. You should definitely experience it.")

    

# BREAK AND CONTINUE

x = 0
while x < 20:
    print("We are incrementing x")
    if x%2 == 0:
        x += 3
        continue
    if x%3 ==0:
        x += 5
    x += 1
print("We are done with our loop. X has the value: {}.".format(x))

# INFINITE LOOPS

b = 15
while b < 60:
    b = 5 #resetting the value of b everytine the code is run, so the value of b doesn't change and it stays below 60 making it an infinite loop.
    print("Bugs")
    b = b+7

# Exercise 

Question 1: Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(list):
    lst = []
    i = 0
    while i < len(list):
        if list[i] == 5:
            break
        lst.append(list[i])
        i += 1
    return lst

list = [1,2,3,4,5,6,7,8,9]
sublist(list)

Question 2: Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(list):
    lst = []
    i = 0
    while i < len (list):
        if list[i] == 7:
            break
        lst.append(list[i])
        i += 1
    return lst

list = [1,2,3,4,5,6,7,8,9]
check_nums(list)

Question 3: Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist(list):
    lst = []
    i = 0
    while i < len(list):
        if list[i] == "STOP":
            break
        lst.append(list[i])
        i += 1
    return lst  

list = ("Anger", "Happiness", "Pain", "hdjsh", "fdhnsejfd", "STOP")
sublist(list)

Question 4: Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

def stop_at_z(list):
    lst = []
    idx = 0
    while idx < len(list):
        if list[idx] == "z":
            break
        lst.append(list[idx])
        idx += 1
    return lst

list = ["def", "gh", "lan", "hgj", "gun", "yfs", "z", " yreu"]
stop_at_z(list)

Question 5: Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.


sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
print(sum1)

sum2 = 0
idx = 0
lst = [65,78,21,33]
while idx < len(lst):
    sum2 += lst[idx]
    idx += 1
print(sum2)

Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing

def beginning(list):
    lst = []
    idx = 0
    while idx < len(list):
        if list[idx] == "bye":
            break
        lst.append(list[idx])
        idx += 1
    return lst

list = ["Hi", "Welcome", "to", "our", "home", "Nice", "to", "meet", "you", ".", "bye", "takecare"]
beginning(list)

list = ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']
beginning(list)

