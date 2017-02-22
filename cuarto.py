#! /usr/bin/env python
# -*- coding: utf-8 -*-

def vocal (m):
    if m == "a" or m == "e" or m == "i" or m == "o" or m == "u":
        return True
    elif m == "A" or m == "E" or m == "I" or m == "O" or m == "U":
        return True
    else:
        return False

a=raw_input("ingrese una letra ")
print vocal(a)