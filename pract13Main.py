'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 13: Diccionarios Anidados
Archivo Main
Fecha: 17 De Noviembre De 2022
'''

import pract13Func as pf

opc=1
while opc==1:
    pf.main()
    opc=int(input("Continuar? (0/1): "))
    while opc<0 or opc>1:
        opc=int(input("Continuar? (0/1): "))