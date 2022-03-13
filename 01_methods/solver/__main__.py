from argparse import ArgumentParser
from fractions import Fraction

from . import functions, methods


parser = ArgumentParser()
parser.add_argument("--method", help="method name [piyavski, strongin]")
parser.add_argument("--param", help="method parameter")
parser.add_argument("--xfrom", help="left x boundary")
parser.add_argument("--xto", help="right x boundary")
parser.add_argument("--tests", help="number of tests", type=int)
args = parser.parse_args()


if args.method not in methods.METHODS:
    print("Method not found")
    exit(1)

func = functions.BaseFunction()
param = Fraction(args.param)
method = methods.METHODS[args.method](param)

print("Method:", args.method)
x_all = []
for x_next in method.solve(Fraction(args.xfrom), Fraction(args.xto), func, args.tests):
    x_all.append(x_next)
    print("x", x_next)
    print()
print(*x_all)
