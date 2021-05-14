# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
# Loop does not terminate but continues on with the next iteration.

## Prints all letters except 'e' and 's'
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print("current letter: ", letter)

ls = ["a","e", "i", "o", "u"]
for i in ls:
    if i == "e" or i == "i":
        continue
    print(i)

#Break Statement: It brings control out of the loop.
for letter in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

#range() function
#range() function allows a user to generate a series of numbers within a given range
# Depending upon how many arguments user is passing to the function, user can decide where that series of numebrs will begin and end.

Python Program to
show range() basics

printing a number (horizontally)

for i in range(10):
     print(i, end = "")
print()

#using range for iteration
ls = [10,20,30,40]
for i in range(len(ls)):
    print(ls[i], end= "")
print()

# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
    sum = sum + i
print(sum)

