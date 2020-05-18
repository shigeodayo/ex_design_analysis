# %%
"""
# PANAS with non-parametric analysis (Wilcoxon)
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
# Smiley face vs Neutral face
_, p = stats.wilcoxon(smile_pos, neutral_pos)
print('{:.5f}'.format(p * 3))  # Bonferroni correction

# Neutral face vs Sad face
_, p = stats.wilcoxon(neutral_pos, sad_pos)
print('{:.5f}'.format(p * 3))  # Bonferroni correction

# Sad face vs Smiley face
_, p = stats.wilcoxon(sad_pos, smile_pos)
print('{:.5f}'.format(p * 3))  # Bonferroni correction

# %%
"""
## Negative affect
"""

# %%
# Smiley face vs Neutral face
_, p = stats.wilcoxon(smile_neg, neutral_neg)
print('smile vs neutral: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Neutral face vs Sad face
_, p = stats.wilcoxon(neutral_neg, sad_neg)
print('neutral vs sad: p={:.5f}'.format(p * 3))  # Bonferroni correction

# Sad face vs Smiley face
_, p = stats.wilcoxon(sad_neg, smile_neg)
print('sad vs smile: p={:.5f}'.format(p * 3))  # Bonferroni correction

# %%
"""
## Boxplot
"""

# %%
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

plt.savefig('PANAS.pdf')
plt.show()

# %%
