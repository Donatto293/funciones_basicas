"""
SENA centro de biotecnologia agropecuaria
Ficha:2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 25/04/2024
"""
"""
Este codigo genera 2 numeros pseudo aleatorios y 
realiza funciones matematicas basicas
"""
from module import math_func as mf
import random
#declaro las variables que generan numeros aleatorios
num1 = random.randint(0,100)
num2 = random.randint(0,100)

#funcion saludo() imprime un saludo
def saludo(): 
    print ("hola mundo!:)")
    
       
#aqui llamamos a las funciones
if __name__=="__main__":
    saludo()
    print("numero 1=",num1, "numero 2=",num2)
    suma= mf.sumar(num1,num2)
    resta =mf.restar(num1,num2)
    mf.dividir(num1,num2)#la funcion dividir() imprime en pantalla
    multiplicar=mf.multiplicar(num1,num2)
    # imprimimos los valores
    print("la suma de los numeros es:",suma)
    print("la resta de los numeros es:",resta)
    print("la multiplicar de los numeros es:",multiplicar)


