#! /usr/bin/env python
# -*- coding: utf-8 -*-

def tabla(a):

    for j in range(1,13):
        n=a*j
        print (str(a)+"*"+str(j)+" = "+str(n))


multiplicador = int(input("Cual tabla de multiplicar deseas conocer "))

tabla(multiplicador)
