#! /usr/bin/python3

import glob
import test_config as cfg
import matplotlib.pyplot as plt


netperfs = []
for file in glob.glob("./{}*netperf.txt".format(cfg.antena)):
    print(file)
    data = open(file).read()
    netperf_value = float((data.split()[-5]))
    print(netperf_value)
    netperfs.append(netperf_value)

fig = plt.figure()
ax = fig.add_subplot(111)

#plt.plot(cfg.canales, netperfs)

for xy in zip(cfg.canales, netperfs):
    ax.annotate(xy[1], xy=xy, textcoords='data')

print(len(cfg.canales))
print(len(netperfs))
plt.plot([ str(c) for c in cfg.canales], netperfs)



plt.xlabel("Canal")
plt.ylabel("Mbps")
#plt.xticks(cfg.canales)
plt.grid()
plt.show()

    
