import os
import csv

# Opens the csv file with polling data
py_poll_csv = os.path.join('Resources', 'election_data.csv')

# In preparation for printing out the results text file.
py_poll_output = os.path.join('PyPoll_restults.txt')

## Variable Declarations ##
# Inits the total vote counter.
total_votes = 0
# creates an empty Dictionary to hold candidate names and their votes.
poll_results = {}
# Create the necessary empty lists used for tracking and calculations.
candidates = []
votes = []
percent_of_votes = []
who_is_winner = []

# Opens the csv file with polling data and skips the header row.
with open(py_poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the rows ...     
    for row in csvreader:
        # ... adding to the total_vote counter ...
        total_votes += 1
        # ... Looks for unique values in the 'Candidate' row,
        # ".keys()" will add a unique name to the dictionary (only once since you 
        # can't have two different keys with the same name) ...
        if row[2] in poll_results.keys():
            # ... and adds to their vote count.
            poll_results[row[2]] = poll_results[row[2]] + 1
        else:
            poll_results[row[2]] = 1

# Takes the information in the Dictionary, puts each set into the declared lists, and makes candidate the key and votes the value
for i, j in poll_results.items():
    candidates.append(i)
    votes.append(j)

# Loops through the above list of votes and get the percentage for each candidate.
for i in votes:
    percent_of_votes.append(round(i / total_votes * 100, 1))

# Zip the lists (candidates, votes, and percent_of_votes together) into a new list
voting_results = list(zip(candidates, votes, percent_of_votes))

# Looks through the voteing_results list to find the candidate with the .max votes and adds their name to the list.
for candidate in voting_results:
    if max(votes) == candidate[1]:
        who_is_winner.append(candidate[0])

# Print results to a file named "PyPol_Results.txt"
with open(py_poll_output, "w") as file:
    # ".writelines" allows you to print to multiple lines without having to do multiple file.write statements.
    # The "\n" is like a carriage return. You could shorten everything by getting rid of the multple f"" lines, 
    # but then you have one long line that is diffficult to read without scrolling
    file.writelines(f"---------------------------\n"
    f"Election Results\n"
    f"---------------------------\n"
    f"Total Votes: {(total_votes)}\n")
    for candidate in voting_results:
        # ":.3f" formats the results to have three decimal places.
        file.writelines(f"{str(candidate[0])}: {int(candidate[2]):.3f}%  ({int(candidate[1])})\n")
    file.writelines(f"------------------------- \n"
                    f"Winner: {str(who_is_winner[0])}\n"
                    f"-------------------------")
        
## Prints results to the terminal 
with open(py_poll_output, 'r') as reader:
    print(reader.read())
