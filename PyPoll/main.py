import os 
import csv
csv_file_path = os.path.join("Resources", "election_data.csv")

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    campaign_votes = [85213, 272892, 11606]  # List of votes for each candidate

# Calculate the total number of votes cast
total_votes = sum(campaign_votes)

# Printing the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes for each candidate
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
for i in range(len(candidates)):
    percentage = (campaign_votes[i] / total_votes) * 100
    print(f"{candidates[i]}: {percentage:.3f}% ({campaign_votes[i]})")

# Determine the winner based on popular vote
winner_index = campaign_votes.index(max(campaign_votes))
winner = candidates[winner_index]

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")