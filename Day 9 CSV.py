olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna", 30, "Sailing"),
             ("Win", 29, "Art Competetions"),
             ("Wakakao", 54, "Cycling")]

#output the header row
header_row = "Name, Age, Sport"
print(header_row)
#output each of the rows
for olympian in olympians:
    row_string = "{},{},{}".format(olympian[0], olympian[1], olympian[2])
    print(row_string)



olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna", 30, "Sailing"),
             ("Win", 29, "Art Competetions"),
             ("Wakakao", 54, "Cycling")]
outfile = open("olympians.csv", "w")
#output the header row
outfile.write("Name, Age, Sport")
outfile.write("\n")
#output each of the rows
for olympian in olympians:
    row_string = "{},{},{}".format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write("\n")
outfile.close()


# geeks for geeks code to write a csv file
import csv
# field names
fields = ["Name", "Branch", "Year", "GPA"]

# data rows of csv file
rows = [["Nikhil","COE", "2", "9.0"],
         ["Sanchit", "COE", "2", "9.1"],
         ["Aditya", "IT", "1", "7.8"]]

# name of csv file
filename= "university_records.csv"

# writing to a csv file
with open(filename, "w") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
