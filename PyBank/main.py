import os

import csv

# Sets path to csv file
pathtofile = os.path.join('Resources', 'budget_data.csv')

# opens budget data and stores it in 'csvfile'
with open(pathtofile) as csvfile:

    # budget_data values to be read as dictionary and stored in reader
    reader = csv.DictReader(csvfile, delimiter=',')
    
    # Set variables 
    totalMonths = 0
    total = 0
    previousMonth = 0
    monthlyChange = 0
    listOfChanges =[]  
    monthOfChange = []

    # loop through reader 
    for row in reader:
        
        # Adds up the number of months 
        totalMonths += 1

        #Calculates the net total amount of 'Profit/Losses'
        total += int(row['Profit/Losses'])

        # calculates change between months
        monthlyChange = float(row['Profit/Losses']) - previousMonth

        # sets value of previous month
        previousMonth = float(row['Profit/Losses'])

        #  places changes in list
        listOfChanges += [monthlyChange]

        # places months in a list
        monthOfChange += [row['Date']]

#  creates a dictionary combining the month of change with the profit change
changeByMonth = dict(zip(monthOfChange,listOfChanges))

# grabs the associated maximum profit increase 'month' key from dictionary 
maxIncreaseMonth = max(changeByMonth, key = changeByMonth.get)

# set variable to greatest profit increase value instead of month key
maxIncreaseValue = max(changeByMonth, key = (lambda changetoValue: changeByMonth[changetoValue]))

# grabs the associated minimum profit increase 'month' key from dictionary
minIncreaseMonth = min(changeByMonth, key = changeByMonth.get)

# set variable to greatest profit decrease value instead of month key
minIncreaseValue = min(changeByMonth, key = (lambda changetoValue: changeByMonth[changetoValue]))

# removes first value from profit change list
del listOfChanges[0]

# Calculate average change
totalAverage = round((sum(listOfChanges)/len(listOfChanges)),2)

# displays total months
print(f"Total Months: {totalMonths}")

# displays total amount for profit/losses
print(f"Total: $ {total}")

# displays the average change 
print(f'Average Change $ {totalAverage}')

# displays the Greatest profit increase
print(f'Greatest Increase in Profits: {maxIncreaseMonth} $ {int(changeByMonth[maxIncreaseValue])}')

# displays the greatest profit decrease
print(f'Greatest Decrease in Profits: {minIncreaseMonth} $ {int(changeByMonth[minIncreaseValue])}')

# Write text file 
with open ('FinancialAnalysis.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write(f"Total Months: {totalMonths}\n")
    f.write(f"Total: $ {total}\n")
    f.write(f'Average Change $ {totalAverage}\n')
    f.write(f'Greatest Increase in Profits: {maxIncreaseMonth} $ {int(changeByMonth[maxIncreaseValue])}\n')
    f.write(f'Greatest Decrease in Profits: {minIncreaseMonth} $ {int(changeByMonth[minIncreaseValue])}\n')

