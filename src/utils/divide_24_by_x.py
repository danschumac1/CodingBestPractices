

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('numbers', type=int, help='an integer for the accumulator')
args = parser.parse_args()

def main():
    print("24 divided by your number is", 24/args.numbers)

if __name__ == "__main__":
    main()