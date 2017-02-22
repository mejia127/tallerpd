#! /usr/bin/env python
# -*- coding: utf-8 -*-

def es_bisiesto(a):


    if a % 4 == 0 and (not(a % 100 == 0)):
        print "El ano", a, "es un ano bisiesto porque es multiplo de 4"
    elif a % 400 == 0:
        print "El ano", a, "es un ano bisiesto porque es multiplo de 400"
    else:
        print "El ano", a, "no es bisiesto"

print "Comprobacion de un ano bisiesto"
b = input ("Escriba un ano y le dire si es bisiesto: ")

es_bisiesto(b)