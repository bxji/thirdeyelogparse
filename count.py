import os
import sys

logs = ['log1', 'log2', 'log3']
cache_logs = ['cache_log1', 'cache_log2', 'cache_log3']

folder = sys.argv[1]

final_fetch = 0
final_total = 0

for log in logs:
    total = 0
    dft = 0
    with open(folder + '/' + log, 'r') as file:
        for line in file:
            if 'Preview successful' in line:
                time = line.split('Preview successful, used ')[1].split(' ')[0]
                total = int(time)
            elif line.startswith('HI_BRYAN'):
                time = line.split(' ')[1]
                dft += int(time)
    
    final_fetch += dft
    final_total += total

    print('total time for ' + str(log) + ' was ' + str(total) + ' ms')
    print('data fetch time for ' + str(log) + ' was ' + str(dft) + ' ms')
    print('anomaly detection time for ' + str(log) + ' was ' + str(total - dft) + ' ms')
    print()

print('avg total time for ' + folder + ' uncached was ' + str(final_total / 3))
print('avg fetch time for ' + folder + ' uncached was ' + str(final_fetch / 3))
print('avg anomaly detection time for ' + folder + 'uncached was ' + str((final_total - final_fetch)/3) + ' ms')
print()

final_fetch = 0
final_total = 0

for log in cache_logs:
    total = 0
    dft = 0
    with open(folder + '/' + log, 'r') as file:
        for line in file:
            if 'Preview successful' in line:
                time = line.split('Preview successful, used ')[1].split(' ')[0]
                total = int(time)
            elif line.startswith('HI_BRYAN'):
                time = line.split(' ')[1]
                dft += int(time)
    
    final_fetch += dft
    final_total += total

    print('total time for ' + str(log) + ' was ' + str(total) + ' ms')
    print('data fetch time for ' + str(log) + ' was ' + str(dft) + ' ms')
    print('anomaly detection time for ' + str(log) + ' was ' + str(total - dft) + ' ms')
    print()

print('avg total time for ' + folder + ' with cache was ' + str(final_total / 3))
print('avg fetch time for ' + folder + ' with cache was ' + str(final_fetch / 3))
print('avg anomaly detection time for ' + folder + ' with cache was ' + str((final_total - final_fetch)/3) + ' ms')
print()
