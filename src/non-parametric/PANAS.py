# %%
"""
# Non-parametric analysis with repeated data (Friedman & Wilcoxon)
Within-participant design (3 groups: smiley face, neutral face, sad face)
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline
plt.style.use('seaborn-darkgrid')

# %%
CSV_PATH = '../../data/PANAS'
NUM_OF_PARTICIPANTS = 20
ALPHA = 0.05

# %%
smile_pos = []
neutral_pos = []
sad_pos = []

smile_neg = []
neutral_neg = []
sad_neg = []

# %%
for i in range(NUM_OF_PARTICIPANTS):
    data = pd.read_csv(CSV_PATH + '/p' + str(i) + '.csv')

    # Calculate sum of positive/negative values of each participant, then append the sum to list
    smile_pos.append(data['smiley face'][:10].sum())
    neutral_pos.append(data['neutral'][:10].sum())
    sad_pos.append(data['sad face'][:10].sum())

    smile_neg.append(data['smiley face'][10:].sum())
    neutral_neg.append(data['neutral'][10:].sum())
    sad_neg.append(data['sad face'][10:].sum())

# %%
"""
## Positive affect
"""

# %%
"""
### Friedman test
"""

# %%
# Compare groups
_, p = stats.friedmanchisquare(smile_pos, neutral_pos, sad_pos)
print('p={:.5f}'.format(p))

if p > ALPHA:
    print('Same distributions')
    exit()
else:
    print('Different distributions. You can do a post-hoc test.')

# %%
"""
### Wilcoxon test (as a post-hoc test)
"""

# %%
# Smiley face vs Neutral face
_, p = stats.wilcoxon(smile_pos, neutral_pos)
print('smile vs neutral: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Neutral face vs Sad face
_, p = stats.wilcoxon(neutral_pos, sad_pos)
print('neutral vs sad: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Sad face vs Smiley face
_, p = stats.wilcoxon(sad_pos, smile_pos)
print('sad vs smile: p={:.5f}'.format(p * 3))  # Bonferroni correction

# %%
"""
## Negative affect
"""

# %%
"""
### Friedman test
"""

# %%
# Compare groups
_, p = stats.friedmanchisquare(smile_neg, neutral_neg, sad_neg)
print('p={:.5f}'.format(p))

if p > ALPHA:
    print('Same distributions')
    exit()
else:
    print('Different distributions. You can do a post-hoc test.')

# %%
"""
### Wilcoxon test (as a post-hoc test)
"""

# %%
# Smiley face vs Neutral face
s, p = stats.wilcoxon(smile_neg, neutral_neg)
print('smile vs neutral: p={:.5f}'.format(p * 3))  # Bonferroni correction
print(s)

# Neutral face vs Sad face
_, p = stats.wilcoxon(neutral_neg, sad_neg)
print('neutral vs sad: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Sad face vs Smiley face
_, p = stats.wilcoxon(sad_neg, smile_neg)
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
# Convert array to numpy array
smile_pos_np = np.array(smile_pos)
neutral_pos_np = np.array(neutral_pos)
sad_pos_np = np.array(sad_pos)
smile_neg_np = np.array(smile_neg)
neutral_neg_np = np.array(neutral_neg)
sad_neg_np = np.array(sad_neg)

# Mean
smile_pos_mu = smile_pos_np.mean()
neutral_pos_mu = neutral_pos_np.mean()
sad_pos_mu = sad_pos_np.mean()
smile_neg_mu = smile_neg_np.mean()
neutral_neg_mu = neutral_neg_np.mean()
sad_neg_mu = sad_neg_np.mean()

# Standard deviation
smile_pos_sd = smile_pos_np.std()
neutral_pos_sd = neutral_pos_np.std()
sad_pos_sd = sad_pos_np.std()
smile_neg_sd = smile_neg_np.std()
neutral_neg_sd = neutral_neg_np.std()
sad_neg_sd = sad_neg_np.std()

# Standard error
smile_pos_se = smile_pos_sd / np.sqrt(len(smile_pos))
neutral_pos_se = neutral_pos_sd / np.sqrt(len(neutral_pos))
sad_pos_se = sad_pos_sd / np.sqrt(len(sad_pos))
smile_neg_se = smile_neg_sd / np.sqrt(len(smile_neg))
neutral_neg_se = neutral_neg_sd / np.sqrt(len(neutral_neg))
sad_neg_se = sad_neg_sd / np.sqrt(len(sad_neg))

y_pos = np.array([smile_pos_mu, neutral_pos_mu, sad_pos_mu])
e_pos = np.array([smile_pos_se, neutral_pos_se, sad_pos_se])
y_neg = np.array([smile_neg_mu, neutral_neg_mu, sad_neg_mu])
e_neg = np.array([smile_neg_se, neutral_neg_se, sad_neg_se])

x = np.array(["Smiley face", 'Neutral face', 'Sad face'])
x_position = np.arange(len(x))
error_bar_set = dict(lw=1, capthik=1, capsize=10)

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 2, 1)
ax.bar(x_position, y_pos, yerr=e_pos, tick_label=x, error_kw=error_bar_set, color=['salmon', 'palegreen', 'aqua'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Positive affect', fontsize=14)
ax.set_ylim(10, 50)

ax = fig.add_subplot(1, 2, 2)
ax.bar(x_position, y_neg, yerr=e_neg, tick_label=x, error_kw=error_bar_set, color=['salmon', 'palegreen', 'aqua'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Negative affect', fontsize=14)
ax.set_ylim(10, 50)

plt.savefig('PANAS_bar.pdf')
plt.show()

# %%
"""
### Box plot
pros:
more informative than bar plot

cons:
unable to understand the data distribution (box plot only show summary statistics)
"""

# %%
# error bar: min/max
# box: 25/50(median)/75 percentile
# circle: outlier (1.5 times bigger/smaller than box)
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 2, 1)
ax.boxplot([smile_pos, neutral_pos, sad_pos], labels=['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Positive affect', fontsize=14)
ax.set_ylim(10, 50)

ax = fig.add_subplot(1, 2, 2)
ax.boxplot([smile_neg, neutral_neg, sad_neg], labels=['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Negative affect', fontsize=14)
ax.set_ylim(10, 50)

plt.savefig('PANAS_boxplot.pdf')
plt.show()

# %%
"""
### Violin plot
pros: more informative than box plot (beacuse violin plot represents data distribution)

cons:less popular (their meaning can be harder to grasp for many readers not familiar with the violin plot representation)

"""

# %%
# Similar to box plot, but also represents kernel density estimation (estimated distribution of data)
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 2, 1)
sns.violinplot(data=[smile_pos, neutral_pos, sad_pos], palette=['salmon', 'palegreen', 'aqua'])
ax.set_xticklabels(['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Positive affect', fontsize=14)
ax.set_ylim(10, 50)

ax = fig.add_subplot(1, 2, 2)
sns.violinplot(data=[smile_neg, neutral_neg, sad_neg], palette=['salmon', 'palegreen', 'aqua'])
ax.set_xticklabels(['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Negative affect', fontsize=14)
ax.set_ylim(10, 50)

plt.savefig('PANAS_violinplot.pdf')
plt.show()


# %%
