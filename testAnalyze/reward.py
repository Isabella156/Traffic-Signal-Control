import json
import pickle
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_to_result = "result.json"

with open(path_to_result, 'r') as result:
	result_dic = json.load(result)
	numRounds = result_dic["NumRounds"]
	numIntersections = result_dic["NumberIntersections"]

RoundReward = []

# numIntersections = 2

# for i in range(numRounds):
# 	for i in range(numIntersections):
# 		sample_file = open(os.path.join("train_round", "total_samples_inter_{0}".format(i) + ".pkl"), "rb")
# 		with open(sample_file, 'rb') as f:

total_inter_reward = []
for i in range(numIntersections):
	sample_file = os.path.join("train_round", "total_samples_inter_{0}".format(i) + ".pkl")
	inter_reward = []
	with open(sample_file, 'rb') as f:
		while True:
			try:
				sample_set = pickle.load(f)
				samples_set_df = pd.DataFrame.from_records(sample_set,columns= ['state','action','next_state','inst_reward','reward','time','generator'])
				reward_col = samples_set_df['reward']
				round_mean_reward = np.mean(reward_col)
				inter_reward.append(round_mean_reward)
			except EOFError:
				break
	total_inter_reward.append(inter_reward)

# inter_reward = np.array(inter_reward)
# print(inter_reward)
# print(inter_reward.shape)

# total_inter_reward = np.array(total_inter_reward)
# print(total_inter_reward)
# print(total_inter_reward.shape)

sum_reward = np.sum(total_inter_reward, axis=0)
print(sum_reward)
print(sum_reward.shape)

x = np.arange(100)
y = sum_reward
plt.plot(x, y, color="#96cccb", marker=".", linestyle="-")
plt.xlabel("Number of Rounds")
plt.ylabel("Reward")
plt.savefig("reward.svg")

