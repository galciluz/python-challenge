# First we'll import the os module
import os
# Module for reading CSV files
import csv
# import stadistics functions
import statistics

csvpath = os.path.join('Resources', 'election_data.csv')

#Function count votes per candidate
def vote_per_candidate(candidate_name):
    # reading the csv file and saving values to calculate results
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        # Read the header row first
        csv_header = next(csvreader)
        #initial Variables
        num_vote=0 
        # Read each row of data after the header
        for row in csvreader:
            if str(row[2])==candidate_name:
                num_vote=num_vote+1

    return num_vote

# reading the csv file and saving values to calculate results
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    #initial Variables
    total_vote=1
    num_candidate=0
    candidate_data={"Candidate": [],
                    "Votes": []
                    }
    csv_initial=next(csvreader)
    name=str(csv_initial[2])
    candidate_data["Candidate"]= [name]

    # Read each row of data after the header
    for row in csvreader:
        total_vote = total_vote + 1
        found = False
        i=0
        x= len(candidate_data["Candidate"])
        for i in range(x):
            if str(row[2]) == str(candidate_data["Candidate"][i]): 
                found = True

        if found==False :
            candidate_data["Candidate"].append(str(row[2]))
            num_candidate=num_candidate+1
           
print(total_vote)
i=0
for i in range(len(candidate_data["Candidate"])):
    candidate_name = str(candidate_data["Candidate"][i])
    vote=vote_per_candidate(candidate_name)
    candidate_data["Votes"].append(vote)

print(candidate_data)

