import argparse
import pandas as pd

def process(inputfile):
    df = pd.read_csv(inputfile)
    paras = []
    qs = []
    for index, row in df.iterrows():
        cause = row['Cause']
        effect = row['Effect']

        paras.append(row['Text'] + '[SEP] ' + cause)
        qs.append('nothing?')

        paras.append(row['Text'] + '[SEP] ' + effect)
        qs.append('nothing?')

    filename = ''.join(inputfile.split(".")[:-1])
    f1 = open(f"{filename}.txt", "w", encoding="utf-8")
    f2 = open(f"{filename}_q.txt", "w", encoding="utf-8")
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