#! /usr/bin/env python
# -*- coding: utf-8 -*-

def superposicion(f,n):
    for i in f:
        for m in n:
            if i==m:
                return True
    return False

a=raw_input("ingrese la primera palabra ")
b=raw_input("ingrese la segunda palabra ")
print superposicion(a,b)