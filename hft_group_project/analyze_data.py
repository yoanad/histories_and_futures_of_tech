import os 
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime

water_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', 'water.csv')
water_data = pd.read_csv(water_loc)

# --- Day 1
# tree1_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', '20-30.csv')
# tree1_data = pd.read_csv(tree1_loc)
# tree2_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', '93.csv')
# tree2_data = pd.read_csv(tree2_loc)
# tree3_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', '1.5-2.csv')
# tree3_data = pd.read_csv(tree3_loc)
# Day 1 ---

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

water = pd.DataFrame(water_data, columns=water_data.columns.values)
# drop date col
water.drop('date', axis=1, inplace=True)
# convert datatype to numeric
water = water.apply(pd.to_numeric, errors='coerce')

# calc avg of every column
tree1_mean = tree1.mean(axis=0)
tree2_mean = tree2.mean(axis=0)
tree3_mean = tree3.mean(axis=0)
water_mean = water.mean(axis=0)

plt.figure(figsize=(12, 10))
plt.style.use('ggplot')

# === Day 1
# # tree 1
# plot1 = plt.subplot(221)
# tree1_mean.plot.bar(rot=0)
# plot1.set_title('20-30cm')

# #tree 2
# plot2 = plt.subplot(222)
# tree2_mean.plot.bar(rot=0)
# plot2.set_title('80-90cm')

# #tree 3
# plot3 = plt.subplot(223)
# tree3_mean.plot.bar(rot=0)
# plot3.set_title('150-200cm')
# Day 1 ===

# === Day 2

f2 = plt.figure(2)
plot1 = plt.subplot(221)
tree1_mean.plot.bar(rot=0)
plot1.set_title('20-30cm')

#tree 2
plot2 = plt.subplot(222)
tree2_mean.plot.bar(rot=0)
plot2.set_title('130-150cm')

#tree 3
plot3 = plt.subplot(223)
tree3_mean.plot.bar(rot=0)
plot3.set_title('200-300cm')
# Day 2 ===

#tree 4
plot4 = plt.subplot(224)
water_mean.plot.bar(rot=0)
plot4.set_title('water/studio')


## === Day 1
# f3 = plt.figure(3)
# light_vals = [ tree1_mean["light"], tree2_mean["light"], tree3_mean["light"]]
# light_graph = pd.DataFrame({'x': ["20-30", "80-90", "150-200"], 'y': light_vals })
# lp = plt.plot( 'x', 'y', data=light_graph, linestyle='dashed')
# plt.title("Light changes, day 1", loc='left', fontsize=12, fontweight=0, color='orange')
# plt.xlabel("Tree Diameter")
# plt.ylabel("Light Value")
## Day 1 ===

## === Day 2
f4 = plt.figure(4)
light_vals = [ tree1_mean["light"], tree2_mean["light"], tree3_mean["light"]]
light_graph = pd.DataFrame({'x': ["20-30", "130-150", "200-300"], 'y': light_vals })
lp = plt.plot( 'x', 'y', data=light_graph, linestyle='dashed')
plt.title("Light changes, day 2", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Tree Diameter")
plt.ylabel("Light Value")
## Day 2 ===



plt.show()
