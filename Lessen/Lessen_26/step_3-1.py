import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to input file')
parser.add_argument('--output', help='Path to output file')
args = parser.parse_args()

print(args.input)
print(args.output)
