import argparse
uncompressed_list=[2,3,4,5,2,1,3,5,7]

def delta_compression(uncompressed_list):
    uncompressed_list=[int(x) for x in uncompressed_list]
    compressed_list=[]
    prev_value=0
    for i in uncompressed_list:
        compressed_list.append(i-prev_value)
        prev_value=i

    print(f"The compressd list is {compressed_list}")

def delta_decompression(compressed_list):
    compressed_list=[int(x) for x in compressed_list]
    uncompressed_list=[]
    prev_value=0
    for i in compressed_list:
        curr_value=i+prev_value
        uncompressed_list.append(curr_value)
        prev_value=curr_value

    print(f"The uncompressed list is {uncompressed_list}")

def get_parser():
    argparser=argparse.ArgumentParser(description="Command Line Utility to demonstrate the delta compression")
    argsubparser=argparser.add_subparsers(title="Commands",dest="command",required=True)
    args=argsubparser.add_parser("compression",
                                help="To do the delta compression")
    args.add_argument("compression",
                      nargs="+",
                      help="Provide the list")
    args=argsubparser.add_parser("decompression",
                                 help="To do the delta decompression")
    args.add_argument("decompression",
                      nargs="+",
                      help="Provide the list")
    
    return argparser

def main(argv=None):
    parser=get_parser()
    args=parser.parse_args(argv)
    match args.command:
        case "compression":delta_compression(args.compression)
        case "decompression":delta_decompression(args.decompression)
        case _:raise Exception(f"INVALID COMMAND {args.command}")

if __name__=="__main__":
    main()


