import json
import pandas as pd
import numpy as np

with open("traffic_env.conf",'r') as traffic_env:
    traffic_env_dic = json.load(traffic_env)
    num_intersections = traffic_env_dic["NUM_INTERSECTIONS"]

all_duration = []
for i in range(0, num_intersections):
    path_to_vehicle = "vehicle_inter_{}.csv".format(i)
    df_vehicle = pd.read_csv(path_to_vehicle, sep=',', header=0, dtype={'':str, 'enter_time': float, 'leave_time': float},
        names=["", "enter_time", "leave_time"])
    duration = df_vehicle["leave_time"].values - df_vehicle["enter_time"].values
    duration_without_nan = duration[~np.isnan(duration)]
    all_duration = np.append(all_duration, duration_without_nan)

mean_duration = np.mean(all_duration)
print(mean_duration)