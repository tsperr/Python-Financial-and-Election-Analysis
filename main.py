# This is for PyBank!
# First, we import os and csv modules to create file paths and read csv files
import os
import csv 

# import the path to view on all operating systems
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
    csvreader=csv.reader(csvfile, delimiter=',')

# skip the header 
    csv_header=next(csvreader)

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
