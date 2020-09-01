import csv

with open('log1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("Following are the change_ID & Customer_ID of the changes done by the Admin")
    for row in csv_reader:
        if (row[1] == 'A'):
            print(row[2],row[3])
            line_count += 1
    print(f'Processed {line_count} changes.')