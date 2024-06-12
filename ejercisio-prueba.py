import os
import msvcrt
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
        nombre=input("ingrese nombre del trabajador: ")
        while True:
            cargo=input("Ingrese el cargo: ")
            if cargo.lower()=="ceo" or cargo.lower()=="desarrollador" or cargo.lower()=="analista de datos":
                break
            else :
                print("El cargo ingresado no esta dentro de esta empresa")
        while True:
            try:
                sueldo_bruto=int(input("ingrese el sueldo bruto: "))
                if sueldo_bruto>0:
                    break
                else:
                    print("su sueldo no puede ser negativo o 0")
            except:
                print("valor ingresado invalido")

        salud=sueldo_bruto*0.07
        afp=sueldo_bruto*0.12
        liquido=sueldo_bruto-(salud+afp)
        lista=[nombre,cargo,sueldo_bruto,salud,afp,liquido]
        os.system("cls")
        matriz.append(lista)
        print("trabajador agregado con exito")
        print("presione cualquier tecla para continuar")
        msvcrt.getch()

    elif opcion==2:
        i=0
        while i<len(matriz):
            print(matriz[i])
            i=i+1

        print("presione cualquier tecla para continuar")
        msvcrt.getch()

    elif opcion==3:
        i=0
        bus_cargo=input("ingrese el cargo a buscar: ")
        while i<len(matriz):
            if matriz[i][1]==bus_cargo.lower():
                with open("trabajadores.txt","a") as archivo:
                    archivo.write(matriz[i][0])
                    archivo.write(" ,")
                    archivo.write(matriz[i][1])
                    archivo.write(" ,")
                    archivo.write(str(matriz[i][2]))
                    archivo.write(" ,")
                    archivo.write(str(matriz[i][3]))
                    archivo.write(" ,")
                    archivo.write(str(matriz[i][4]))
                    archivo.write(" ,")
                    archivo.write(str(matriz[i][5]))
                    archivo.write("\n")
            i=i+1
        os.system("cls")
        print("Archivo creado con exito")
        print("presione cualquier tecla para continuar")
        msvcrt.getch()      
    else:
        break