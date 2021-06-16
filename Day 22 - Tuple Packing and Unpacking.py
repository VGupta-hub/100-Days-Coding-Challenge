# Tuple Packing and Unpacking

julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta", "Georgia"
print(julia[4])

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta", "Georgia")
print(julia[4])

Both give same responses.

# Tuples as Return Values

Tuples Assignment with Packing

def circleinfo(r):
    """Return circumference and area of a circle of radius r"""
    c = 2*3.1459*r
    a = 3.1459*r*r
    return c,a
circleinfo(10)

Tuples Assignment with Unpacking

julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia

def add(x,y):
    return x+y

add(5,4)

z = (1,7)
add(*z)

* is used to tell python to treat z as (x,y) in the add function else it wil give an typeerror of arguments.

# Exercise

Question 1: Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.

olympics = "Beijing" , "London" ,"Rio" , "Tokyo"
print(olympics)

Question 2: The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country.

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for i in tuples_lst:
    country.append(i[1])
print(country)


Question 3: With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.

olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp

Question 4: Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.

def info(name, gender, age, bday_month, hometown):
    f = name, gender, age, bday_month, hometown
    return f

info("Joel", "Male", 27, "March" , "Alberta")

Question 5: Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method.


gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

lst = gold.items()

num_medals = []
for i in lst:
    num_medals.append(i[1])
print(num_medals)

