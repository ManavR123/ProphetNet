import argparse
import os

import pandas as pd

def process(inputdir):
    df = pd.read_csv(os.path.join(inputdir, f"{inputdir}.csv"))
    paras = []
    qs = []
    for index, row in df.iterrows():
        cause = row['Cause']
        effect = row['Effect']

        paras.append(row['Text'] + '[SEP] ' + cause)
        qs.append('nothing?')

        paras.append(row['Text'] + '[SEP] ' + effect)
        qs.append('nothing?')

    f1 = open(os.path.join(inputdir, f"{inputdir}.txt"), "w", encoding="utf-8")
    f2 = open(os.path.join(inputdir, f"{inputdir}_q.txt"), "w", encoding="utf-8")
    f1.write('\n'.join(paras))
    f2.write('\n'.join(qs))
    f1.close()
    f2.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--input', type=str, help='The path to the input file')
    args = parser.parse_args()
    if args.input:
        process(args.input)
