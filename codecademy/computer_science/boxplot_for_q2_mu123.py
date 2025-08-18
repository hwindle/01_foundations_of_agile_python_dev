#!/usr/bin/python3

import matplotlib as plt
import numpy as np 

newborn_1 = (6,
                7,
                7,
                7,
                8,
                8,
                9,
                10,
                11,
                11.5,
                11.5,
                12,
                12,
                12,
                13,
                13,
                13.5,
                14,
                14,
                14.5,
                14.5)

newborn_2 = (9,
                9,
                9,
                9.5,
                10,
                10,
                10,
                10.5,
                11,
                11.5,
                12,
                12,
                12,
                12.5,
                13,
                13,
                13.5,
                14,
                14,
                14.5)

babies_data = []
babies_data.append(newborn_1)
babies_data.append(newborn_2)

# Creates a horizontal boxplot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

# rectangular box plot
bplot1 = ax1.boxplot(babies_data_data,
                     vert=False,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax1.set_title('Newborn 1 Compared to Newborn 2 Sleep Times')

# notch shape box plot
bplot2 = ax2.boxplot(babies_data_data,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
ax2.set_title('Notched box plot')

# fill with colors
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)


plt.subtitle('Source: EMA Question 2')
plt.xlabel('Hours')
plt.ylabel('Infant')
plt.show()