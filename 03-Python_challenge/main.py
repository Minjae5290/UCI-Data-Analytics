import os
import csv

budget_data = os.path.join("..","03-Python_challenge","budget_data.csv")

with open(budget_data, newline="") as csvfile:	

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
	    