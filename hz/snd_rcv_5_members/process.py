import csv
import numpy

with open('rcvs.csv', 'rb') as rcvs:
    spamreader = csv.reader(rcvs, delimiter=',')
    list = []
    for row in spamreader:
        val = abs(long(row[3]) - long(row[2]))
        if 0 < val < 2000:
            list.append(val)

    sorted_list = sorted(list)

    print(max(sorted_list))
    print(sorted_list)
    print (numpy.histogram(sorted_list, bins=numpy.arange(max(sorted_list) + 1)))
    print (numpy.percentile(sorted_list, 95))
    print (numpy.percentile(sorted_list, 99))

    hist, bin_edges = numpy.histogram(sorted_list, bins=numpy.arange(max(sorted_list) + 1))
    s = ''
    for h in hist:
        s += str(h) + ','

    v = ''
    for e in bin_edges:
        v += str(e) + ','
    print(s[:-1])
    print(v[:-1])
