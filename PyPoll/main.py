import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0 
candidate_list = []
candidate_dict = {}

winning_vote = 0 
winner = ""

with open(csvpath, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            # start counting total votes    
                   
            # get the reference to the candidate name from the row 
           
            # begin the if statement 
           
            # add the candidate to the list_candidate 

    
    # print the total votes 
    
    
    # loop through the candidates and calculate their percentage of the votes 
  

    # print to terminal and the txt file       
    print(f"--------------------")
    print(f"Winner: {winner}")
    print(f"--------------------")
    datafile.write(f"--------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write(f"--------------------")
