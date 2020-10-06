# %%
"""
# Correlation
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
CSV_PATH = '../../../data/statistical_test/examples/correlation_ex_data.csv'
OUTPUT_PATH = 'output/'
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
x = data['Computer Experience']
data


# %%
y_s = data['Standard']
slope_s, intercept_s, rvalue_s, pvalue_s, stderr_S = stats.linregress(x, y_s)
print('r={:.5f}, p={:.5f}'.format(rvalue_s, pvalue_s))

# %%
y_p = data['Prediction']
slope_p, intercept_p, rvalue_p, pvalue_p, stderr_p = stats.linregress(x, y_p)
print('r={:.5f}, p={:.5f}'.format(rvalue_p, pvalue_p))

# %%
plt.figure(figsize=(7, 5))

# Plot data (Standard)
plt.plot(x, y_s, 'bo', alpha=0.4)
# Regression line
plt.plot(x, slope_s * np.array(x) + intercept_s, 'b')

# Plot data (Prediction)
plt.plot(x, y_p, 'ro', alpha=0.4)
# Regression line
plt.plot(x, slope_p * np.array(x) + intercept_p, 'r')

plt.xlabel('Computer Experience', fontsize=14)
plt.ylabel('Performance', fontsize=14)
plt.ylim(0, 350)

plt.savefig(os.path.join(OUTPUT_PATH, 'correlation.pdf'))
plt.show()

# %%
