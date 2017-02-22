#! /usr/bin/env python
# -*- coding: utf-8 -*-

def max_tres (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print n1
    elif n2 > n1 and n2 > n3:
        print n2
    elif n3 > n2 and n3 > n1:
        print n3
    else:
        print "Son iguales"

a=input("ingrese el primer valor ")
b=input("ingrese el segundo valor ")
c=input("ingrese el tercer valor ")
max_tres(a,b,c)