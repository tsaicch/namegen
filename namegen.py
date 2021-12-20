import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='my description')
    parser.add_argument('cloudProvider', type=str)
    parser.add_argument('env', type=str)
    parser.add_argument('resourceType', type=str)
#    parser.add_argument('resourceNum', type=int)
    return parser
def get_parser2():
    parser = argparse.ArgumentParser(description='my description')
    parser.add_argument('-cp', '--cloudprovider', type=str)
    parser.add_argument('-env', '--environment', type=str)
    parser.add_argument('-rt', '--resourcetype', type=str)
#    parser.add_argument('resourceNum', type=int)
    return parser

if __name__ == '__main__':
    cloudProviderMap={"google":"g","azure":"a","awx":"w"}
    envMap={"production":"p", "uat":"u", "dev":"d"}
    resourcerMap={"computing_engine":"vm","cloud_storage":"csg","cloud_network":"cng"}
    
    parser = get_parser2()
    args = parser.parse_args()
    a=cloudProviderMap[args.cloudprovider]
    b=envMap[args.environment]
    c=resourcerMap[args.resourcetype]
    print(a + b + c)
