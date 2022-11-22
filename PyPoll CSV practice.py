# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
#Open the data file and path to .csv
import csv
import os

# Assign a variable for the file to load and the path using Chaining
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

 # Write three counties to the file with header
    txt_file.write("Counties in the Election\n")
    txt_file.write("----------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# To do: read and analyze the data here
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election

