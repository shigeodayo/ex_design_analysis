# %%
"""
## Confusion Matrix (PaCaPa: Study 2)
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

# %matplotlib inline
plt.style.use('seaborn-darkgrid')

# %%
CSV_PATH = '../../data/pacapa/study-2'
NUM_OF_PARTICIPANTS = 12
OUTPUT_PATH = 'output/pacapa/study-2'
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
columns = ['Square (1,1)', 'Square (1.25,0.75)', 'Square (0.75,1.25)',
         'Circle (1,1)', 'Circle (1.25,0.75)', 'Circle (0.75,1.25)',
         'Triangle (1,1)', 'Triangle (1.25,0.75)', 'Triangle (0.75,1.25)']

# %%
data = pd.DataFrame(columns=columns, index=columns)
data = data.fillna(0)
# data

# %%
# Read csv files
for i in range(NUM_OF_PARTICIPANTS):
    p = pd.read_csv(CSV_PATH + '/p' + str(i) + '.csv', index_col=0)
    # display(p)
    data = data.add(p)
# display(data)

# %%
data = 100 * data / 12
vmin = 0
vmax = 100  # 12

# %%
sns.heatmap(data.T, annot=True, cmap='Blues', vmin=vmin, vmax=vmax)
plt.ylabel('True shape')
plt.xlabel('Predicted shape')

plt.savefig(os.path.join(OUTPUT_PATH, 'pacapa_cm.pdf'), dpi=350, bbox_inches='tight', pad_inches=0.1)
plt.show()

# %%
