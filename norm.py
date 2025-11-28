import numpy as np

data = np.array([5,10,15,20,25], dtype=float)

min_val = data.min()
max_val = data.max()
minmax_norm = (data - min_val) / (max_val - min_val)

mean = data.mean()
std = data.std(ddof=0) 
z_score = (data - mean) / std

print("original:", data)
print("min-max normalized:", minmax_norm)
print("z-score normalized:", z_score)