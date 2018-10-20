#Assignment : Unit 3 | Assignment - Py Me Up, Charlie
# Krishna Keshav                                Date : 10/19/2018
#---------------------------------------------------------------------
## PyBank
######################################################################

# Import os module that has functions to interact with the file system
import os
# Import module for reading CSV files
import csv

#Get current working directory
cwkdir = os.getcwd()
#Append file directory and make a complete file path
filepath = os.path.join( cwkdir,'Resources','budget_data.csv')

#Initialize variables
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0

#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         #Placeholder to track greatest increase in profits (financial analysis)
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #Placeholder to track greatest decrease in profits (financial analysis)
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total months (financial analysis)
         mcount = mcount + 1
         total += int(Amount) 

## Display Results ##      
#The total number of months included in the dataset
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')