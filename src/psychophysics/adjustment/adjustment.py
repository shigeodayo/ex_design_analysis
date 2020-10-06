import glob
import csv

CSV_PATH = '../../../data/psychophysics/adjustment'

def main():
    answer_csvs = glob.glob(CSV_PATH + '/*.csv')
    print('num of csvs: {}'.format(len(answer_csvs)))

    part_avg_ans = [0] * len(answer_csvs)
    for i, answer_csv in enumerate(answer_csvs):
        id, part_avg_ans[i] = get_avg_ans(answer_csv)
        print('{} (avg): {:.2f}'.format(id, part_avg_ans[i]))

    print('PSE = {:.2f}%'.format(sum(part_avg_ans) / len(part_avg_ans)))


def get_avg_ans(answer_csv):
    with open(answer_csv) as f:
        reader = csv.reader(f)
        lines = [row for row in reader]
        id = lines[0][1]
        sum = 0
        # print(lines[2])
        for ans in lines[2]:
            sum += int(ans)
        return id, sum / len(lines[2])


if __name__ == '__main__':
    main()
