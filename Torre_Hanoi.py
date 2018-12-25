#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:48:24 2018

@author: robson
"""

def movimentar(peca, de_torre, para_torre):
    print("Movimentar peça {} da torre {} para a torre {}".format(peca, de_torre, para_torre))

def towers(lista_pecas, de_torre, para_torre, torre_extra):
    if len(lista_pecas)==1:
        movimentar(lista_pecas[0], de_torre, para_torre)
    else:
        towers(lista_pecas[:len(lista_pecas)-1],de_torre, torre_extra, para_torre)
        movimentar(lista_pecas[len(lista_pecas)-1], de_torre, para_torre)
        towers(lista_pecas[:len(lista_pecas)-1],torre_extra, para_torre, de_torre)


#exemplo
        
lista = [x for x in range(1,5)]

towers(lista, 'P1', 'P2', 'P3')