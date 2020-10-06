# %%
"""
# Chi^2 test
"""

# %%
import numpy as np
import pandas as pd
import scipy.stats as stats
import os

# %%
CSV_PATH = '../../../data/statistical_test/incendiary_reflection/chi-square/classified_face.csv'
NUM_OF_CLASSIFIED = 200
ALPHA = 0.05
columns = ['smiley face mirror', 'sad face mirror']
index = ['smile', 'neutral', 'sad']

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
# display(data.head())

# %%
smile_mirror_count = data['smiley face mirror'].value_counts()
sad_mirror_count = data['sad face mirror'].value_counts()
print(smile_mirror_count)
print(sad_mirror_count)

# %%
cross_data = pd.DataFrame(columns=columns, index=index)
cross_data[columns[0]] = [smile_mirror_count[1], 
                          smile_mirror_count[0],
                          smile_mirror_count[2]]
cross_data[columns[1]] = [sad_mirror_count[2], 
                          sad_mirror_count[0],
                          sad_mirror_count[1]]
print(cross_data)

# %%
result = stats.chi2_contingency(cross_data, correction=False)
print('chi^2({},N={})={:.2f}, p={:.5f}'.format(result[2], 20, result[0], result[1]))

# %%


# %%
