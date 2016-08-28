import csv
import numpy
import glob

inits = {}
adds = {}

for filename in glob.glob("*.txt"):
    print(filename)
    with open(filename, 'rb') as result_file:
        spamreader = csv.reader(result_file, delimiter=',')

        for row in spamreader:
            if row[1] == 'ini':
                inits[row[3]] = row[2]
            elif row[1] == 'add':
                adds[row[3]]

print(inits)


        # with open('rcvs.csv', 'rb') as rcvs:
        #     spamreader = csv.reader(rcvs, delimiter=',')
