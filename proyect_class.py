print("Bienvenido\nGUARDERIA VILLA FELIZ")

class niño():


    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    
    def inf(self):
        
        print("Guarderia villa feliz")
        print("Nombre del niño: "+ self.nombre, self.apellido + ".")
        print("Edad: " + self.edad)  

    #Getters
    def get_Nombre(self):
        return self.nombre

    def get_Apellido(self):
        return self.apellido

    def get_Edad(self):
        return self.edad

    #Setters
    def set_Edad(self, edad):
        self.edad = edad
 

#subclase grupo de niños nivel 1
class nivel_1(niño):
    edad = "Nivel 1"

#subclase grupo de niños nivel 2
class nivel_2(niño):
    edad = "Nivel 2"

#subclase grupo de niños nivel 3
class nivel_3(niño):
    edad = "Nivel 3"

#subclase grupo de niños nivel 4
class nivel_4(niño):
    edad = "Nivel 4"
   

a = int(input("Inserte:\n1 - Para visualizar a los niños de nivel 1:\n2 - Para visualizar a los niños de nivel 2:\n3 - Para visualizar a los niños de nivel 3:\n4 - Para visualizar a los niños de nivel 4:\n-------->" ))
        #if de niños nivel 1
if a == 1:
    niño_nivel1 = nivel_1("Ernesto", "Rosas", "2 años")
    print(niño_nivel1.edad)
    niño_nivel1.inf()

        #elif de niños nivel 2
elif a == 2:
    niño_nivel2 = nivel_2("Alejandra", "Martinez", "3 años")
    print(niño_nivel2.edad)
    niño_nivel2.inf()

        #elif de niños nivel 3
elif a == 3:
    niño_nivel3 = nivel_3("Ramon", "Cazares", "4 años")
    print(niño_nivel3.edad)
    niño_nivel3.inf()

    #elif de niños nivel 4
elif a == 4:
    niño_nivel4 = nivel_4("Maria", "Gonzalez", "5 años")
    print(niño_nivel4.edad)
    niño_nivel4.inf()


#Inicio de modificacion con los Setters y Getters
set = int(input("\nInserte:\n1 - Para modificar datos:\n2 - Para salir del programa:\n--------> " ))

if set == 1:
    es = int(input("\nInserte:\n1 - Para modificar niño de nivel 1:\n2 - Para modificar niño de nivel 2:\n3 - Para modificar niño de nivel 3:\n3 - Para modificar niño de nivel 4:\n--------> " ))

    if es == 1:
        modi = int(input("\nInserte:\n1 - Para modificar Edad:\n2 - Para Salir:\n--------> " ))
        if modi == 1:
            eda = int(input("Ingresa el nuevo edad: " ))
            print("Guardado con exito")
            print("\n---La nueva edad es: " )
            level1 = niño("Ernesto", "Rosas", "2 años")
            level1.set_Edad(eda)
            print(level1.get_Edad())
            print("\n---")
            print("\n---Adios---")
            
        elif modi == 3:
            print("\n---Adios---")
            

    elif es == 2:
        modi = int(input("\nInserte:\n1 - Para modificar Nombre:\n2 - Para modificar Apellido:\n3 - Para modificar Edad:\n--------> " ))
        if modi == 1:
            eda = input("Ingresa el nuevo edad: " )
            print("Guardado con exito")
            print("\n---La nueva edad es: " )
            level2 = niño("Alejandra", "Martinez", "3 años")
            level2.set_Edad(eda)
            print(level2.get_Edad())
            print("\n---")
            print("\n---Adios---")
            


        elif modi == 3:
            print("\n---Adios---")

    elif es == 3:
        modi = int(input("\nInserte:\n1 - Para modificar Nombre:\n2 - Para modificar Apellido:\n3 - Para modificar Edad:\n--------> " ))
        if modi == 1:
            eda = input("Ingresa el nuevo edad: " )
            print("Guardado con exito")
            print("\n---La nueva edad es: " )
            level3 = niño("Ramon", "Cazares", "4 años")
            level3.set_Edad(eda)
            print(level3.get_Edad())
            print("\n---")
            print("\n---Adios---")


        elif modi == 3:
            print("\n---Adios---")

    elif es == 4:
        modi = int(input("\nInserte:\n1 - Para modificar Nombre:\n2 - Para modificar Apellido:\n3 - Para modificar Edad:\n--------> " ))
        if modi == 1:
            eda = input("Ingresa el nuevo edad: " )
            print("Guardado con exito")
            print("\n---La nueva edad es: " )
            level4 = niño("Maria", "Gonzalez", "5 años")
            level4.set_Edad(eda)
            print(level4.get_Edad())
            print("\n---")
            print("\n---Adios---")


        elif modi == 3:
            print("\n---Adios---")

elif set == 2:
            print("\n---Adios---")