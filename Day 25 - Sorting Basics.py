L1 = [1,7,4,-1,3]
L1.sort()
print(L1)


L2 = ["Apple", "Kiwi", "Blueberry"]
L2.sort()
print(L2)

L3 = sorted(L2)
print(L3)

Optional reverese parameter

L2 = ["Apple", "Kiwi", "Blueberry"]
print(sorted(L2, reverse = True))

# Optional Key Parameter

lst = [1,7,4,-2,3]
def absolute(x):
    if x>=0:
        return x
    else:
        return -x

print(absolute(30))
for y in lst:
    print(absolute(y))

if you also want to sort the absolute values then the belowoptional parameter is used

L2 = sorted(lst, key = absolute)
print(L2)

#or in reverese order
print(sorted(lst, reverse = True, key = absolute))

L2 = sorted(lst, key = lambda x: absolute(x))
print(L2)

# Advanced Sorting

Sorting a dictionary

lst = ["E", "F", "B", "A", "D", "I", "I", "C", "B","A", "D", "D", "E", "D"]
d = {}
for x in lst:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for x in sorted(d, key = lambda k: d[k], reverse = True):
    print("{} appears {} times.".format(x, d[x]))

tups = [("A", 3, 2),
        ("C", 1, 4),
        ("B", 3, 1),
        ("A", 2, 4),
        ("C", 1, 2)]
for tup in sorted(tups):
        print(tup)

fruits = ["peach", "kiwi", "apple",'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key = lambda fruit_name: (len(fruit_name), fruit_name), reverse = True)
for fruit in new_order:
    print(fruit)

When to use a Lambda Expression

# Exercises

Question 1: Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)
print(sorted_letters)

Question 2: Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
print(animals_sorted)

Question 3: The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}



medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)
print(alphabetical)


Question 4: Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def g(k,d):
    return d[k]
ks = medals.keys()
top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]  
print(top_three)

Question 5:We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}


groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def g(k,d):
    return d[k]
ks = groceries.keys()
# print(ks)
most_needed = sorted(ks,key=lambda x : g(x,groceries),reverse = True)  
print(most_needed)


Question 6: Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.

def last_four(idx):
    return (str(idx)[-4:])


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
last_four(ids)
sorted_ids = sorted(ids, key=last_four )
print(sorted_ids)

Question 7: Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
def last_four(x):
    
    return (str(x)[-4:])
last_four(ids)

sorted_id = sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_id)

Question 8: Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']


ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key = lambda x: x[1])
print(lambda_sort)

