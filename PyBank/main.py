import os
import csv

## Set a path where the budget data is located
csvpath = os.path.join(".", "Resources", "budget_data.csv")


## Read in the data
with open(csvpath) as csvfile:

    ## Reader
    csvreader = csv.reader(csvfile)

    ## Header
    csv_header = next(csvreader)

    ## Net total amount of profit/losses over entire period
    net = 0

    ## Total number of months (number of rows)
    months = 0
    
    changes = []   # List that stores changes in profits/losses
    ## Iterate through all the rows in the file
    
    previous_pl  = 0 # previous profit/loss

    ## CALCULATE 
    ## 1) NET CHANGE IN PROFIT OVER ENTIRE PERIOD
    ## 2) NUMBER OF MONTHS 
    ## 3) MAX INCREASE IN PROFIT
    ## 4) MAX DECREASE IN PROFIT
    # Max increase in profit
    max_increase = 0 
    # Date at which the max increase in profit occurred. Initially set to a random date. 
    max_increase_date = "Jan-1"
    # Max decrease in profit
    max_decrease = 0
    # Date at which the max decrease in profit occurred. Initially set to a random date
    max_decrease_date = "Jan-1"
    for row in csvreader:
        if row[0] == "Jan-10":
            previous_pl = float(row[1])
        ## Add one to the total number of months
        months += 1
        ## print(row[1])
        ## Update net total amount of profit/losses over entire period
        net += float(row[1])
        ## Add change in profit/loss that occurred from last month to this month to list
        ## Update max increase in profit or max decrease in profit
        if row[0] != "Jan-10":
            change = float(row[1]) - previous_pl
            changes.append(change)
            if change > max_increase:
                max_increase = change
                max_increase_date = row[0]
            elif change < max_decrease:
                max_decrease = change
                max_decrease_date = row[0]
            previous_pl = float(row[1])

         

    ### CALCULATE AVERAGE MONTH-TO-MONTH CHANGES IN PROFIT/LOSS 
    sum_of_changes = 0
    for change in changes:
        sum_of_changes += change
    average = round(sum_of_changes/len(changes),2)
    


#### PRINT TO TERMINAL AND WRITE TO FILE
## I used the code from as a model for formatting a string to show 2 decimal places ("Some string %.2f" % variable) 
## from the top answer at https://stackoverflow.com/questions/3221654/specifying-number-of-decimal-places-in-python
## Terminal
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {months}")
print("Total: $%.2f" % net) 
print("Average Change: $%.2f" %average)
print("Greatest Increase in profits: " + max_increase_date + " ($%.2f)" %max_increase)
print(f"Greatest Decrease in profits: " +  max_decrease_date + " ($%.2f)" %max_decrease)
## File
# Specify the file to write to 
output_path = os.path.join(".", "Analysis", "new.csv")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write information
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total months:', f'{months}'])
    csvwriter.writerow(['Total', '$%.2f' % net])
    csvwriter.writerow(['Average Change: ', '$%.2f' %average])
    csvwriter.writerow(['Greatest Increase in profits: ', f'{max_increase_date}', '($%.2f)' %max_increase])
    csvwriter.writerow(['Greatest Decrease in profits: ', f'{max_decrease_date}', '($%.2f)' %max_decrease])