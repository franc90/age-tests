import csv
import numpy
import matplotlib.pyplot as plt

font = {'family': 'normal',
        'weight': 'normal',
        'size': 20}

with open('rcvs.csv', 'rb') as rcvs:
    spamreader = csv.reader(rcvs, delimiter=',')
    list = []
    i = 0
    for row in spamreader:
        if i >= 1250:
            break
        val = abs(long(row[3]) - long(row[2]))
        if 0 < val < 2000:
            list.append(val)
            i += 1

    sorted_list = sorted(list)

    print (len(sorted_list))
    print(min(sorted_list))
    print(max(sorted_list))
    # print(sorted_list)
    # print (numpy.histogram(sorted_list, bins=numpy.arange(start=1, stop=max(sorted_list) + 1)))
    print ('95:  ' + str(numpy.percentile(sorted_list, 95)))
    print ('99:  ' + str(numpy.percentile(sorted_list, 99)))
    print ('avg: ' + str(numpy.average(sorted_list)))

    hist, bin_edges = numpy.histogram(sorted_list, bins=numpy.arange(start=1, stop=max(sorted_list) + 1))

    bins = [i for i in xrange(0, max(sorted_list) + 1)]
    print (bins)

    my_dpi = 96

    plt.hist(sorted_list, bins, color='black')
    # plt.rc('font', **font)
    plt.rcParams.update({'font.size': 19})

    fig = plt.gcf()
    fig.tight_layout(pad=2)
    plt.xlabel('time [ms]')
    plt.ylabel('count')

    plt.show()
