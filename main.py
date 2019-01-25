import argparse
from diff_parser import DiffParser
from ast_parser import ASTParser


def main():
    if part == "1":
        print("Running Part 1 - Parsing diff files from... diffs/" + filename + "\n")
        diffParser = DiffParser()
        with open("diffs/" + filename) as file:
            diffParser.parse(file)



    elif part == "2":
        print("Running Part 2 - AST ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--part', required=True)
    parser.add_argument('-f', '--filename')
    args = parser.parse_args()
    part = args.part
    filename = args.filename
    main()