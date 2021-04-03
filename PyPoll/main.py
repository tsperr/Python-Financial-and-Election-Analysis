#This is for PyPoll!
# First, we import os and csv modules to create file paths and read csv files
import os
import csv 

# import the path to view on all operating systems
PyPollcsvpath=os.path.join('..','Resources','election_data.csv')

# set variables for counting to zero
votes_count=0

# make lists for storing data
canidates=[]
votes=[]
canidate_count=[]
percent=[]

# read through the csv file
with open(PyPollcsvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

# skip the header 
    csv_header=next(csvreader)

# loop through election data csv
    for row in csvreader: 
# count number of votes by counting the number of people who voted        
        votes_count=votes_count+1
# calculate a complete list of candidates who received votes
        if row[2] not in canidates:
            canidates.append(row[2])
        votes.append(row[2])

# find percentage of votes each canidate got
    for person in canidates:
        canidate_count.append(votes.count(person))
        percent.append(round(votes.count(person)/votes_count*100,3))

# find the winner of who got the most votes
winner=canidates[canidate_count.index(max(canidate_count))]



print("--------------------------------------------")
print("Election Results")
print("--------------------------------------------")
print("Total Votes:" + str(votes_count))
print("--------------------------------------------")
for i in range(len(canidates)):
    print(f'{canidates[i]}: {percent[i]}% {canidate_count[i]}')
print("--------------------------------------------")
print(f'winner:{winner}')
print("---------------------------------------------")

with open('canidate_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------\n") 
    text.write("Election Results" + "\n")
    text.write("----------------------------------------------------\n")
    text.write("Total Votes:" + str(votes_count) + "\n")
    text.write("----------------------------------------------------\n")
    for i in range(len(canidates)):
        text.write(f'{canidates[i]}: {percent[i]}% {canidates_count[i]}\n')
    text.write("---------------------------------------------------------\n")
    text.write(f'winner:{winner}')
    text.write("--------------------------------------------------------\n")
    
