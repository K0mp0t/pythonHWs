import argparse
import os.path
import sys

parser = argparse.ArgumentParser(description="tail ubuntu command")
parser.add_argument("filenames", help="filenames", nargs='*', type=argparse.FileType('r'))

args = parser.parse_args()

if len(args.filenames) > 0:
    cumulative_ln = 0
    cumulative_wn = 0
    cumulative_bn = 0

    for filename in args.filenames:
        with open(filename.name, 'r') as f:
            lines = f.readlines()

        ln = len(lines)
        wn = len(' '.join(lines).split())
        bn = os.path.getsize(filename.name)

        print(f'{ln} {wn} {bn} {filename.name}')

        cumulative_ln += ln
        cumulative_wn += wn
        cumulative_bn += bn

    if len(args.filenames) > 1:
        print(f'{cumulative_ln} {cumulative_wn} {cumulative_bn} total')
else:
    lines = sys.stdin.readlines()

    print(f'{len(lines)} {len(" ".join(lines).split())} {len("".join(lines).encode("utf-8"))}')
