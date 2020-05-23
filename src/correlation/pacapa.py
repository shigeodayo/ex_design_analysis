# %%
"""
# Correlation (PaCaPa: Study 1)
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use('seaborn-darkgrid')

# %%
CSV_PATH = '../../data/pacapa/study-1'
NUM_OF_PARTICIPANTS = 18
NUM_OF_TRIALS = 2
OUTPUT_PATH = 'output/pacapa/study-1'
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
x = [0.5, 0.75, 1.0, 1.25, 1.5]
y = []

# %%
for i in range(NUM_OF_PARTICIPANTS):
    p = pd.read_csv(os.path.join(CSV_PATH, 'p' + str(i) + '.csv'), index_col=0)
    # display(p)
    sum = [0] * len(x)
    for j in range(NUM_OF_TRIALS):
        sum += p['trial-' + str(j)]
    y.extend(sum / NUM_OF_TRIALS)
    # print(x)
# print(y)
# print(len(x))

# %%
# Effect size of 'r'
# small size : 0.1
# medium size: 0.3
# large size : 0.5
slope, intercept, rvalue, pvalue, stderr = stats.linregress(x * NUM_OF_PARTICIPANTS, y)
print('r={:.5f}, p={:.5f}'.format(rvalue, pvalue))

# %%
plt.figure(figsize=(7, 5))

# Plot data
plt.plot(x * NUM_OF_PARTICIPANTS, y, 'o', alpha=0.4)
plt.xlabel('Cube size', fontsize=14)
plt.ylabel('Perceived size', fontsize=14)

# Regression line
plt.plot(x, slope * np.array(x) + intercept, 'k')

plt.ylim(0, 2.0)

plt.savefig(os.path.join(OUTPUT_PATH, 'pacapa_crr.pdf'))
plt.show()

# %%
