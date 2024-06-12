import os
os.system("cls")


trabajadores=[]

while True:
    print("""
Registros de Trabajador
          -
1. Reistrar
2. Lista
3. Imprimir plantilla de Sueldos
4. Salir

Seleccione opcion
          """)
    while True:
        try:
            opc=int(input("> "))
            if opc in(1,2,3,4):
                break
            else:
                print("ERROR!, Ingrese una opcion entre 1 y 4")
        except:
            print("Error!, Ingrese opcion en numeros ENTEROS.")

    if opc==1:
        print("""Registrar
              """)
        nombre=input("Ingrese nombre\n>").upper
        
        while True:
            try:
                cargo=int(input("Seleccione Cargo:\n 1. CEO\n2. Desarrolllador\n3. Analista de Datos\n---\n> "))
                if cargo in(1,2,3):
                    break
                else:
                    print("ERROR!, Ingrese una opcion entre 1 y 3")
                
            except:
                print("Error!, Ingrese opcion en numeros ENTEROS.")
        
        while True:
            try:
                bruto=int(input("Ingrese Sueldo\n> "))
                if bruto>0:
                    break
                else:
                    print("Error!, ingrese sueldo superior a 0")
            except:
                print("Error!, Ingrese opcion en numeros ENTEROS.")

        afp=bruto*0.07
        salud=bruto*0.12

        total=afp+salud

        liquido=bruto-total

        trabajador={"nombre": nombre,
                     "cargo": cargo,
                     "bruto": bruto,
                     "salud": salud,
                     "afp": afp,
                     "liquido": liquido}
        trabajadores.append(trabajador)
          
    elif opc==2:
        print("Datos Generales")
        print("Nombre\t\t\t\t Cargo")
        
    elif opc==3:
        pass
    elif opc==4:
        break
        