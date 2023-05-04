import os
import shutil
import glob
import json

path_to_exp = os.path.join("exp.conf")
path_to_train = os.path.join("train_round")
path_to_test = os.path.join("test_round")

# remove train
shutil.rmtree(path_to_train)
# remove test file
with open(path_to_exp,'r') as exp:
	exp_dic = json.load(exp)
	num_rounds = exp_dic["NUM_ROUNDS"]
for i in range(0, num_rounds):
	path_to_round_folder = os.path.join("test_round", "round_{}".format(i))
	for infile in glob.glob(os.path.join(path_to_round_folder, '*.pkl')):
		os.remove(infile)
	for infile in glob.glob(os.path.join(path_to_round_folder, '*.txt')):
		os.remove(infile)
   
    