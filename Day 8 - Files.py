file = open("C:/Users/vgupt/Downloads/The Card Free Website Template - Free-CSS.com/2109_the_card/ABOUT THIS TEMPLATE.txt", "w")
# contents = file.readlines()
# for line in contents:
#     print(line.strip())
for number in range(13):
    square = number*number
    file.write(str(square))
    file.write("\n")
