import csv
import numpy
import glob

inits = {}
adds = {}
ext = {}
rmv = {}

add_time = []
remove_time = []

for filename in glob.glob("*.txt"):
    with open(filename, 'rb') as result_file:
        spamreader = csv.reader(result_file, delimiter=',')

        for row in spamreader:
            if row[1] == 'ini':
                inits[row[3]] = row[2]
            elif row[1] == 'add':
                values = adds.get(row[3], [])
                values.append(row[2])
                adds[row[3]] = values
            elif row[1] == 'ext':
                ext[row[3]] = row[2]
            elif row[1] == 'rmv':
                values = rmv.get(row[3], [])
                values.append(row[2])
                rmv[row[3]] = values

for key, value in inits.iteritems():
    v = adds.get(key)
    if v is None:
        continue
    for val in v:
        computed = abs(long(value) - long(val))
        if 0 < computed < 20000:
            add_time.append(computed)

for key, value in ext.iteritems():
    v = rmv.get(key)
    if v is None:
        continue
    for val in v:
        computed = abs(long(value) - long(val))
        if 0 < computed < 20000:
            remove_time.append(computed)

add_time = sorted(add_time)
remove_time = sorted(remove_time)

print(add_time)
print(remove_time)
