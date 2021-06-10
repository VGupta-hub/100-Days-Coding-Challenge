txt = "Alpha Gamma Rho Theta Beta aat ttaat huuasdsud aashhds haha kalam pat"
a_count = 0
h_count = 0
for i in txt:
    if i == "a":
        a_count += 1
    elif i == "h":
        h_count += 1
print("The letter 'a' arrives", a_count, "times.")
print("The letter 'h' arrives", h_count, "times.")

Doing the above with dictionary would avoid assigning a_count, h_count again and again.

%%time
txt = "Alpha Gamma Rho Theta Beta aat ttaat huuasdsud aashhds haha kalam pat"
x = {}
x["a"] = 0
x["h"] = 0
for i in txt:
    if i == "a":
        x[i] += 1
    elif i == "h":
        x[i] += 1
print("The letter 'a' arrives", x["a"], "times.")
print("The letter 'h' arrives", x["h"], "times.")

We can also do this by assigning i in if condition so that we can print any number we want without manually writing an accumulator variable for it.

%%time
txt = "Alpha Gamma Rho Theta Beta aat ttaat huuasdsud aashhds haha kalam pat"
x = {}
for i in txt:
    if i not in x:
        x[i] = 0
    x[i] += 1
print("The letter 'a' arrives", x["a"], "times.")
print("The letter 'h' arrives", x["h"], "times.")
print("The letter 't' arrives", x["t"], "times.")

Question : Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and  the number of times it occurrs. Save this dictionary to the variable name word_counts.

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
lst = sentence.split(" ")
print(lst)
word_counts = {}
for word in lst:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
print(word_counts)

Question : Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.

stri = "what can I do"
char_d = {}
for i in stri:
    if i not in char_d:
        char_d[i] = 0
    char_d[i] += 1
print(char_d)

# Accumulating Results from a Dictionary

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
lst = sentence.split(" ")
print(lst)
word_counts = {}
for word in lst:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
print(word_counts)

for y in word_counts:
    print("There is", word_counts[y], y)

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
lst = sentence.split(" ")
print(lst)
word_counts = {}
for word in lst:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1
print(word_counts)
print(word_counts["the"] > word_counts["rabbit"])

stri = "what can I do"
char_d = {}
for i in stri:
    if i not in char_d:
        char_d[i] = 0
    char_d[i] += 1
print(char_d)
letter_values = {"a":1,"b":2,"c":3,"d":4,"e":7,"f":8,"y":10,"z":21}
scrabble_score = 0
for y in char_d:
    if y in letter_values:
        scrabble_score = scrabble_score + letter_values[y] * char_d[y]
print(scrabble_score)
        

Question: The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total.

travel = {"North America":2, "Europe": 8, "South America": 3, "Asia": 4, "Africa": 1, "Antartica": 0, "Australia": 1}

total = 0
for i in travel:
    total = total + travel[i]
print(total)

Question: schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits.

schedule = {"UARTS 150": 2, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 96": 14}
total_credits = 0
for course in schedule:
    total_credits = total_credits + schedule[course]
print(total_credits)

Question: Create a dictionary called d that keeps the track of all the characters in the string placement and notes how many times each character was seen. Then find the key with the lowest value in this dictionary and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw bbridge is near. Most people visit Mackinaw later in the season."
d = {}
for i in placement:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)

#finding the key with the lowest value
keys = list(d.keys())
#print(keys)
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)      

Question: Create a dictionary called lett_d that keeps track of all the characters in the string product and notes how many times each character was seen. Then find the key with the highest value in this dictionary and assign that key to max value.

product = "iphone and android phones"
lett_d = {}
for letter in product:
    if letter not in lett_d:
        lett_d[letter] = 0
    lett_d[letter] += 1
print(lett_d)

#finding the key with the highest value
keys = list(lett_d.keys())
max_value = keys[0]

for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
print(max_value)

# Exercise

Q1: The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits.

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for i in Junior:
    credits = credits + Junior[i]
print(credits)

Q2: Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for i in str1:
    if i not in freq:
        freq[i] = 0
    freq[i] += 1
print(freq)

Q3: Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"
counts = {}
for i in s1:
    if i not in counts:
        counts[i] = 0
    counts[i] += 1
print(counts)

Q4: Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
words = str1.split(" ")
freq_words = {}
for i in words:
    if i not in freq_words:
        freq_words[i] = 0
    freq_words[i] += 1
print(freq_words)

Q5: Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
words = sent.split(" ")
wrd_d = {}
for i in words:
    if i not in wrd_d:
        wrd_d[i] = 0
    wrd_d[i] += 1
print(wrd_d)

Q6: Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i] += 1
print(characters)

#finding the key with the highest value
keys = list(characters.keys())
best_char = keys[0]
for y in keys:
    if characters[y] > characters[best_char]:
        best_char = y
print(best_char)

Q7: Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for i in sally:
    if i not in characters:
        characters[i] = 0
    characters[i] += 1
print(characters)

#finding the least frequent letter

keys = list(characters.keys())
worst_char = keys[0]

for y in keys:
    if characters[y] < characters[worst_char]:
        worst_char = y
print(worst_char)

Q8: Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string2 = string1.lower()
print(string2)
letter_counts = {}
for i in string2:
    if i not in letter_counts:
        letter_counts[i] = 0
    letter_counts[i] += 1
print(letter_counts)

Q9: Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
new_p = p.lower()
low_d = {}
for i in new_p:
    if i not in low_d:
        low_d[i] = 0
    low_d[i] += 1
print(low_d)

