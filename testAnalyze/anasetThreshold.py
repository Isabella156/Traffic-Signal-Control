import json
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--title", type=str, default='Hangzhou 4_4')
parser.add_argument("--threshold", type=int, default=200)
argument = parser.parse_args()
# read parameters
path_to_result = "result.json"
with open(path_to_result, 'r') as result:
	result_dic = json.load(result)
	numRounds = result_dic["NumRounds"]
	numIntersections = result_dic["NumberIntersections"]

threshold = argument.threshold
numNan = []
allDuration = []

for i in range(0, numRounds):
	path_to_round_folder = os.path.join("test_round", "round_{}".format(i))
	nanCount = 0
	# print("round num: ", i, "\n")
	for j in range(0, numIntersections):
		path_to_vehicle = os.path.join(path_to_round_folder, "vehicle_inter_{}.csv".format(j))
		df_vehicle = pd.read_csv(path_to_vehicle, sep=',', header=0, dtype={'':str, 'enter_time': float, 'leave_time': float},
                names=["", "enter_time", "leave_time"])
		duration = df_vehicle["leave_time"].values - df_vehicle["enter_time"].values
		leaveTime = df_vehicle["leave_time"]
		nanCount += leaveTime.isna().sum()
	numNan.append(nanCount)

# plot number of NaN

x = np.arange(numRounds)
y = numNan
plt.plot(x, y, color="#96cccb", marker=".", linestyle="-")
plt.xlabel("Number of Rounds")
plt.ylabel("Number of NaN")
plt.title(argument.title)
fileName = argument.title.replace(' ', '')
plt.savefig(fileName + "nanNum.svg")
