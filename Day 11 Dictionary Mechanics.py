dict = {"one": "golf", "two":"baseball", "three": "hockey"}
value = dict["two"]

print(value)

print(dict["one"])

medals = {"Gold" : 7, "Silver": 8, "Bronze": 6}
print(medals["Silver"])

medals["Gold"]

medals["copper"] = 5

medals

medals["steel"] = 6
medals

del medals["steel"]

medals

medals["Silver"] += 20
medals

len(medals)

for key in medals.keys():
    print(key)

for key in medals.keys():
    print(key, "has the value", medals[key])
    

print(list(medals.keys()))

print(list(medals.values()))
print(list(medals.items()))

"apples" in medals

"Gold" in medals

print(medals.get("Steel"))

medals.get("Gold")/medals.get("Silver")

total = 0
medals = {"Gold" : 7, "Silver": 8, "Bronze": 6}
for key in medals:
    if len(key)>4:
        total += medals[key]
        print(total)

awards = medals
print(awards is medals)

awards["Gold"] = 88
print(medals["Gold"])

Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())
print(countries)

Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable belarus.

medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
belarus = medal_count.get("Belarus")
print(belarus)

The dictionary total_golds contains the total number of gold medals that countries have won over the course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name chile_golds.

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds.get("Chile")
print(chile_golds)


Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value.

US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals.get("Fencing")
print(fencing_value)








