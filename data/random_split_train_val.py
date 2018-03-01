import numpy as np
import os

data_dir = './KITTI/training/image_2'
image_set_dir = './KITTI/ImageSets'
trainval_file = image_set_dir+'/trainval.txt'
train_file = image_set_dir+'/train.txt'
val_file = image_set_dir+'/val.txt'

idx = [f.split('.png')[0] for f in os.listdir(data_dir) if f.endswith(".png")]
"""idx = []
with open(trainval_file) as f:
  for line in f:
    idx.append(line.strip())
f.close()
"""
idx = np.random.permutation(idx)

train_idx = sorted(idx[:np.int(len(idx)/2)])
val_idx = sorted(idx[np.int(len(idx)/2):])

with open(train_file, 'w') as f:
  for i in train_idx:
    f.write('{}\n'.format(i))
f.close()

with open(val_file, 'w') as f:
  for i in val_idx:
    f.write('{}\n'.format(i))
f.close()

print('Trainining set is saved to ' + train_file)
print('Validation set is saved to ' + val_file)
