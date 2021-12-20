import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='my description')
    parser.add_argument('ip', type=str)
    parser.add_argument('port', type=int)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    print(args.ip + ':' + str(args.port))
    print(type(args.ip))
    print(type(args.port))
