import os
import csv

budget_data = os.path.join("..","03-Python_challenge", "budget_data.csv")


with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

total_months = 0
month_change = []
amount_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
total_amount = 0

    header = next(csvreader)
    first_row = next(csvreader)
    total_months = total_months + 1
    total_amount = total_amount + int(first_row[1])
    prv_amount = int(first_row[1])

    for row in csvreader:

        total_months = total_months + 1
        total_amount = total_amount + int(row[1])

        amount_change = int(row[1]) - prv_amount
        prv_amount = int(row[1])
        amount_change_list = amount_change_list + [amount_change]
        month_change = month_change + [row[0]]
        
        if amount_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = amount_change

        if amount_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = amount_change

amount_avg = sum(amount_change_list) / len(amount_change_list)

output = (f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average  Change: ${amount_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

file_to_output = os.path.join("output", "budget_data_analysis.txt")

print(output)

with open(file_to_output, "w") as xlsx_file:
    xlss_file.write(output)





--------------------------------------------------------------------------


# Incorporated the csv module
import os
import csv

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)