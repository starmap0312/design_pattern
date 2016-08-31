import configparser

parser = configparser.ConfigParser()
parser._interpolation = configparser.ExtendedInterpolation()
parser.read("example.ini")

print(parser.sections())
print(parser.get('SectionTwo', 'Param1'))
print(parser.get('SectionThree', 'Charlie'))
