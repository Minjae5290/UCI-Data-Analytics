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

budget_data_analysis = os.path.join("output", "budget_data_analysis.xlsx")

print(output)

with open(file_to_output, "w") as xlsx_file:
    xlss_file.write(output)





--------------------------------------------------------------------------

import os
import csv

election_data = os.path.join("..","03-Python_challenge", "election_data.csv")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for row in csvreader:

        print(". ", end=""),

        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:

    election_results = (f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        xlsx_file.write(voter_output)

    winner_summary = (f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winner_summary)

    file_to_output = os.path.join("analysis", "election_analysis.xlsx")
    xlsx_file.write(winner_summary)
