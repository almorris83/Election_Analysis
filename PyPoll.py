#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        print(row)
        
    
    
#Using the open() function with the "w" mode we will write data to the file.
    open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")
    #Write three counties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")


# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote