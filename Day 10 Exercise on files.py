# 1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

file = open("travel_plans.txt", "r")

num = 0
for i in file:
    num = num + len(i)
    file.write(str(num))
    file.write("\n")

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.

file = open("emotion_words.txt", "r")
num_words = 0
for i in file:
    num_words = num_words + len(i.split())
    file.write(str(num_words))

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
file = open("school_prompt.txt" , "r")
num_lines = 0
num_lines = sum(1 for line in file)

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
file = open("school_prompt.txt" , "r")
beginning_chars = file.read(30)
print(beginning_chars)

# Using the file school_prompt.txt, assign the third word of every line to a list called three.
file = open("school_prompt.txt" , "r")
three = []

three = [line.split()[2] for line in file]
print(three)

# Create a list called emotions that contains the first word of every line in emotion_words.txt.
file = open("emotion_words.txt", "r")
emotions = []
emotions = [line.split()[0] for line in file]
print(emotions)

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
file = open("travel_plans.txt", "r")
first_chars = file.read(33)
print(first_chars)

#Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
file = open("school_prompt.txt", "r")
words = file.read().split()
p_words = [word for word in words if 'p' in word]
