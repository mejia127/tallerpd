#! /usr/bin/env python
# -*- coding: utf-8 -*-

def mas_larga(lista):
    a=raw_input("Ingrese otra palabra ")

    for i in lista:
        if len(lista) > len(a):
            mas_larga = lista
        else:
            mas_larga=a

    return mas_larga

a=raw_input("ingrese una palabra ")
print mas_larga(a)