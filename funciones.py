import msvcrt
import os
def opcion1(matriz):
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
def opcion2(matriz):
        i=0
        while i<len(matriz):
            print(matriz[i])
            i=i+1

        print("presione cualquier tecla para continuar")
        msvcrt.getch()

def opcion3(matriz):
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