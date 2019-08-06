import os
import csv

# input path
py_bank_csv = os.path.join('Resources', 'budget_data.csv')

# output path
py_bank_output = os.path.join('PyBank_Results.txt')

# Create the necessary lists and variables for the calculations.
total_months = []
total_revenue = []
average_change = []

# Open csv file, set the reader and skip the header row as usual
with open(py_bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # loops through the rows in the file and add to the lists defined above
    for row in csvreader:
        # Gives a total based on the number of rows in column 1
        total_months.append(row[0])
        # Adds the integer value of each or the rows in colmn 2 together to give a result
        total_revenue.append(int(row[1]))

    # loops through the Profits/Losses row to calculate the monthly profit change
    # the -1 removes the blank entry from the calculation, since we need to find the result between two entries
    for i in range(len(total_revenue) - 1):
        average_change.append(total_revenue[i + 1] - total_revenue[i])

# Grab the biggest profit and loss total
max_increase_change = max(average_change)
max_decrease_chane = min(average_change)

# Grab the corresponding months for profit and loss by looking ahead +1 from current posistion
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1

# Print totals to the terminal using the \n command to forgoe using multiple "print()" statements
print(
    f"Financial Analysis \n"
    f"------------------------- \n"
    f"Total Months: {len(total_months)} months \n"
    f"Total Profits: ${sum(total_revenue)} \n"
    f"Average Change: ${round(sum(average_change) / len(average_change), 2)} \n"
    f"Greatest Increase in Profits: {total_months[max_increase_month]} ${max_increase_change} \n"
    f"Greatest Decrease in Profits: {total_months[max_decrease_month]} ${max_decrease_chane} \n"
)

# Print results to a file named "PyBank_Results.txt"
with open(py_bank_output, "w") as file:
    file.write("Financial Analysis")
    file.write(f"\n")
    file.write(f"-------------------------")
    file.write(f"\n")
    file.write(f"Total Months: {len(total_months)} months")
    file.write(f"\n")
    file.write(f"Total Profits: ${sum(total_revenue)}")
    file.write(f"\n")
    file.write(f"Average Change: ${round(sum(average_change) / len(average_change), 2)}")
    file.write(f"\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} ${max_increase_change}")
    file.write(f"\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} ${max_decrease_chane}")
