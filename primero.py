#! /usr/bin/env python
# -*- coding: utf-8 -*-

def max (n1, n2):
    if n1 > n2:
        print n1
    elif n2 > n1:
        print n2
    else:
        print "Son iguales"

a=input("ingrese el primer valor ")
b=input("ingrese el segundo valor ")
max(a,b)