import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--title", type=str, default='Hangzhou 4_4')
argument = parser.parse_args()

# running time
'''
df = pd.read_csv('running_time.csv', sep='\t', header=0)
all_times = df['all_times'].values
x = np.arange(all_times.size)
y = all_times
plt.plot(x, y, color="#96cccb", marker=".", linestyle="-")
plt.xlabel("Number of Rounds")
plt.ylabel("Running Time")
plt.title(argument.title)
fileName = argument.title.replace(' ', '')
plt.savefig(fileName + "running_time.svg")
'''



# real dataset
# Jinan, Hangzhou, New York
'''
size = 3
x = np.arange(size)

attention = np.array([95.89, 86.93, 17.63])
Fixedtime = np.array([61.83, 81.83, 23.27])
MaxPressure = np.array([103.22, 116.31, 44.46])

labels = ['Jinan', 'Hangzhou', 'New York']

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, attention,  width=width, label='Attention', fc='#A1A9D0')
plt.bar(x + width, Fixedtime, width=width, label='Fixedtime', fc='#CFEAF1', tick_label=labels)
plt.bar(x + 2 * width, MaxPressure, width=width, label='MaxPressure', fc='#F6CAE5')
plt.legend()
for i, v in enumerate(attention):
    plt.text(x[i], v + 0.5, str(v), ha='center', fontsize=8)
for i, v in enumerate(Fixedtime):
    plt.text(x[i] + width, v + 0.5, str(v), ha='center', fontsize=8)
for i, v in enumerate(MaxPressure):
    plt.text(x[i] + 2 * width, v + 0.5, str(v), ha='center', fontsize=8)
plt.savefig("realDataset.svg")
'''
# virtual dataset LSR
# 3_3 6_6 10_10
'''
size = 3
x = np.arange(size)

attention = np.array([29.17, 28.42, 29.62])
Fixedtime = np.array([35.63, 36.22, 36.47])
MaxPressure = np.array([34.19, 33.47, 33.90])

labels = ['3_3', '6_6', '10_10']

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, attention,  width=width, label='Attention', fc='#A1A9D0')
plt.bar(x + width, Fixedtime, width=width, label='Fixedtime', fc='#CFEAF1', tick_label=labels)
plt.bar(x + 2 * width, MaxPressure, width=width, label='MaxPressure', fc='#F6CAE5')
plt.ylim(bottom=0, top=50)
plt.legend()
for i, v in enumerate(attention):
    plt.text(x[i], v + 0.5, str(v), ha='center', fontsize=8)
for i, v in enumerate(Fixedtime):
    plt.text(x[i] + width, v + 0.5, str(v), ha='center', fontsize=8)
for i, v in enumerate(MaxPressure):
    plt.text(x[i] + 2 * width, v + 0.5, str(v), ha='center', fontsize=8)
plt.savefig("virtualDatasetLSR.svg")

# virtual dataset S
# 1_1 1_2 1_3 1_10
'''

'''
size = 4
x = np.arange(size)

Attention = np.array([26.0, 29.12, 28.95, 28.88])
Fixedtime = np.array([29.44, 34.81, 34.96, 35.07])
MaxPressure = np.array([29.42, 29.20, 29.57, 28.76])

labels = ['1_1', '1_2', '1_3', '1_10']

total_width, n = 1, 4
width = total_width / n
x = x - (total_width - width) / 3

plt.ylim(bottom=0, top=40)
plt.bar(x, Attention,  width=width, label='Attention', fc='#A1A9D0')
plt.bar(x + width, Fixedtime, width=width, label='Fixedtime', fc='#CFEAF1', tick_label=labels)
plt.bar(x + 2 * width, MaxPressure, width=width, label='MaxPressure', fc='#F6CAE5')
plt.legend(loc='best')
for i, v in enumerate(Attention):
    plt.text(x[i], v + 0.5, str(v), ha='center', fontsize=8)
for i, v in enumerate(Fixedtime):
    plt.text(x[i] + width, v + 0.5, str(v), ha='center', fontsize=8)
for i, v in enumerate(MaxPressure):
    plt.text(x[i] + 2 * width, v + 0.5, str(v), ha='center', fontsize=8)
plt.savefig("virtualDatasetS.svg")
'''

# Uni-direction/Bi-direction

size = 6
x = np.arange(size)

Attention = np.array([29.17, 29.62, 28.42, 28.81, 29.62, 28.02])
Fixedtime = np.array([34.19, 33.64, 33.47, 31.93, 33.90, 31.12])
MaxPressure = np.array([35.63, 35.63, 36.22, 36.22, 36.47, 36.47])

labels = ['3_3 Bi', '3_3 Uni', '6_6 Bi', '6_6 Uni', '10_10 Bi', '10_10 Uni']

plt.xlabel("Direction")
plt.ylabel("Average Travel Time")

plt.plot(labels[0:2], Attention[0:2], marker='o', markersize=3, color="#B883D4", label='Attention')
plt.plot(labels[2:4], Attention[2:4], marker='o', markersize=3, color="#B883D4")
plt.plot(labels[4:6], Attention[4:6], marker='o', markersize=3, color="#B883D4")

plt.plot(labels[0:2], Fixedtime[0:2], marker='o', markersize=3, color="#9E9E9E", label='Fixedtime')
plt.plot(labels[2:4], Fixedtime[2:4], marker='o', markersize=3, color="#9E9E9E")
plt.plot(labels[4:6], Fixedtime[4:6], marker='o', markersize=3, color="#9E9E9E")

plt.plot(labels[0:2], MaxPressure[0:2], marker='o', markersize=3, color="#F0988C", label='MaxPressure')
plt.plot(labels[2:4], MaxPressure[2:4], marker='o', markersize=3, color="#F0988C")
plt.plot(labels[4:6], MaxPressure[4:6], marker='o', markersize=3, color="#F0988C")
# total_width, n = 1, size
# width = total_width / n
# x = x - (total_width - width) / (size - 1)

# plt.ylim(bottom=0, top=50)
# plt.bar(x, Attention,  width=width, label='Attention', fc='#B883D4')
# plt.bar(x + width, Fixedtime, width=width, label='Fixedtime', fc='#9E9E9E', tick_label=labels)
# plt.bar(x + 2 * width, MaxPressure, width=width, label='MaxPressure', fc='#F0988C')
plt.legend()
# for i, v in enumerate(Attention):
#     plt.text(x[i], v + 0.5, str(v), ha='center', fontsize=8)
# for i, v in enumerate(Fixedtime):
#     plt.text(x[i] + width, v + 0.5, str(v), ha='center', fontsize=8)
# for i, v in enumerate(MaxPressure):
#     plt.text(x[i] + 2 * width, v + 0.5, str(v), ha='center', fontsize=8)
plt.savefig("UniBiDirection.svg")


# traffic flow 1_1
'''
size = 7
x = np.arange(size)

Attention = np.array([26.0, 26.48, 27.60, 30.89, 31.54, 33.71, 40.99])
Fixedtime = np.array([29.44, 29.54, 31.18, 30.89, 31.94, 41.08, 50.54])
MaxPressure = np.array([29.42, 29.53, 31.17, 30.88, 31.93, 33.72, 142.19])
x = [100, 200, 300, 400, 500, 600, 700]

plt.title("1_1 Traffic Flow")
plt.xlabel("Traffic Flow")
plt.ylabel("Average Travel Time")

plt.plot(x, Attention, marker='o', markersize=3, color="#7898e1")
plt.plot(x, Fixedtime, marker='o', markersize=5, color="#efa666")
plt.plot(x, MaxPressure, marker='o', markersize=3, color="#eddd86")

plt.legend(['Attention', 'Fixedtime', 'MaxPressure'])

y_major_locator=MultipleLocator(20)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim(25, 52)

plt.savefig("TrafficFlow1_1.svg")
'''

# trafic flow 1_2
'''
size = 7
x = np.arange(size)

Attention = np.array([29.12, 31.07, 31.50, 33.00, 33.78, 31.92, 34.01])
Fixedtime = np.array([34.81, 37.19, 36.35, 37.65, 38.64, 52.82, 82.67])
MaxPressure = np.array([29.20, 32.15, 36.40, 36.45, 38.67, 52.81, 47.53])
x = [100, 200, 300, 400, 500, 600, 700]

plt.title("1_2 Traffic Flow")
plt.xlabel("Traffic Flow")
plt.ylabel("Average Travel Time")

plt.plot(x, Attention, marker='o', markersize=3, color="#7898e1")
plt.plot(x, Fixedtime, marker='o', markersize=5, color="#efa666")
plt.plot(x, MaxPressure, marker='o', markersize=3, color="#eddd86")

plt.legend(['Attention', 'Fixedtime', 'MaxPressure'])

y_major_locator=MultipleLocator(20)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim(25, 85)

plt.savefig("TrafficFlow1_2.svg")
'''

# trafic flow 1_3
'''
size = 7
x = np.arange(size)

Attention = np.array([28.95, 29.64, 31.41, 31.52, 32.84, 31.88, 37.07])
Fixedtime = np.array([34.96, 37.29, 36.22, 37.57, 38.10, 53.97, 73.79])
MaxPressure = np.array([29.58, 32.62, 37.56, 34.87, 38.95, 47.10, 44.05])
x = [100, 200, 300, 400, 500, 600, 700]

plt.title("1_3 Traffic Flow")
plt.xlabel("Traffic Flow")
plt.ylabel("Average Travel Time")

plt.plot(x, Attention, marker='o', markersize=3, color="#7898e1")
plt.plot(x, Fixedtime, marker='o', markersize=5, color="#efa666")
plt.plot(x, MaxPressure, marker='o', markersize=3, color="#eddd86")

plt.legend(['Attention', 'Fixedtime', 'MaxPressure'])

y_major_locator=MultipleLocator(20)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim(25, 75)

plt.savefig("TrafficFlow1_3.svg")
'''

# trafic flow 1_3
'''
size = 7
x = np.arange(size)

Attention = np.array([28.88, 26.49, 31.49, 32.67, 34.85, 34.22, 32.32])
Fixedtime = np.array([35.07, 37.49, 36.00, 37.47, 38.07, 55.17, 61.25])
MaxPressure = np.array([28.77, 31.83, 36.41, 33.54, 38.55, 52.92, 60.15])
x = [100, 200, 300, 400, 500, 600, 700]

plt.title("1_10 Traffic Flow")
plt.xlabel("Traffic Flow")
plt.ylabel("Average Travel Time")

plt.plot(x, Attention, marker='o', markersize=3, color="#7898e1")
plt.plot(x, Fixedtime, marker='o', markersize=5, color="#efa666")
plt.plot(x, MaxPressure, marker='o', markersize=3, color="#eddd86")

plt.legend(['Attention', 'Fixedtime', 'MaxPressure'])

y_major_locator=MultipleLocator(20)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim(25, 65)

plt.savefig("TrafficFlow1_10.svg")
'''