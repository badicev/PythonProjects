# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Command Line Interfaces (CLI) app >> Production >> Client
#Package

import argparse

my_parser = argparse.ArgumentParser(prog="MyApp", description= "Returns theaddition, multiplication, division and substraction of any two numbers." )

#fromfile_prefix_chars="@"   ---for external arguments @args.txt

#def func(args, args)

my_parser.add_argument('arg1', help='The First Entry', type=int)
my_parser.add_argument('arg2', help='The Second Entry', type=int)
my_parser.add_argument('--arg3', help=" Shift Optional Arg", type=int) #optional argument
my_parser.add_argument('--arg4', help=" Shift Optional Arg", action='store_true') 
args = my_parser.parse_args()


input1 = args.arg1
input2 = args.arg2
input3 = args.arg3
input4 = args.arg4


if input3 == None:
    shift = 5
else:
    shift = input3


shift = 5
print(f"The Summation is: {input1 + input2 + shift}")
print(f"The Substraction is: {input1 - input2 + shift}")
print(f"The Multiplication is: {input1 * input2 + shift}")
print(f"The Division is: {input1 / input2 + shift}")
if input4 == True:
    print(f"The power of 2 of the first argument: {input1*input1}")


print("done executing")

