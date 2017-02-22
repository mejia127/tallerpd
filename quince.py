#! /usr/bin/env python
# -*- coding: utf-8 -*-

def par_impar(n):
    ind=0
    while n>0:
        r=n%10
        ind= ind+r
        n=n/10
    if (ind%2==0):
        print ("la suma es par y tiene " + str(ind) + "digitos")
    else:
        print ("la suma es impar y tiene " + str(ind) + "digitos")

a=input("ingrese el valor ")
par_impar(a)