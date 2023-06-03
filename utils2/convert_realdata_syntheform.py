import pickle
import numpy as np

def convert_task_sub(task, sub):
    timestamps_list = []
    types_list = []
    lengths_list = []
    timeintervals_list = []

    file_path = '/NS/ssdecl/work/point_process/thp_dataset/' + task + '_formatted_seq_len_500/' + sub +'.pkl'
    with open(file_path, 'rb') as f:
        file = pickle.load(f, encoding='latin1')
        dim_process = file['dim_process']
        print('dim_process: {} for task: {}'.format(dim_process,task))
        seqs = file[sub]
        one_seq_num = 0
        for seq in seqs:
            timestamps = []
            types = []
            timeintervals = []
            for event in seq:
                event_type = event['type_event']
                event_timestamp = event['time_since_start']
                event_timeinterval = event['time_since_last_event']

                timestamps.append(event_timestamp)
                types.append(event_type)
                timeintervals.append(event_timeinterval)
            lengths = len(seq)
            if lengths == 1:
                one_seq_num += 1
                continue

            if sub=='test':
                timestamps = timestamps[int(len(timestamps)*0.70):]
                types = types[int(len(types)*0.70):]
                lengths = int(lengths*0.30)
        

            timestamps_list.append(np.asarray(timestamps))
            types_list.append(np.asarray(types))
            lengths_list.append(np.asarray(lengths))
            timeintervals_list.append(np.asarray(timeintervals))

    #print('one_seq_num: {}'.format(one_seq_num))
    #print('types', types_list)
    save_path = '/NS/ssdecl/work/point_process/sahp_data/' + task + '/' + sub +'.pkl'
    with open(save_path, "wb") as f:
        save_data_ = {'timestamps': np.asarray(timestamps_list),
                     'types': np.asarray(types_list),
                     'lengths': np.asarray(lengths_list),
                     'timeintervals': np.asarray(timeintervals_list)
                      }
        pickle.dump(save_data_,f)

if __name__ == '__main__':
    task_list = ['stackoverflow']
    sub_dataset = ['train', 'dev', 'test']

    for task in task_list:
        for sub in sub_dataset:
            convert_task_sub(task,sub)
