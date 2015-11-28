"""
Exercise to demonstrate facility with python
Challenge is to implement an elevator path planning framework
"""

import sys


def readcommands(inputfile) -> object:
    print(inputfile)
    with open(inputfile) as f:
        content = f.readlines()
    for cmd in content:
        print(cmd)
    return content


def main(argv):
    inputfile = ''
    mode = ''
    if len(sys.argv) > 2:
        print(sys.argv[1])
        inputfile = sys.argv[1]
        print(sys.argv[2])
        mode = sys.argv[2]
        readcommands(inputfile)

#


if __name__ == "__main__":
    main(sys.argv[1:])

