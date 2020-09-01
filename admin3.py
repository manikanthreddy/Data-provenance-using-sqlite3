import csv

with open('log1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("Following are the user_type,change_ID & Customer_ID of the changes due to wrong data entry")
    for row in csv_reader:
        if (row[2] == '1'):
            print(row[1],row[2],row[3])
            line_count += 1
    print(f'Processed {line_count} changes.')