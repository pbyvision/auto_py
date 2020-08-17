import argparse

parser = argparse.ArgumentParser(description="주민번호 탐색기")
parser.add_argument('--file', help='file name')
parser.add_argument('--sheet', type=int,  help='sheet 위치번호')
parser.add_argument('--col', help='Column 위치')

args = parser.parse_args()

print(args.file)
print(args.sheet)
print(args.col)
