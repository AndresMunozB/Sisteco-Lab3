
"""
Integrante: Andrés Muñoz 
            Diego Mellis
            Javier Arredondo
"""    
from jadCypher import JadCypher
import time
import matplotlib.pyplot as plt

def graficar(title,xlabel,ylabel,x,y):
	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(x,y,"-")
	plt.show()

def encryptFile(inputName,outputName,password,size_block,show):
    jad = JadCypher()
    inputFile = open(inputName,"r")
    outputFile = open(outputName, "w")
    text = ""
    for line in inputFile:
        text += line
    stringOutput = jad.encrypt(text,password,size_block,show)
    outputFile.write(stringOutput)
    inputFile.close()
    outputFile.close()

def decryptFile(inputName,outputName,password,size_block,show):
    jad = JadCypher()
    inputFile = open(inputName,"r")
    outputFile = open(outputName, "w")
    text = ""
    for line in inputFile:
        text += line
    stringOutput = jad.decrypt(text,password,size_block,show)
    outputFile.write(stringOutput)
    inputFile.close()
    outputFile.close()

def printMenu():
    print("    MENU\n")
    print("1) Cambiar tamaño del bloque.")
    print("2) Cambiar contraseña.")
    print("3) Encriptar archivo.")
    print("4) Desencriptar archivo.")
    print("5) Encriptar archivo (mostrar pasos).")
    print("6) Desencriptar archivo (mostrar pasos).")
    print("7) Salir")

def avalancha(t1,t2):
    contador = 0
    largo = 0
    t1bit = t1
    t2bit = t2
    if len(t1bit) > len(t2bit):
        largo = len(t2bit)
    else:
        largo = len(t1bit)
    for i in range(len(t1bit)):
        if(t1bit[i] != t2bit[i]):
            
            print(i,t1bit[i],t2bit[i])
            contador +=1
    print(contador)
def compareFiles():
    inputFile1 = open("1","r")
    inputFile2 = open("3","r")
    text1 = ""
    text2 = ""
    for line in inputFile1:
        text1 += line
    for line in inputFile2:
        text2 += line
    avalancha(text1,text2)
    inputFile1.close()
    inputFile2.close()

def main():
    
    size_block = 8
    password = "chaopenc"
    menu = ""
    print("NOTA: Tamaño del bloque por defecto: 8 ")
    print("      Contraseña por defecto: 'holacomo' \n\n")
    while(True):
        printMenu()
        menu = input("Ingresa una opción: ")
        if(menu == '1'):
            try:
                size_block = int(input("Ingrese el tamaño del bloque: "))
            except:
                print("Error al ingresar el tamaño del bloque.")
        elif (menu == '2'):
            try:
                password = input("Ingrese la contraseña: ")
            except:
                print("Error al ingresar el la contraseña.")
        elif (menu == '3'):
            try:
                inputName = input("Ingrese el nombre del archivo de entrada: ")
                outputName = input("Ingrese el nombre del archivo de salida: ")    
                encryptFile(inputName,outputName,password,size_block,False)
            except:
                print("Error al encriptar, intente nuevamente.")
        elif (menu == '4'):
            try:
                inputName = input("Ingrese el nombre del archivo de entrada: ")
                outputName = input("Ingrese el nombre del archivo de salida: ")
                decryptFile(inputName,outputName,password,size_block,False)
            except:
                print("Error al desencriptar, intente nuevamente.")
        elif (menu == '5'):
            try:
                inputName = input("Ingrese el nombre del archivo de entrada: ")
                outputName = input("Ingrese el nombre del archivo de salida: ")
                encryptFile(inputName,outputName,password,size_block,True)
            except:
                print("Error al encriptar, intente nuevamente.")
        elif (menu == '6'):
            try:
                inputName = input("Ingrese el nombre del archivo de entrada: ")
                outputName = input("Ingrese el nombre del archivo de salida: ")
                decryptFile(inputName,outputName,password,size_block,True)
            except:
                print("Error al desencriptar, intente nuevamente.")
        elif (menu == '7'):
            break
        



main()

