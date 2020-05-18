# %%
"""
# Creativity with parametric analysis
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
CSV_PATH = '../../data/creativity/n_idea.csv'
NUM_OF_PARTICIPANTS = 10

# %%
data = pd.read_csv(CSV_PATH)
print(data)

# %%
"""
## ANOVA
"""

# %%
_, p = stats.f_oneway(data['smiley face'], data['neutral'], data['sad face'])
print('ANOVA: p={:.5f}'.format(p))

# %%
"""
## Multiple comparisons
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
## Boxplot
"""

# %%
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)
ax.boxplot([data['smiley face'], data['neutral'], data['sad face']], labels=['Smiley face', 'Neutral face', 'Sad face'])
ax.set_xlabel('Facial expression', fontsize=14)
ax.set_ylabel('Positive affect', fontsize=14)
ax.set_ylim(0, 15)

plt.savefig('creativity.pdf')
plt.show()

# %%
