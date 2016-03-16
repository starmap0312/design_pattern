# parse the arguments passed-in when executing the script
import sys
import argparse

args = sys.argv[1:]
parser = argparse.ArgumentParser()
parser.add_argument('var1', help='1st positional argument')
parser.add_argument('--varname', help='named argument varname')
parser.add_argument('var2', help='2nd positional argument', default = 0)
parsed_args = parser.parse_args(args)

# python test.py 1 --varname value two
#   Namespace(var1='1', var2='two', varname='value')
print(parsed_args)
