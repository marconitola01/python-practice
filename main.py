import time
import random

#hallar numero maximo
"""""""""""
def max (n1, n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print("Son iguales")
print('introduce un numero 1')
n1 = int(input())
print('introduce nuemro 2')
n2 = int(input())
print('el mayor es :')
max(n1,n2)
"""""

#tomar tres numeros y devolver el maximo de ellos
"""""""""
def maxtr(n1,n2,n3):
    if n1 > n2 and n1>n3:
        print(n1)
    if n2 > n1 and n2 > n3:
        print(n2)
    if n3 > n1 and n3 > n2:
        print(n3)

print('introduce numero 1')
numero1 = int(input())
print('intriduce numero 2')
numero2 = int(input())
print('introduce numero 3')
numero3 = int(input())

print('el numero maximo es: ')
maxtr(numero1,numero2,numero3)

"""""


#imprimir el largo de una lista o cadena (se pude gace con len pero alovorgo)
"""""""""
def tamaño(Lista):
    contador = 0
    for i in Lista:
        contador += 1
    return contador

print(tamaño([1,2,3,4]))
print(tamaño("buenalabanda"))
"""""

#devolver true si es una vocal y sino false
"""""""""
def vocalT(vocal):
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal=="o" or vocal =="u":
        return True
    if vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
        return True
    else:
        return False
print('ingrese una vocal')
vocal = input()

print(vocalT(vocal))
"""""

#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""""""""
def sumar(ListaNumeros1):
    suma = 0
    for i in ListaNumeros1:
        suma += i
    return suma

def multipli(ListaNumeros2):
    multi = 1
    for j in ListaNumeros2:
        multi *= j
    return multi

print(sumar([1,2,3,4]))
print(multipli([1,2,3,4]))
"""""

#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""""""""
def palabraInversa(palabra):
    invertida = ""
    contador = len(palabra)
    index = -1
    while contador >= 1:
        invertida += palabra[index]
        index = index +(-1)
        contador -= 1
    return invertida

print(palabraInversa("buenas"))
"""""""""

#llenar array

"""""""""
def llenarLista():
    lista = []
    for i in range(5):
        print('ingres un numero')
        lista.append(int(input()))
    print(lista);


llenarLista()
"""""