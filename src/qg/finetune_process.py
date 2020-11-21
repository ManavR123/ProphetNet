import argparse
import os

import pandas as pd
from sklearn.model_selection import train_test_split


def create_input(dirname):
    df = pd.read_csv(os.path.join(dirname, f"{dirname}.csv"))
    paras = []
    qs = []
    for index, row in df.iterrows():
        paras.append(row["context"].replace("\n", "") + " [SEP] " + row["answer"])
        qs.append(row["question"])

    train_paras, train_qs, valid_paras, valid_qs = train_test_split(
        paras, qs, test_size=0.25, random_state=42
    )

    f1 = open(os.path.join(dirname, f"train_{dirname}.txt"), "w", encoding="utf-8")
    f2 = open(os.path.join(dirname, f"train_{dirname}_q.txt"), "w", encoding="utf-8")
    f1.write("\n".join(train_paras))
    f2.write("\n".join(train_qs))
    f1.close()
    f2.close()

    f1 = open(os.path.join(dirname, f"valid_{dirname}.txt"), "w", encoding="utf-8")
    f2 = open(os.path.join(dirname, f"valid_{dirname}_q.txt"), "w", encoding="utf-8")
    f1.write("\n".join(valid_paras))
    f2.write("\n".join(valid_qs))
    f1.close()
    f2.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Processing script for causal question experiments"
    )
    parser.add_argument("--dirname", type=str, help="Name of directory to process")
    args = parser.parse_args()
    if args.dirname:
        create_input(args.dirname)
