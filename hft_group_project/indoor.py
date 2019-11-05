import os 
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime

indoor_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', 'indoor.csv')
indoor = pd.read_csv(indoor_loc)

df = pd.DataFrame(indoor, columns=indoor.columns.values)
# drop date col
df.drop('date', axis=1, inplace=True)
# convert datatype to numeric
df = df.apply(pd.to_numeric, errors='coerce')
# calc avg of every column
indoor_mean = df.mean(axis=0)

plt.figure(figsize=(12, 10))
plt.style.use('ggplot')
indoor_mean.plot.bar(rot=0)

plt.show()
