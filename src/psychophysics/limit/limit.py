import glob
import csv

# You can try the 'method of limit' from the link below:
# https://shigeodayo.github.io/PsychophysicsWebExp/index.html
CSV_PATH = '../../../data/psychophysics/limit'  # Put the experimental data (CSVs) in this directory.
HALF_STEP = 0.5  # the half of the step to increase/decrease the lightness, the unit is '%'

def main():
    answer_csvs = glob.glob(CSV_PATH + '/*.csv')
    print('num of csvs: {}'.format(len(answer_csvs)))

    part_avg_ans_up = [0] * len(answer_csvs)
    part_avg_ans_down = [0] * len(answer_csvs)
    part_avg_ans = [0] * len(answer_csvs)
    for i, answer_csv in enumerate(answer_csvs):
        id, part_avg_ans_up[i], part_avg_ans_down[i] = get_avg_ans(answer_csv)
        part_avg_ans[i] = (part_avg_ans_up[i] + part_avg_ans_down[i]) / 2
        print('{} (avg): {:.2f} (up) - {:.2f} (down)'.format(id, part_avg_ans_up[i], part_avg_ans_down[i]))

    print('------------------------------------------------')
    print('PSE = {:.2f}%'.format(sum(part_avg_ans) / len(part_avg_ans)))
    print('------------------------------------------------')


def get_avg_ans(answer_csv):
    with open(answer_csv) as f:
        reader = csv.reader(f)
        lines = [row for row in reader]
        id = lines[0][1]
        sum_up = 0
        sum_down = 0
        # print(lines[2])
        for i in range(len(lines[1])):
            if lines[1][i] == 'up':
                sum_up += int(lines[2][i]) - HALF_STEP
            else:
                sum_down += int(lines[2][i]) + HALF_STEP
        return id, (sum_up / lines[1].count('up')), (sum_down / lines[1].count('down'))


if __name__ == '__main__':
    main()
