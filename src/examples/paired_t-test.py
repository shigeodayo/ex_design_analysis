# %%
"""
# paired t-test
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats

# %%
CSV_PATH = '../../data/examples/paired_t_ex_data.csv'
ALPHA = 0.05
NUM_OF_PARTICIPANTS = 8

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
data

# %%
_, p = stats.ttest_rel(data['No Prediction'], data['With Prediction'])
print('No Predicition vs With Predicition: p={:.5f}'.format(p))
if p < ALPHA:
    print('Significant difference')
else:
    print('No significant difference')

# %%
