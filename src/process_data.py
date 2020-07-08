from pytorch_transformers import BertTokenizer
import tqdm
import argparse


def convert_cased2uncased(fin, fout):
    fin = open(fin, 'r', encoding='utf-8')
    fout = open(fout, 'w', encoding='utf-8')
    tok = BertTokenizer.from_pretrained('bert-base-uncased')
    for line in tqdm.tqdm(fin.readlines()):
        org = line.strip().replace(" ##", "")
        new = tok.tokenize(org)
        new_line = " ".join(new)
        fout.write('{}\n'.format(new_line))


def convert_cased2uncased_reverse(fin, fout):
    fin = open(fin, 'r', encoding='utf-8')
    fout = open(fout, 'w', encoding='utf-8')
    tok = BertTokenizer.from_pretrained('bert-base-uncased')
    for line in tqdm.tqdm(fin.readlines()):
        org = line.strip().replace(" ##", "").split("[SEP]")
        try:
            ans = tok.tokenize(org[1].strip())
        except:
            print(line)
            print(org)
        par = tok.tokenize(org[0].strip())[:510 - len(ans)] # at most 512 tokens can be fed to our model
        par = " ".join(par)
        ans = " ".join(ans)
        fout.write('{} [SEP] {}\n'.format(ans, par))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--input', type=str, help='The path to the input file \
        or directory')
    parser.add_argument('--output', type=str, help='The path to the output file \
        or directory')
    parser.add_argument('--tgt', action='store_true', help='tgt file')
    parser.add_argument('--src', action='store_true', help='tgt file')
    args = parser.parse_args()
    
    if args.tgt:
        convert_cased2uncased(args.input, args.output)
    elif args.src:
        convert_cased2uncased_reverse(args.input, args.output)

