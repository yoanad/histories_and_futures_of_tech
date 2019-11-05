import os 
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime

# === Day 2
tree1_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/day2', '25.csv')
tree1_data = pd.read_csv(tree1_loc)
tree2_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/day2', '130.csv')
tree2_data = pd.read_csv(tree2_loc)
tree3_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/day2', '300.csv')
tree3_data = pd.read_csv(tree3_loc)
# Day 2 ===

tree1 = pd.DataFrame(tree1_data, columns=tree1_data.columns.values)
# drop date col
tree1.drop('date', axis=1, inplace=True)
# convert datatype to numeric
tree1 = tree1.apply(pd.to_numeric, errors='coerce')

tree2 = pd.DataFrame(tree2_data, columns=tree2_data.columns.values)
# drop date col
tree2.drop('date', axis=1, inplace=True)
# convert datatype to numeric
tree2 = tree2.apply(pd.to_numeric, errors='coerce')

tree3 = pd.DataFrame(tree3_data, columns=tree3_data.columns.values)
# drop date col
tree3.drop('date', axis=1, inplace=True)
# convert datatype to numeric
tree3 = tree3.apply(pd.to_numeric, errors='coerce')

# calc avg of every column
tree1_mean = tree1.mean(axis=0)
tree2_mean = tree2.mean(axis=0)
tree3_mean = tree3.mean(axis=0)

f1 = plt.figure(figsize=(18, 16))
f1.suptitle("Tree with diameter 20-30cm", fontsize=14)
plt.style.use('ggplot')
# #tree 1

plot1 = plt.subplot(231)
tree1_mean.plot.bar(rot=0)
plot1.set_title('Averages')

plot2 = plt.subplot(232)
plt.plot(tree1["temperature"])
plot2.set_title('temperature')
plt.xlabel('data measurement points')
plt.ylabel('value')

plot3 = plt.subplot(233)
plt.plot(tree1["humidity"])
plot3.set_title('humidity')
plt.xlabel('data measurement points')
plt.ylabel('value')

plot4 = plt.subplot(234)
plt.plot(tree1["light"])
plot4.set_title('light')
plt.xlabel('data measurement points')
plt.ylabel('value')


plot5 = plt.subplot(235)
plt.plot(tree1["soil"])
plot5.set_title('soil moisture')
plt.xlabel('data measurement points')
plt.ylabel('value')

plot6 = plt.subplot(236)
plt.plot(tree1["air"])
plot6.set_title('air quality')
plt.xlabel('data measurement point')
plt.ylabel('value')

# #tree 2
# plot2 = plt.subplot(222)
# tree2_mean.plot.bar(rot=0)
# plot2.set_title('130-150cm')

# #tree 3
# plot3 = plt.subplot(223)
# tree3_mean.plot.bar(rot=0)
# plot3.set_title('200-300cm')
# # Day 2 ===

# #tree 4
# plot4 = plt.subplot(224)
# water_mean.plot.bar(rot=0)
# plot4.set_title('water/studio')


# f3 = plt.figure(3)

plt.show()
