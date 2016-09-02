import csv
import numpy
import glob
import matplotlib.pyplot as plt

# folders = ['hz/ini_rmv/']
folders = ['zk/ini_rmv1/', 'zk/ini_rmv2/']

exts = {}
rmvs = {}

add_time = []
remove_time = []


def get_name(param, file_name):
    slash_index = file_name.rindex('/') + 1
    dot_index = file_name.rindex('.')
    suffix = file_name[slash_index:dot_index]

    return param + suffix


for folder in folders:
    for file_name in glob.glob(folder + "*.txt"):
        with open(file_name, 'rb') as result_file:
            spam_reader = csv.reader(result_file, delimiter=',')

            for row in spam_reader:
                if len(row) != 4:
                    continue
                if row[1] == 'ext':
                    print row
                    exts[row[3]] = row[2]
                elif row[1] == 'rmv':
                    print '\t ' + str(row)
                    values = rmvs.get(row[3], [])
                    values.append(row[2])
                    rmvs[row[3]] = values

print exts
print rmvs

for key, value in exts.iteritems():
    v = rmvs.get(key)
    if v is None:
        continue
    for val in v:
        computed = abs(long(value) - long(val))
        if 0 < computed < 20000:
            add_time.append(computed)
        elif 20000 <= computed < 200000:
            add_time.append(computed/10)

add_time = sorted(add_time)

print add_time
print (len(add_time))
print(min(add_time))
print(max(add_time))
# print(add_time)
# print (numpy.histogram(add_time, bins=numpy.arange(start=1, stop=max(add_time) + 1)))
print ('95:  ' + str(numpy.percentile(add_time, 95)))
print ('99:  ' + str(numpy.percentile(add_time, 99)))
print ('avg: ' + str(numpy.average(add_time)))

print (add_time)

hist, bin_edges = numpy.histogram(add_time, bins=numpy.arange(start=1, stop=max(add_time) + 1))

bins = [i for i in xrange(0, max(add_time) + 1, 20)]
print (bins)

my_dpi = 96

plt.hist(add_time, bins, color='black')
# plt.rc('font', **font)
plt.rcParams.update({'font.size': 19})

fig = plt.gcf()
fig.tight_layout(pad=2)
plt.xlabel('time [ms]')
plt.ylabel('count')

plt.show()

