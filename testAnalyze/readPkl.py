#show_pkl.py
 
import pickle
path='total_samples_inter_0.pkl'   #path='/root/……/aus_openface.pkl'   pkl文件所在路径
# path='inter_8.pkl' 

with open(path, 'rb') as f:
    while True:
        try:
            data = pickle.load(f)
            print(data)
        except EOFError:
            break
# print(len(data))