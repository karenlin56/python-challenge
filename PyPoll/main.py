import os
import csv

## Path to budget data csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")

### Read in the data ###
with open(csvpath) as csvfile:

    ## Reader
    csvreader = csv.reader(csvfile)


    ###### VARIABLES  ######
    ## Number of voters
    voters = 0
    ## Dictionary of candidates and number of votes each person got
    candidates_votes = {}
    ## List to store candidates in the order that they appear in csv file
    candidates_chosen = []
    
    

    ###############  GET TOTAL NUMBER OF VOTERS AND VOTES (CANDIDATES) IN THE ORDER THEY APPEAR IN THE FILE ##################
    for row in csvreader:
        ## Each row represents a voter/vote
        voters += 1 
        ## Grab the candidate this voter voted for
        if row[2] != "Candidate": ## Don't want to grab the column name 'Candidate
            candidate = row[2]
            candidates_chosen.append(candidate) ## Add this candidate the voter voted for to list



        
    #################  COUNT NUMBER OF VOTES EACH CANDIDATE GOT  ########################
    ## (Go through list of candidates in order that they appear in csv file (there are many repeats) and transform 
    ## that information into number of votes each candidate go)
    candidates_chosen.sort() ## All the instances for each candidate are grouped together
    candidate = candidates_chosen[0] ## The candidate we will count the votes for first is the first candidate that appears in list
    count = 0 ## Count of votes for each candidate
    for i in range(1, len(candidates_chosen)): 
        count += 1
        ## If candidate at previous line doesn't equal candidate at this line
        ## or we have reached the end of the list add total number of votes for this candidate to dictionary(with candidate names as keys
        ##                                                                                                   and number of votes as values)
        if candidate != candidates_chosen[i] or i == (len(candidates_chosen)-1): 
            if i == (len(candidates_chosen)-1): ## if at end of the list, we still need to increment count, unlike other cases
                count += 1
            candidates_votes[candidate] = count ## Put candidate name and number of counts for this candidate into dictionary
            count = 0  ## Reset count for next candidate
        candidate = candidates_chosen[i] ## Set candidate variable to candidate this voter voted for
        
     





    #################   WHICH CANDIDATE GOT THE MOST VOTES   #####################
    max_votes = 0 ## Initially set maximum number of votes received to 0
    for key in candidates_votes.keys(): ## Iterate through keys in dictionary
        # Find the candidate with the most number of votes
        if int(candidates_votes[key]) > max_votes: 
            winner = key
            max_votes = int(candidates_votes[key])
        
        






######## OUTPUT INFORMATION TO TERMINAL AND FILE
### Terminal
print("Election Results")
print("------------------------------------------")
print(f"Total votes: {voters}")
for key in candidates_votes.keys():
    percentage =    round(candidates_votes[key]/voters*100, 3)
    print(f"{key}: {percentage}%({candidates_votes[key]})")
print(f"Winner: {winner}")
###File
# Specify the file to write to
output_path = os.path.join(".", "Analysis", "new.csv")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write information
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total votes', f'{voters}'])
    for key in candidates_votes.keys():
        percentage =    round(candidates_votes[key]/voters*100, 3)
        csvwriter.writerow([f'{key}:', f'{percentage}%', f'{candidates_votes[key]}'])
    csvwriter.writerow(["Winner:", f'{winner}'])
  