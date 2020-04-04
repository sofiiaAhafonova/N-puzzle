import argparse
from parser import parse
from a_star import AStar, Heuristic


def main():
    parser = argparse.ArgumentParser(description='Solve N-puzzle')
    parser.add_argument("-f", "--filename", help="A file with puzzle", type=str, required=True)
    args = parser.parse_args()
    try:
        puzzle, size = parse(args.filename)
    except Exception as e:
        print(e)
    else:
        a_star = AStar(Heuristic.MANHATTAN, puzzle, size)
        a_star.solve_puzzle()
        a_star.print_puzzle()
        a_star.print_eval()


if __name__ == '__main__':
    main()
