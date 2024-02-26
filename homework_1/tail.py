import argparse
import sys
from collections import deque

parser = argparse.ArgumentParser(description="tail ubuntu command")
parser.add_argument("filenames", help="filenames", nargs='?', type=argparse.FileType('r'))

args = parser.parse_args()

if args.filenames is not None:
    for filename in args.filenames:
        if len(args.filenames) > 1:
            print(f'==> {filename.name} <==')

        with open(filename.name, 'r') as f:
            q = deque(f, 10)

            for line in q:
                print(line, end='')
else:
    q = deque(sys.stdin, 17)

    for line in q:
        print(line, end='')
