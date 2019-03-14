import configparser

parser=configparser.ConfigParser()
parser.read("test_config.cfg")
if(parser.get("RunSettings","ENVIRONMENT")=="ProdEnvironment"):
    print(parser.get('ProdEnvironment','user'))
if(parser.get("RunSettings","ENVIRONMENT")=="UATEnvironment"):
    print(parser.get('UATEnvironment','user'))

#JSON - Run time
#kankishore@gmail.com