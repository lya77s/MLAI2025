import numpy as np

x = np.random.randn(1000)  
mean = x.mean()
var = x.var(ddof=0)     
std = x.std(ddof=0)       

print("mean:", mean)
print("variance:", var)
print("std:", std)