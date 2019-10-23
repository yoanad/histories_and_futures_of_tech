import os 
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime

sensor_data_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', 'test.csv')
sensor_data = pd.read_csv(sensor_data_loc)

df = pd.DataFrame(sensor_data, columns=sensor_data.columns.values)

# drop date col
df.drop('date', axis=1, inplace=True)

# convert datatype to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# calc avg of every column
avgs = df.mean(axis=0)

plt.figure(figsize=(12, 10))
plt.style.use('ggplot')

#tree 1
plot1 = plt.subplot(221)
avgs.plot.bar(rot=0)
plot1.set_title('tree 1')

#tree 2
plot2 = plt.subplot(222)
avgs.plot.bar(rot=0)
plot2.set_title('tree 2')

#tree 3
plot3 = plt.subplot(223)
avgs.plot.bar(rot=0)
plot3.set_title('tree 3')

#tree 4
plot4 = plt.subplot(224)
avgs.plot.bar(rot=0)
plot4.set_title('tree 4')

plt.show()
