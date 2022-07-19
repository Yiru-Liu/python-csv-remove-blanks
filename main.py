import csv

with open('test dummy.csv', newline='') as r, open('removed.csv', 'w', newline='') as w:
    reader = csv.reader(r)
    for row in reader:
        print(row)
        if all('' == s or s.isspace() for s in row):
            print('true')
        else:
            print('false')
    w.close()