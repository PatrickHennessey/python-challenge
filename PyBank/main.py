import os
import csv

# Opens the csv file with polling data
py_bank_csv = os.path.join('Resources', 'budget_data.csv')

# In preparation for printing out the results text file.
py_bank_output = os.path.join('PyBank_Results.txt')

## Variable Declarations ##
# Create the necessary empty lists used for calculations.
total_months = []
total_revenue = []
average_change = []

# Open csv file, set the reader and skips the header row as usual
with open(py_bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loops through the rows in the file and add to the lists defined above ...
    for row in csvreader:
        # ... Gives a total based on the number of rows in column 1 ...
        total_months.append(row[0])
        # ... Adds the integer value of each or the rows in colmn 2 together to give a result.
        total_revenue.append(int(row[1]))

    # Loops through the Profits/Losses row to calculate the monthly profit change
    # The "range(len(total_revenue) - 1):" removes the blank entry from the calculation, since we need to find the result between two entries
    for i in range(len(total_revenue) - 1):
        average_change.append(total_revenue[i + 1] - total_revenue[i])

# Grab the biggest profit and loss total
max_increase_change = max(average_change)
max_decrease_change = min(average_change)

# Grab the corresponding months for profit and loss by looking ahead +1 from current posistion
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1

# Print results to a file named "PyBank_Results.txt"
with open(py_bank_output, "w") as file:
    # ".writelines" allows you to print to multiple lines without haveing to do multiple file.writes statements.
    # The "\n" is like a carriage return. You could shorten everything by getting rid of the multple f"" lines,
    # but then you have one long line that is diffficult to read without scrolling    file.writelines(
        file.writelines(f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total Months: {len(total_months)} months\n"
        # ":.2f" formats the results to have two decimal places.
        f"Total Profits: ${sum(total_revenue):.2f}\n"
        f"Average Change: ${round(sum(average_change) / len(average_change), 2)}\n"
        f"Greatest Increase in Profits: {total_months[max_increase_month]} {max_increase_change:.2f}\n"
        f"Greatest Profit Loss: {total_months[max_decrease_month]} ${max_decrease_change:.2f}\n")
    
# Prints the resulting text file to the terminal
with open(py_bank_output, 'r') as reader:
    print(reader.read())
