import argparse
import os

import pandas as pd

def create_input(dirname):
    df = pd.read_csv(os.path.join(dirname, f"{dirname}.csv"))
    paras = []
    qs = []
    for index, row in df.iterrows():
        paras.append(row["context"].replace("\n", "") + ' [SEP] ' + row["answer"])
        qs.append(row["question"])

    f1 = open(os.path.join(dirname, f"{dirname}.txt"), "w", encoding="utf-8")
    f2 = open(os.path.join(dirname, f"{dirname}_q.txt"), "w", encoding="utf-8")
    f1.write('\n'.join(paras))
    f2.write('\n'.join(qs))
    f1.close()
    f2.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing script for causal question experiments')
    parser.add_argument('--dirname', type=str, help='Name of directory to process')
    args = parser.parse_args()
    if args.dirname:
        create_input(args.dirname)
