<<<<<<< HEAD
# This is for PyBank!
=======
#This is for PyPoll!
>>>>>>> 8bbb98889eebb17cd98996dca9d1c7987c17ac47
# First, we import os and csv modules to create file paths and read csv files
import os
import csv 

# import the path to view on all operating systems
<<<<<<< HEAD
PyBankcsvpath=os.path.join('Resources','PyBank.csv')

#set variables to zero
count_of_months=0
total_profit=0
initial_profit=0
total_change=0
max_change=0
max_change_month=0
decrease_month=0
decrease_value=0

#make lists
months=[]
monthly_change=[]

# read through the csv file
with open(PyBankcsvpath) as csvfile:
=======
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
>>>>>>> 8bbb98889eebb17cd98996dca9d1c7987c17ac47
    csvreader=csv.reader(csvfile, delimiter=',')

# skip the header 
    csv_header=next(csvreader)

<<<<<<< HEAD
# read through the rest of the rows
    for row in csvreader: 

        # loop through and count the months
        count_of_months= count_of_months + 1

        # loop through and add up the total amount of profit/losses
        total_profit=total_profit + int(row[1])

        # find changes in profit/losses 
        final_profit=int(row[1])
        monthly_change_profits=final_profit - initial_profit
        if (monthly_change_profits>max_change) and monthly_change_profits>0:
            max_change=monthly_change_profits
            max_change_month=row[0]
        elif (monthly_change_profits<max_change) and monthly_change_profits<0:
            decrease_value=monthly_change_profits
            decrease_month=row[0] 

        # store the number  
        monthly_change.append(monthly_change_profits)
        # compile this number through the data
        total_change=total_change + monthly_change_profits
        # reset the initial profit to be compiled
        final_profit=initial_profit 

# calculate the average change in profits
average_change_profits=int(total_change/count_of_months)

# # calculate the greatest increase in profits (date and amount) over the entire period


print("-------------------------------------------------------------")
print("Financial Analysis")
print("-------------------------------------------------------------")
print("Total Months:" + str(count_of_months))
print("Total:" + "$" + str(total_profit))
print("Average Change:" + "$" + str(average_change_profits))
print("Greatest Increase In Profits:" + str(max_change_month) + "($" + str(max_change) + ")")
print("Greatest Decrease In Profits:" + str(decrease_month) + "($" + str(decrease_value) + ")")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------\n") 
    text.write("Fianancial Analysis" + "\n")
    text.write("----------------------------------------------------\n")
    text.write("Total Months:" + str(months) + "\n")
    text.write("Total:" + "$" + str(total_profit) + "\n")
    text.write("Average Change:" + "$" + str(monthly_change) + "\n")
    text.write("Greatest Increase In Profits" + str(max_change_month) + "($" + str(max_change) + ")" + "\n")
    text.write("Greatest Decrease In Profits" + str(decrease_month) + "($" + str(decrease_value) + ")" + "\n")
=======
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
    
>>>>>>> 8bbb98889eebb17cd98996dca9d1c7987c17ac47
