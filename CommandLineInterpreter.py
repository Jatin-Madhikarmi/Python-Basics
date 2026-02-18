import sys
import argparse

def get_parser():
   
    parser=argparse.ArgumentParser(description="Command Line Utility")
    subparser=parser.add_subparsers(title="Commands",dest="command",required=True)

    subparser.add_parser("main",help="Entering the main function")

    addsubparser=subparser.add_parser("add",help="Add functions to add only two numbers")

    addsubparser.add_argument("num1",type=int,help="Number 1")
    addsubparser.add_argument("num2",type=int,help="Number 2")

    return parser

def cmd_main(args):
    print("Entered the main function sucessfully")

def cmd_add(args):
    print("Entered the add function sucessfully")
    print(type(args))
    print(f"The resulting number is {args.num1 + args.num2}")
def main(argv=None):
    parser=get_parser()
    args=parser.parse_args(argv)

    match args.command:
        case "add":cmd_add(args)
        case "main":cmd_main(args)
        case _:raise Exception("Invalid command")

if __name__=="__main__":
    main()