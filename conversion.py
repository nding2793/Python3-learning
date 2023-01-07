"""
@author: Nan Ding
@desc: conversion hex binary
"""

print("Please input a number for conversion, or q to quit")

while True:
    value = input("Please input a number > 0: __\b\b")
    
    if value == "q":
        break
        
    base = input("Please input \"bin\" or \"hex\": ___\b\b\b")
    value = int(value)
    
    if base == "q":
        break
    elif base == "bin":
        print(bin(value))
    elif base == "hex":
        print(hex(value))
         
