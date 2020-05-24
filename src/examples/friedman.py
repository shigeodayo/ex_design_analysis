# %%
"""
# Freidman test
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
CSV_PATH = '../../data/examples/friedman_ex_data.csv'
ALPHA = 0.05
NUM_OF_PARTICIPANTS = 8
OUTPUT_PATH = 'output/'
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
datadata = pd.read_csv(CSV_PATH, index_col=0)
# data

# %%
# Compare groups
_, p = stats.friedmanchisquare(data['Standard'], data['Prediction'], data['Speech'])
print('p={:.5f}'.format(p))

if p > ALPHA:
    print('Same distributions')
    exit()
else:
    print('Different distributions. You can do a post-hoc test.')# Compare groups

# %%
"""
## Post-hoc test (Wilcoxon test)
P-value needs to be corrected to avoid multiplicity of statistical tests.

I use Bonferroni correction here.
"""

# %%
# Standard vs Prediction
_, p = stats.wilcoxon(data['Standard'], data['Prediction'])
print('Standard vs Prediction: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Prediction vs Speech
_, p = stats.wilcoxon(data['Prediction'], data['Speech'])
print('Prediction vs Speech: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Speech vs Standard
_, p = stats.wilcoxon(data['Speech'], data['Standard'])
print('Speech vs Standard: p={:.5f}'.format(p * 3))  # Bonferroni correction

# %%
"""
## Visualization
3 different data visualizations (Bar plot, Box plot, Violin plot)
"""

# %%
"""
### Bar plot (average & standard error)
pros: easy to compare multiple data (average)

cons: less informative (average and standard error)
"""

# %%
# Mean
standard_mu = data['Standard'].mean()
prediction_mu = data['Prediction'].mean()
speech_mu = data['Speech'].mean()

# Standard deviation
standard_sd = data['Standard'].std()
prediction_sd = data['Prediction'].std()
speech_sd = data['Speech'].std()

# Standard error
standard_se = standard_sd / np.sqrt(NUM_OF_PARTICIPANTS)
prediction_se = prediction_sd / np.sqrt(NUM_OF_PARTICIPANTS)
speech_se = speech_sd / np.sqrt(NUM_OF_PARTICIPANTS)

y = np.array([standard_mu, prediction_mu, speech_mu])
e = np.array([standard_se, prediction_se, speech_se])

x = np.array(["Standard", 'Prediction', 'Speech'])
x_position = np.arange(len(x))
error_bar_set = dict(lw=1, capthik=1, capsize=10)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x_position, y, yerr=e, tick_label=x, error_kw=error_bar_set, color=['salmon', 'palegreen', 'aqua'])
ax.set_xlabel('Conditions', fontsize=14)
ax.set_ylabel('Performance', fontsize=14)
ax.set_ylim(1, 5)

plt.savefig(os.path.join(OUTPUT_PATH, 'friedman_bar.pdf'))
plt.show()

# %%
"""
### Boxplot
pros:
more informative than bar plot

cons:
unable to understand the data distribution (box plot only show summary statistics)
"""

# %%
# error bar: min/max
# box: 25/50(median)/75 percentile
# circle: outlier (1.5 times bigger/smaller than box)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.boxplot([data['Standard'], data['Prediction'], data['Speech']], labels=['Standard', 'Prediction', 'Speech'])
ax.set_xlabel('Conditions', fontsize=14)
ax.set_ylabel('Performance', fontsize=14)
ax.set_ylim(1, 5)

plt.savefig(os.path.join(OUTPUT_PATH, 'friedmanfriedman_box.pdf'))
plt.show()

# %%
"""
### Violin plot
pros: more informative than box plot (beacuse violin plot represents data distribution)

cons:less popular (their meaning can be harder to grasp for many readers not familiar with the violin plot representation)
"""

# %%
# Similar to box plot, but also represents kernel density estimation (estimated distribution of data)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
sns.violinplot(data=[data['Standard'], data['Prediction'], data['Speech']], palette=['salmon', 'palegreen', 'aqua'])
ax.set_xticklabels(['Standard', 'Prediction', 'Speech'])
ax.set_xlabel('Conditions', fontsize=14)
ax.set_ylabel('Performance', fontsize=14)
ax.set_ylim(0, 5)

plt.savefig(os.path.join(OUTPUT_PATH, 'friedmanfriedman_violin.pdf'))
plt.show()

# %%
