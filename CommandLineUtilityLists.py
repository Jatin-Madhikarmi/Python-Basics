import argparse


def get_parser():
    parser=argparse.ArgumentParser(description="Process a list of numbers followed by an integer through the command line utility")
    parser.add_argument("list_numbers",
                        nargs="+",
                        metavar="N",
                        type=int,
                        help="Process a list of numbers")
    parser.add_argument("last_number",
                        type=int,
                        help="Process the last integer value")
    return parser

def main(argv=None):
    parser=get_parser()
    args=parser.parse_args(argv)
    print(f"The list of number is {args.list_numbers}")
    print(f"The last number is {args.last_number}")

if __name__=="__main__":
    main()

    