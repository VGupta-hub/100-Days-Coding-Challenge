# Leetcode Question

Question: Given the string, s, sort the string by numbered word and the resulting output should be "This is a sentence"

s = "is2 sentence4 This1 a3"
new_s = s.split()
print(new_s)
updated_list = sorted(new_s, key = lambda x: int(x[-1]))

print(updated_list)
#remove last character 
lst = [sub[ : -1] for sub in updated_list]
print(lst)
str = ""
for i in lst:
    str = str + i

print(str) 

