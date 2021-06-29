import numpy as np
import pandas as pd

# COnfig the number of users at the groud
N_Config = [50,100,150]
N = N_Config[0]
# config the mission ground
MaximumX = 1000 #km
MaximumY = 1000 #km
# config rate requirement of 5G devices
MaximumRate = 20 #Gb/s
MinimumRate = 10 #Gb/s

# generate data rate of users
data_rate = np.random.randint(10000,20000,N)
print(data_rate)



