# %%
"""
# Parametric analysis with repeated data (ANOVA & Tukey-HSD)
Within-participant design (3 groups: smiley face, neutral face, sad face)

To use ANOVA, you need to make sure that the data fulfill these requirements:
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

# %matplotlib inline
plt.style.use('seaborn-darkgrid')

# %%
CSV_PATH = '../../data/creativity/n_idea.csv'
NUM_OF_PARTICIPANTS = 10
ALPHA = 0.05

# %%
data = pd.read_csv(CSV_PATH)
print(data)

# %%
"""
## Normality check
"""

# %%
_, p = stats.shapiro(data['smiley face'])
print('p={:.5f}'.format(p))
if p > ALPHA:
    print('Normality check: passed')
else:
    print('Normality check: rejected')

_, p = stats.shapiro(data['neutral'])
print('p={:.5f}'.format(p))
if p > ALPHA:
    print('Normality check: passed')
else:
    print('Normality check: rejected')

_, p = stats.shapiro(data['sad face'])
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
_, p = stats.bartlett(data['smiley face'], data['neutral'], data['sad face'])
if p > ALPHA:
    print('Sphericity check: passed')
else:
    print('Sphericity check: rejected')

# %%
"""
## ANOVA
"""

# %%
_, p = stats.f_oneway(data['smiley face'], data['neutral'], data['sad face'])
print('ANOVA: p={:.5f}'.format(p))

if p > ALPHA:
    print('Same distributions')
    exit()
else:
    print('Different distributions. You can do a post-hoc test.')

# %%
"""
## Multiple comparisons
There are several ways to do a multiple comparision (as a post-hoc test).

I use 'Tukey-HSD' and 't-test (with Bonferroni correction)' here.

You can use whichever you like.

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
tukey_hsd(['smiley face', 'neutral face', 'sad face'], data['smiley face'], data['neutral'], data['sad face'])

# %%
"""
### t-test (with Bonferroni correction)
"""

# %%
# Smiley face vs Neutral face
_, p = stats.ttest_rel(data['smiley face'], data['neutral'])
print('smile vs neutral: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Neutral face vs Sad face
_, p = stats.ttest_rel(data['neutral'], data['sad face'])
print('neutral vs sad: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Sad faec vs Smiley face
_, p = stats.ttest_rel(data['sad face'], data['smiley face'])
print('sad vs smile: p={:.5f}'.format(p * 3))  # Bonferroni correction

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
smile_mu = data['smiley face'].mean()
neutral_mu = data['neutral'].mean()
sad_mu = data['sad face'].mean()

# Standard deviation
smile_sd = data['smiley face'].std()
neutral_sd = data['neutral'].std()
sad_sd = data['sad face'].std()

# Standard error
smile_se = smile_sd / np.sqrt(NUM_OF_PARTICIPANTS)
neutral_se = neutral_sd / np.sqrt(NUM_OF_PARTICIPANTS)
sad_se = sad_sd / np.sqrt(NUM_OF_PARTICIPANTS)

y = np.array([smile_mu, neutral_mu, sad_mu])
e = np.array([smile_se, neutral_se, sad_se])

x = np.array(["Smiley face", 'Neutral face', 'Sad face'])
x_position = np.arange(len(x))
error_bar_set = dict(lw=1, capthik=1, capsize=10)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x_position, y, yerr=e, tick_label=x, error_kw=error_bar_set, color=['salmon', 'palegreen', 'aqua'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Number of ideas', fontsize=14)
ax.set_ylim(0, 18)

plt.savefig('creativity_bar.pdf')
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
ax.boxplot([data['smiley face'], data['neutral'], data['sad face']], labels=['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Number of ideas', fontsize=14)
ax.set_ylim(0, 18)

plt.savefig('creativity_boxplot.pdf')
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
sns.violinplot(data=[data['smiley face'], data['neutral'], data['sad face']], palette=['salmon', 'palegreen', 'aqua'])
ax.set_xticklabels(['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Number of ideas', fontsize=14)
ax.set_ylim(0, 18)

plt.savefig('creativity_violinplot.pdf')
plt.show()

# %%
