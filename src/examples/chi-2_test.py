# %%
"""
## Chi^2 test
"""

# %%
import pandas as pd
import scipy.stats as stats

# %%
CSV_PATH = '../../data/examples/chi-2_ex_data.csv'

# %%
data = pd.read_csv(CSV_PATH, index_col=0)
# data

# %%
result = stats.chi2_contingency(data, correction=False)
print('chi^2({})={:.5f}, p={:.5f}'.format(result[2],result[0], result[1]))

# %%


# %%
