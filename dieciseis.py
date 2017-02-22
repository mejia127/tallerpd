#! /usr/bin/env python
# -*- coding: utf-8 -*-

def digitos(n):
    ind = 1
    while n >=10:
        n = n / 10
        ind = ind + 1

        if ind%2==0:
            print ind



a=input("ingrese el numero ")
digitos(a)