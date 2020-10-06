# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

import glob
import csv

plt.style.use('seaborn-darkgrid')

# %%
CSV_PATH = '../../../data/psychophysics/constant'
OUTPUT_PATH = 'output/'
if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
HEADER = ['id', '10', '30', '50', '70', '90']
REPETITION = 4

# %%
ans_csvs = glob.glob(CSV_PATH + '/*.csv')
print('num of csvs: {}'.format(len(ans_csvs)))

# %%
def get_ans_series(ans_csv):
    with open(ans_csv) as f:
        reader = csv.reader(f)
        lines = [row for row in reader]
        # id = lines[0][1]
        ans_dict = {'10': 0, '30': 0, '50': 0, '70': 0, '90': 0}
        for i, ans in enumerate(lines[2]):
            sample_lightness = lines[1][i]
            if ans == 'sample':
                ans_dict[sample_lightness] += 1
        series = pd.Series(ans_dict)
        # print(series)
        series['id'] = lines[0][1]
    return series

# %%
ans_df = pd.DataFrame(columns=HEADER)
for ans_csv in ans_csvs:
    ans_series = get_ans_series(ans_csv)
    # print(id)
    # print(ans_series)
    ans_df = ans_df.append(ans_series, ignore_index=True)
ans_df

# %%
X = pd.Series([10, 30, 50, 70, 90])
Y = [ans_df['10'].mean(), ans_df['30'].mean(), ans_df['50'].mean(), ans_df['70'].mean(), ans_df['90'].mean()]
Y_norm = pd.Series(list(map(lambda x: x / REPETITION, Y)))
print(Y_norm)

# %%
# LogisticRegression().fit(X.values.reshape(1, -1), Y_norm.values.reshape(1, -1))
print(Y_norm.values.reshape(1, -1))
print(Y_norm.values.reshape(-1, 1))

# %%
plt.figure(figsize=(7, 5))
plt.plot(X, Y_norm, 'o')
plt.xlabel('Lightness of sample', fontsize=14)
plt.ylabel('Probability of lighenss (sample > reference)', fontsize=14)

plt.ylim(0, 1.0)
plt.savefig(os.path.join(OUTPUT_PATH, 'constant.pdf'))
plt.show()

# %%
