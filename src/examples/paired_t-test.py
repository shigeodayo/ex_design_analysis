# %%
"""
# paired t-test
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# %%
CSV_PATH = '../../data/examples/paired_t_ex_data.csv'
ALPHA = 0.05
NUM_OF_PARTICIPANTS = 8

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
# data

# %%
"""
## Data Visualization
"""

# %%
# Mean
control_mu = data['No Prediction'].mean()
prediction_mu = data['With Prediction'].mean()

# Standard deviation
control_sd = data['No Prediction'].std()
prediction_sd = data['With Prediction'].std()

# Standard error
control_se = control_sd / np.sqrt(NUM_OF_PARTICIPANTS)
prediction_se = prediction_sd / np.sqrt(NUM_OF_PARTICIPANTS)

y = np.array([control_mu, prediction_mu])
e = np.array([control_se, prediction_se])

x = np.array(["No Prediction", 'With Prediction'])
x_position = np.arange(len(x))
error_bar_set = dict(lw=1, capthik=1, capsize=10)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x_position, y, yerr=e, tick_label=x, error_kw=error_bar_set, color=['salmon', 'aqua'])
ax.set_xlabel('Conditions', fontsize=14)
ax.set_ylabel('Performance', fontsize=14)
ax.set_ylim(0, 350)

plt.show()# Mean

# %%
"""
## Statistical analysis (t-test)
"""

# %%
_, p = stats.ttest_rel(data['No Prediction'], data['With Prediction'])
print('No Predicition vs With Predicition: p={:.5f}'.format(p))
if p < ALPHA:
    print('Significant difference')
else:
    print('No significant difference')

# %%
