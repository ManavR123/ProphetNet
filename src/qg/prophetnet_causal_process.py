import argparse
import os

import pandas as pd

def process_input(dirname):
    df = pd.read_csv(os.path.join(dirname, f"{dirname}.csv"))
    paras = []
    qs = []
    for index, row in df.iterrows():
        cause = row['Cause']
        effect = row['Effect']

        paras.append(row['Text'] + ' [SEP] ' + cause)
        qs.append('nothing?')

        paras.append(row['Text'] + ' [SEP] ' + effect)
        qs.append('nothing?')

    f1 = open(os.path.join(dirname, f"{dirname}.txt"), "w", encoding="utf-8")
    f2 = open(os.path.join(dirname, f"{dirname}_q.txt"), "w", encoding="utf-8")
    f1.write('\n'.join(paras))
    f2.write('\n'.join(qs))
    f1.close()
    f2.close()


def process_output(dirname):
    f = open(os.path.join(dirname, f"{dirname}_output.txt"), 'r', encoding='utf8')
    qs = f.readlines()
    cause_qs = []
    effect_qs = []
    for i in range(0, len(qs), 2):
        cause_qs.append(qs[i])
        effect_qs.append(qs[i+1])
    df = pd.read_csv(os.path.join(dirname, f"{dirname}.csv"))
    df['cause_question'] = cause_qs
    df['effect_question'] = effect_qs
    df.to_csv(os.path.join(dirname, f"{dirname}.csv"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing script for causal question experiments')
    parser.add_argument('--dirname', type=str, help='Name of directory to process')
    parser.add_argument('--input', action="store_true", help='Process input?')
    parser.add_argument('--output', action="store_true", help='Process output?')
    args = parser.parse_args()
    if args.input:
        process_input(args.dirname)
    if args.output:
        process_output(args.dirname)
