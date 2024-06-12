import os
import msvcrt
from funciones import * 
matriz=[["Trabajador","cargo","Sueldo bruto","desc.salud","Desc.afp","liquido a pagar"]]
while True:
    os.system("cls")
    print("Planta nuclear")
    print("1-Registrar usuario")
    print("2-listar todos los trabajadores")
    print("3-imprimir plantilla de sueldos")
    print("4-Salir del programa")
    while True:    
        try:
            opcion=int(input("Ingrese una opcion: "))
            if opcion>0 and opcion<5:
                break
            else:
                print("opcion no dentro de los parametros")
        except:
            print("Opcion escrita invalidada")
    if opcion==1:
        opcion1(matriz)
    elif opcion==2:
        opcion2(matriz)
    elif opcion==3:
        opcion3(matriz) 
    else:
        print("Adios")
        break