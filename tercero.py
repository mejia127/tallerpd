#! /usr/bin/env python
# -*- coding: utf-8 -*-

def long_cad(lista):
    cont=0
    for i in lista:
        cont=cont+1
    return cont

a=raw_input("ingrese el texto ")
print (long_cad(a))