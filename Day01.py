import csv
from csv import reader

# Open the CSV file for reading
with open(r"d:\link\to\file\\input-text.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')

    # Initialize a list to store the sums of first and last digits
    sums = []

    for row in reader:
        # Initialize a variable to store the concatenated digits
        concatenated_digits = ""
        for i in row[0]:
            print("Value of i: " + i)
            if i.isdigit():
                concatenated_digits += i
                first_digit = concatenated_digits[0]
                last_digit = concatenated_digits[-1]
        row_num = first_digit + last_digit
        print(row_num)
        sums.append(int(row_num))
# Calculate the total sum of all rows
total_sum = sum(sums)
print("Total sum:", total_sum)
