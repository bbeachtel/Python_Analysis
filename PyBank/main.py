import csv
import os

# Set file path
file_path = os.path.join("Resources", "budget_data.csv")

# Initialize Variables
total_months = 0
net_sum = 0
changes = []
dates = []
previous_sum = 0

# Open CSV and read it
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skipping the header

    # Iterate through rows
    for row in csvreader:
        # Count months and net sum
        total_months += 1
        net_sum += int(row[1])

        # Check if total_months is greater than 1
        if total_months > 1:
            changes.append(int(row[1]) - previous_sum)
            dates.append(row[0])

        previous_sum = int(row[1])

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_sum}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
with open("financial_analysis.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_sum}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
