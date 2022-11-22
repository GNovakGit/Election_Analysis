counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {}
counties_dict["Arapaho"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

my_tuple = ( )
counties_tuple = ("Arapahoe","Denver","Jefferson")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
'append insert and remove methods'

# F STRING LITERALS EDIT  #Print Function (integer value converted to a string)
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
#create membership operation by determining if el paso is in counties list
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
#COMBINE MEMBERSHP AND LOGICAL OPERATIONS TO TEST CONDITIONS
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
# Check if Arapahoe and El paso is in the counties list

# variable (i or any variable) to search in range of length of counties list
for i in range(len(counties)):
    print(counties[i])

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

#Get the key value pairs of a dictionary
for key, value in counties_dict.items():
    print(key, value)
#now use voters and counties instaed of value and key
for county, voters in counties_dict.items():
    print(county, voters)
#Show the data in a meaningful way
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# Nested For Loop. retrieve each dictionary and second loop to reference data to get each value
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Retrieve ONLY the number of registered voters from each dictionary ..the "VALUE"
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# or print just the keys..
for county_dict in voting_data:
    print(county_dict['county'])

# COUNTIES Dictionary method 
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# MULTILINE F STRINGS
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#FORMAT FLOATING-POINT DECIMALS
f'{value:{width},.{.2}}'

print(message_to_candidate)



















