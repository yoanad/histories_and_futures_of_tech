import os 
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime

# === Day 1
d1t1_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', '20-30.csv')
d1t1_data = pd.read_csv(d1t1_loc)
d1t2_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', '93.csv')
d1t2_data = pd.read_csv(d1t2_loc)
d1t3_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', '1.5-2.csv')
d1t3_data = pd.read_csv(d1t3_loc)
# Day 1 ===


# === Day 2
d2t1_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/day2', '25.csv')
d2t1_data = pd.read_csv(d2t1_loc)
d2t2_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/day2', '130.csv')
d2t2_data = pd.read_csv(d2t2_loc)
d2t3_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets/day2', '300.csv')
d2t3_data = pd.read_csv(d2t3_loc)
# Day 2 ===

# other outdoor tree
d4t1_loc = os.path.join(os.getcwd(), 'hft_group_project/datasets', 'outdoortree.csv')
d4t1_data = pd.read_csv(d4t1_loc)
d4t1 = pd.DataFrame(d4t1_data, columns=d4t1_data.columns.values)
d4t1.drop('date', axis=1, inplace=True)
d4t1 = d4t1.apply(pd.to_numeric, errors='coerce')

# day 1 
d1t1 = pd.DataFrame(d1t1_data, columns=d1t1_data.columns.values)
d1t1.drop('date', axis=1, inplace=True)
d1t1 = d1t1.apply(pd.to_numeric, errors='coerce')

d1t2 = pd.DataFrame(d1t2_data, columns=d1t2_data.columns.values)
d1t2.drop('date', axis=1, inplace=True)
d1t2 = d1t2.apply(pd.to_numeric, errors='coerce')

d1t3 = pd.DataFrame(d1t3_data, columns=d1t3_data.columns.values)
d1t3.drop('date', axis=1, inplace=True)
d1t3 = d1t3.apply(pd.to_numeric, errors='coerce')


#day 2
d2t1 = pd.DataFrame(d2t1_data, columns=d2t1_data.columns.values)
d2t1.drop('date', axis=1, inplace=True)
d2t1 = d2t1.apply(pd.to_numeric, errors='coerce')

d2t2 = pd.DataFrame(d2t2_data, columns=d2t2_data.columns.values)
d2t2.drop('date', axis=1, inplace=True)
d2t2 = d2t2.apply(pd.to_numeric, errors='coerce')

d2t3 = pd.DataFrame(d2t3_data, columns=d2t3_data.columns.values)
d2t3.drop('date', axis=1, inplace=True)
d2t3 = d2t3.apply(pd.to_numeric, errors='coerce')


d1_soil_dataset = [d1t1["soil"], d1t2["soil"], d1t3["soil"], d4t1["soil"]]
d1_temperature_dataset = [d1t1["temperature"], d1t2["temperature"], d1t3["temperature"], d4t1["temperature"]]
d1_humidity_dataset = [d1t1["humidity"], d1t2["humidity"], d1t3["humidity"], d4t1["humidity"]]
d1_light_dataset = [d1t1["light"], d1t2["light"], d1t3["light"], d4t1["light"]]
d1_air_dataset = [d1t1["air"], d1t2["air"], d1t3["air"], d4t1["air"]]
d1_tree_titles = ["20-30", "80-90cm", "150-200cm", "Independant day, street tree"]

d2_soil_dataset = [d2t1["soil"], d2t2["soil"], d2t3["soil"], d4t1["soil"]]
d2_temperature_dataset = [d2t1["temperature"], d2t2["temperature"], d2t3["temperature"], d2t1["temperature"]]
d2_humidity_dataset = [d2t1["humidity"], d2t2["humidity"], d2t3["humidity"], d4t1["humidity"]]
d2_light_dataset = [d2t1["light"], d2t2["light"], d2t3["light"], d4t1["light"]]
d2_air_dataset = [d2t1["air"], d2t2["air"], d2t3["air"], d4t1["air"]]
d2_tree_titles = ["20-30", "80-90cm", "150-200cm", "Independant day, street tree"]


d2_tree_titles = ["20-30cm", "130-150cm", "200-300cm", "Independant day, street tree"]
plt.close('all')


f1 = plt.figure(figsize=(24, 16))
f1.suptitle("Soil values, day 1", fontsize=14)
plt.style.use('ggplot')

for i in range(len(d1_soil_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d1_soil_dataset[i])
    plot.set_title(d1_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')
f1.suptitle("Soil values, day 1", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Soil values, day 1', bbox_inches='tight', dpi=100)


f2 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d2_soil_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d2_soil_dataset[i])
    plot.set_title(d2_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f2.suptitle("Soil values, day 2", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Soil values, day 2', bbox_inches='tight', dpi=100)

f3 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d1_temperature_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d1_temperature_dataset[i])
    plot.set_title(d1_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f3.suptitle("Temperature values, day 1", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Temperature values, day 1', bbox_inches='tight', dpi=100)

f4 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d2_temperature_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d2_temperature_dataset[i])
    plot.set_title(d2_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f4.suptitle("Temperature values, day 2", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Temperature values, day 2', bbox_inches='tight', dpi=100)

f5 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d1_humidity_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d1_humidity_dataset[i])
    plot.set_title(d1_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f5.suptitle("Humidity values, day 1", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Humidity values, day 1', bbox_inches='tight', dpi=100)

f6 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d2_humidity_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d2_humidity_dataset[i])
    plot.set_title(d2_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f6.suptitle("Humidity values, day 2", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Humidity values, day 2', bbox_inches='tight', dpi=100)

f7 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d1_light_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d1_light_dataset[i])
    plot.set_title(d1_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')
f7.suptitle("Light values, day 1", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Light values, day 1', bbox_inches='tight', dpi=100)

f8 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d2_light_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d2_light_dataset[i])
    plot.set_title(d2_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f8.suptitle("Light values, day 2", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Light values, day 2', bbox_inches='tight', dpi=100)

f9 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d1_air_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d1_air_dataset[i])
    plot.set_title(d1_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f9.suptitle("Air Quality values, day 1", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Air Quality values, day 1', bbox_inches='tight', dpi=100)

f10 = plt.figure(figsize=(24, 16))
plt.style.use('ggplot')

for i in range(len(d2_air_dataset)):
    plot = plt.subplot(2,4,i+1)
    plt.plot(d2_air_dataset[i])
    plot.set_title(d2_tree_titles[i])
    plt.xlabel('time')
    plt.ylabel('value')

f10.suptitle("Air Quality  values, day 2", x = 0.15, y=.95, horizontalalignment='left', verticalalignment='top', fontsize = 15)
plt.savefig('Air Quality values, day 2.png', bbox_inches='tight', dpi=100)

plt.show()
