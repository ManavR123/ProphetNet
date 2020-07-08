from pytorch_transformers import BertTokenizer
import argparse


def bert_uncased_tokenize(fin, fout):
    fin = open(fin, 'r', encoding='utf-8')
    fout = open(fout, 'w', encoding='utf-8')
    tok = BertTokenizer.from_pretrained('bert-base-uncased')
    for line in fin:
        word_pieces = tok.tokenize(line.strip())
        new_line = " ".join(word_pieces)
        fout.write('{}\n'.format(new_line))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--input', type=str, help='The path to the input file \
        or directory')
    args = parser.parse_args()
    out = args.input.split('/')
    out[-1] = 'tokenized_' + out[-1]
    outfile = '/'.join(out)
    if args.input:
        bert_uncased_tokenize(args.input, outfile)

