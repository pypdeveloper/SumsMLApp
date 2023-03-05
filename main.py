import csv
import random

# Define the range of numbers for Number 1 and Number 2
min_num = -10000
max_num = 10000

# Open a new CSV file
with open('random_numbers.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Number 1', 'Number 2', 'Sum']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header row to the CSV file
    writer.writeheader()

    # Write 10000 random rows to the CSV file
    for i in range(10000):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        sum_num = num1 + num2
        writer.writerow({'Number 1': num1, 'Number 2': num2, 'Sum': sum_num})

