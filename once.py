#! /usr/bin/env python
# -*- coding: utf-8 -*-

def digitos(n):
    indice=1
    while n>9:
        n=n/10
        indice +=1
    print indice

a=input("ingrese el numero ")
digitos(a)