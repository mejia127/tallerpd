#! /usr/bin/env python
# -*- coding: utf-8 -*-

def decimal(binario):
    binario = str(binario)
    decimal = 0
    exp = len (binario) -1
    for i in binario:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
    return decimal

a=input("ingrese un numero binario ")
print decimal(a)