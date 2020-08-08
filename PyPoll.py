# To Do for Election Analysis: 

#Total number of votes cast
#A complete list of candidates who received votes 
#Total number of votes each candidate received 
#Percentage of votes each candidate won 
#The winner of the election based on a popular vote 

#Add our dependencies
import csv
import os

# Assign a filename variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0 

# Declare a new list for candidate options
candidate_options = []

#Declare a dictionary to count total votes per candidate
candidate_votes = {}

#Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file. 
    for row in file_reader:

        #2. Add the total vote count. 
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:

            #Add it to the list of candidates. 
            candidate_options.append(candidate_name)

            #Track that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count. * note this is outside the if statement, but in the for loop
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts. 

        #Iterate through the candidate list. 
        for candidate_name in candidate_votes:
        
            #Retreive vote count of candidate. 
            votes = candidate_votes[candidate_name]

            #Calculate the percentate of votes.
            vote_percentage = float(votes) / float(total_votes) *100

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
            candidate_results = (
                    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
             #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

        #Determine winning vote count and candidate.
        #Determine if the votes is greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # if true then set winning_count = votes and winning_percet = vote_percentage. 
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name. 
            winning_candidate = candidate_name

    #Print winning candidate summary to terminal. 
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)   