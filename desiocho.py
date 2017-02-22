#! /usr/bin/env python
# -*- coding: utf-8 -*-

def mayusculas (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower():
            cont += 1

    print "La cadena tiene "+ str(cont)+" mayusculas"


a=raw_input("ingrese una palabra ")
print mayusculas(a)

