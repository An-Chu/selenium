import csv

with open('account.csv', 'w') as file:
    fieldName = ['user', 'password']
    writer = csv.DictWriter(file, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({'user':'2051052006','password':'PhuocAn1234'})

with open('account.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)