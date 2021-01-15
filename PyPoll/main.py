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
                    "Votes": [],
                    "Perc Votes": []
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
           
#calculate num of votes per candidate and % of votes           
i=0
for i in range(len(candidate_data["Candidate"])):
    candidate_name = str(candidate_data["Candidate"][i])
    vote=vote_per_candidate(candidate_name)
    candidate_data["Votes"].append(vote)
    perc_vote = format(((vote/total_vote)*100), "0.2f")
    candidate_data["Perc Votes"].append(perc_vote)

#create a file .txt and saved all the Election Result
i=0
filepath = os.path.join("output","election_result.txt")
_, filename = os.path.split(filepath)
file = open(filepath, "w")
file.write("------------------------------------" + "\n")
file.write("             Election Result             " + "\n")
file.write("____________________________________" + "\n")
file.write ("      Total Votes: " + str(total_vote) +  "\n")
file.write("____________________________________" + "\n")
for i in range(len(candidate_data["Candidate"])):
    file.write(str(i+1) + ".-" + str(candidate_data["Candidate"][i]) +": %"+  str(candidate_data["Perc Votes"][i]) + " ("+ str(candidate_data["Votes"][i])+")"  + "\n")

file.write("____________________________________" + "\n")
#Return the index of the Candidate with max vote in order to select and print the winner
max=candidate_data["Votes"].index(max(candidate_data["Votes"]))
file.write("         Winner: " + str((candidate_data["Candidate"][max])) + "\n")
file.write("------------------------------------"+ "\n")
file.close()

#Print using the file .txt created
file = open(filepath, "r")
print(file.read())
file.close
