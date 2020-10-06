# %%
"""
# One-way ANOVA (and normality / sphericity check)

To use ANOVA, you need to make sure that the data fulfill these requirements:
- Normality
- Homogeneity of variances / SphericityTo use ANOVA, you need to make sure that the data fulfill these requirements:
- Normality
- Homogeneity of variances / Sphericity
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# %matplotlib inline
plt.style.use('seaborn-darkgrid')

# %%
CSV_PATH = '../../../data/statistical_test/examples/one-way_ANOVA_ex_data.csv'
ALPHA = 0.05
NUM_OF_PARTICIPANTS = 8
OUTPUT_PATH = 'output/'
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
data

# %%
"""
## Normality check
"""

# %%
_, p = stats.shapiro(data['Standard'])

print('p={:.5f}'.format(p))
if p > ALPHA:
    print('Normality check: passed')
else:
    print('Normality check: rejected')

_, p = stats.shapiro(data['Prediction'])
print('p={:.5f}'.format(p))
if p > ALPHA:
    print('Normality check: passed')
else:
    print('Normality check: rejected')

_, p = stats.shapiro(data['Speech'])
print('p={:.5f}'.format(p))
if p > ALPHA:
    print('Normality check: passed')
else:
    print('Normality check: rejected')

# %%
"""
## Homogeneity of variances / Sphericity check
"""

# %%
_, p = stats.bartlett(data['Standard'], data['Prediction'], data['Speech'])
print('p={:.5f}'.format(p))
if p > ALPHA:
    print('Sphericity check: passed')
else:
    print('Sphericity check: rejected')

# %%
"""
## One-way ANOVA
"""

# %%
_, p = stats.f_oneway(data['Standard'], data['Prediction'], data['Speech'])
print('ANOVA: p={:.5f}'.format(p))

if p > ALPHA:
    print('Same distributions')
    # exit()
else:
    print('Different distributions. You can do a post-hoc test.')

# %%
"""
## Multiple comparisons
No significant difference is found on this data, thus no need to conduct a post-hoc test. 

But, as an example, I’ll show you a post-hoc test with this data.
"""

# %%
"""
### Tukey-HSD
"""

# %%
# https://qiita.com/TaigaU121/items/12c480f51a026ca9f333
def tukey_hsd(ind, *args):
    data_arr = np.hstack( args ) 

    ind_arr = np.array([])
    for x in range(len(args)):
        ind_arr = np.append(ind_arr, np.repeat(ind[x], len(args[x]))) 
    print(pairwise_tukeyhsd(data_arr,ind_arr))

# %%
tukey_hsd(['Standard', 'Prediction', 'Speech'], data['Standard'], data['Prediction'], data['Speech'])

# %%
"""
### t-test (with Bonferroni correction)
t-test can be used for multiple comparisions, but p-value needs to be corrected to avoid multiplicity of statistical tests.

i.e. if you done a statistical test with 95% confidence 3 times, the confidence of the results is 0.95 x 0.95 x 0.95 = 0.857375.
"""

# %%
# Standard vs Prediction
_, p = stats.ttest_rel(data['Standard'], data['Prediction'])
print('Standard vs Prediction: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Prediction vs Speech
_, p = stats.ttest_rel(data['Prediction'], data['Speech'])
print('Prediction vs Speech: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Speech vs Standard
_, p = stats.ttest_rel(data['Speech'], data['Standard'])
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
ax.set_ylim(0, 350)

plt.savefig(os.path.join(OUTPUT_PATH, 'ANOVA_bar.pdf'))
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
ax.set_ylim(0, 370)

plt.savefig(os.path.join(OUTPUT_PATH, 'ANOVA_box.pdf'))
plt.show()

# %%
"""
### Violin plot
pros: more informative than box plot (beacuse violin plot represents data distribution)

cons:less popular (their meaning can be harder to grasp for many readers not familiar with the violin plot representation)### Violin plot
"""

# %%
# Similar to box plot, but also represents kernel density estimation (estimated distribution of data)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
sns.violinplot(data=[data['Standard'], data['Prediction'], data['Speech']], palette=['salmon', 'palegreen', 'aqua'])
ax.set_xticklabels(['Standard', 'Prediction', 'Speech'])
ax.set_xlabel('Conditions', fontsize=14)
ax.set_ylabel('Performance', fontsize=14)
ax.set_ylim(0, 400)

plt.savefig(os.path.join(OUTPUT_PATH, 'ANOVA_violin.pdf'))
plt.show()

# %%
