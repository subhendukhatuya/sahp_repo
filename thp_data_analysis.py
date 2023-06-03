import pickle
import numpy as np

thp_data_path = './stackoverflow_formatted_seq_len_500'
with open(thp_data_path + '/train.pkl', 'rb') as f:
	data = pickle.load(f, encoding='latin-1')
	num_types = data['dim_process']
	data = data['train']
        

inter_arrival_times = []
for seq_index in range(int(len(data)/2)):
    seq = data[seq_index]

    for event in seq:
        inter_arrival_times.append(event['time_since_last_event'])


print(len(inter_arrival_times))
print('mean of ineter arrival time is', np.mean(inter_arrival_times))

print('variance of int arr time', np.var(inter_arrival_times))



#print(data[-1])
