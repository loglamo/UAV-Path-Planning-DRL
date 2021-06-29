import numpy as np
import pandas as pd

# COnfig the number of users at the groud
N_Config = [50,100,150]
N = N_Config[0]
# config the mission ground
MaximumX = 1 #km-> m
MaximumY = 1 #km-> m

# generate N fixed users on the ground
coords = [(np.random.randint(0,1000), np.random.randint(0,1000)) for _ in range(N)]
print(coords)
pd.DataFrame(coords).to_csv("coord_v1.csv")
