import csv
import os

# Set file path
file_path = os.path.join("Resources", "election_data.csv")

# Open CSV
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skipping the header

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skip the header row

    # Iterate through the rows
    for row in csvreader:
        # Update total votes
        total_votes += 1

        # Update candidate votes
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        # Update winner information
        if candidates[candidate_name] > winner_votes:
            winner = candidate_name
            winner_votes = candidates[candidate_name]

# Calculate percentages, determine the winner, and print/write results
with open("election_results.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Update winner information within the loop
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------")

    # Print Results to Terminal
    print("Election Results\n")
    print("-------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})\n")
    print("-------------------------\n")
    print(f"Winner: {winner}\n")
    print("-------------------------")
    