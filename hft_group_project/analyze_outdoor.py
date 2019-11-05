import os 
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime

water_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', 'water.csv')
water_data = pd.read_csv(water_loc)

# === Day 2
tree1_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/', 'outdoortree.csv')
tree1_data = pd.read_csv(tree1_loc)
# Day 2 ===

tree1 = pd.DataFrame(tree1_data, columns=tree1_data.columns.values)
# drop date col
tree1.drop('date', axis=1, inplace=True)

# convert datatype to numeric
tree1 = tree1.apply(pd.to_numeric, errors='coerce')

tree1 = tree1[tree1["soil"] < 100 ]
# calc avg of every column
tree1_mean = tree1.mean(axis=0)

plt.figure(figsize=(12, 10))
plt.style.use('ggplot')
plot1 = plt.subplot(221)
tree1_mean.plot.bar(rot=0)
plt.title("Street tree", loc='left', fontsize=12, fontweight=0, color='orange')

plt.show()
