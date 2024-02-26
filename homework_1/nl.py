import argparse
import sys

parser = argparse.ArgumentParser(description="nl -b a ubuntu command")
parser.add_argument("filename", help="filename", nargs='?', type=argparse.FileType('r'),
                    default=(None if sys.stdin.isatty() else sys.stdin))

args = parser.parse_args()

linenum = 1

if args.filename.name != '<stdin>':
    with open(args.filename.name, 'r') as f:
        line = f.readline()

        while line is not None and line.strip() != '':
            print(f'\t{linenum} {line}', end='')
            line = f.readline()
            linenum += 1

else:
    line = sys.stdin.readline()

    while line is not None and line.strip() != '':
        print(f'\t{linenum} {line}', end='')
        line = sys.stdin.readline()
        linenum += 1
