# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Command Line Interfaces (CLI) app >> Production >> Client
#Package

import argparse

my_parser = argparse.ArgumentParser(prog="MyApp", description= "Returns theaddition, multiplication, division and substraction of any two numbers." )

#def func(args, args)

my_parser.add_argument('arg1', help='The First Entry', type=int)
my_parser.add_argument('arg2', help='The Second Entry', type=int)

args = my_parser.parse_args()


input1 = args.arg1
input2 = args.arg2

print(f"The Summation is: {input1 + input2}")
print(f"The Substraction is: {input1 - input2}")
print(f"The Multiplication is: {input1 * input2}")
print(f"The Division is: {input1 / input2}")


print("done executing")

