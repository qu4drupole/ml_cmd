import argparse

from parse_functions import predict_parser_func

def Main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands")

    
    predict_parser = subparsers.add_parser("predict", help = "Creat")
    predict_parser.add_argument("-p", "--img_path", type = str, help = "Directory to list")
    predict_parser.set_defaults(func = predict_parser_func)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    Main()
