import os
from ColeccionPersonal import ColeccionPersonal
from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from PersonalApoyo import PersonalApoyo
from DocenteInvestigador import DocenteInvestigador
from IngresadorTeclado import IngresadorTeclado
from IColeccion import IColeccion
from typing import List



class Menu:
    __switcher = None
    __ingresador = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,
                            '8':self.salir
                          }
        self.__ingresador = IngresadorTeclado()
        
    

    def opcion(self, unaColeccionPersonal: ColeccionPersonal,op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op in ('1', '2', '3'):
            func(IColeccion(unaColeccionPersonal))
        elif op in ('4', '5', '6', '7'):
            func(unaColeccionPersonal)
        else:
            func()
    
    
    def salir(self):
        print('Usted salio del programa')
    

    def ingresarPersonal(self) -> Personal:
        unaPersona = None
        
#        cuil = input("Ingrese el cuil: ")
        cuil = self.__ingresador.inputRegularExpression("Ingrese el cuil: ", "[0-9]{2,2}\-[0-9]{8,8}-[0-9]", "Cuil invalido, reintente: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        sueldoBasico = self.__ingresador.inputFloat("Ingrese el sueldo, en caso de incluir decimales use un punto: ", "Sueldo invalido, reintente: ")
        antiguedad = self.__ingresador.inputInt("Ingrese la antiguedad en años: ", "Valor invalido, reintente: ")
        tipo = self.__ingresador.inputOpcion("Seleccione el tipo de personal", ["Docente", "Investigador", "Personal de apoyo", "Docente-Investigador"])
        
        if tipo in ["Docente", "Docente-Investigador"]:
            carrera = input("Ingrese la carrera: ")
            cargo = self.__ingresador.inputOpcion("Seleccione el cargo", ["Simple", "Semiexclusivo", "Exclusivo"])
            catedra = input("Ingrese la catedra: ")
        
        if tipo in ["Investigador", "Docente-Investigador"]:
            areaInvestigacion = input("Ingrese el area de investigacion: ")
            tipoInvestigacion = input("Inrgese el tipo de investigacion: ")
        
        if tipo == "Docente-Investigador":
            categoriaIncentivos = self.__ingresador.inputOpcion("Seleccione la categoria de incentivos", ["I", "II", "III", "IV", "V"])
            importeExtra = self.__ingresador.inputFloat("Ingrese el importe extra, en caso de incluir decimales use un punto: ", "Importe invalido, reintente: ")
        
        if tipo == "Personal de apoyo":
            categoria = self.__ingresador.inputInt("Ingrese la categoria, de 1 a 22: ", "Categoria invalida, ingrese un numero entre 21 y 22: ")
            while not (1 <= categoria <= 22):
                categoria = self.__ingresador.inputInt("Categoria invalida, ingrese un numero entre 21 y 22: ", "Categoria invalida, ingrese un numero entre 21 y 22: ")
        

        if tipo == "Docente":
            unaPersona = Docente(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra)
        
        elif tipo == "Investigador":
            unaPersona = Investigador(cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoInvestigacion)
        
        elif tipo == "Docente-Investigador":
            unaPersona = DocenteInvestigador(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvestigacion, tipoInvestigacion, categoriaIncentivos, importeExtra)
        
        elif tipo == "Personal de apoyo":
            unaPersona = PersonalApoyo(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria)
        
        return unaPersona

    def opcion1(self, unaColeccionpersonal: IColeccion):
        insertado = False
        unaPersona = self.ingresarPersonal()
        posicion = self.__ingresador.inputInt("Ingrese la posicion en la que desea insertar el agente, las posiciones empiezan en 1: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
        while not insertado:
            try:
                unaColeccionpersonal.insertarElemento(unaPersona, posicion-1)
            except IndexError:
                posicion = self.__ingresador.inputInt("[ERROR] La posicion ingresada no es valida, reintente: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
            else:
                insertado = True
            print("Agente insertado")



    def opcion2(self, unaColeccionPersonal: IColeccion):
        unaPersona = self.ingresarPersonal()
        unaColeccionPersonal.agregarElemento(unaPersona)
        print("Agente agregado")



    def opcion3(self, unaColeccionPersonas: IColeccion):
        posicion = self.__ingresador.inputInt("Ingrese la posicion del agente que desea mostrar, las posiciones empiezan en 1: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
        mostrado = False
        try:
            unaColeccionPersonas.mostrarElemento(posicion-1)
        except IndexError:
            print("[ERROR] La posicion ingresada no es valida")
        else:
            mostrado = True


    
    def opcion4(self, unaColeccionPersonal: ColeccionPersonal):
        nombreCarrera = input("Ingrese el nombre de la carrera: ")
        print(unaColeccionPersonal.getListadoAgentesInvestigadores(nombreCarrera))



    def opcion5(self, unaColeccionPersonal: ColeccionPersonal):
        nombreAreaInvestigacion = input("Ingrese el area de investigacion: ")
        cantidades = unaColeccionPersonal.contarDocentesInvestigadores(nombreAreaInvestigacion)
        print("Hay {0} docentes investigadores y {1} investigadores normales en el area {2}".format(cantidades[0], cantidades[1], nombreAreaInvestigacion.title()))


    def opcion6(self, unaColeccionPersonal: ColeccionPersonal):
        print(unaColeccionPersonal.getListadoPersonal())


    def opcion7(self, unaColeccionPersonal: ColeccionPersonal):
        categoriaInvestigacion = self.__ingresador.inputOpcion("Seleccione la categoria de investigacion", ["I", "II", "III", "IV", "V"])
        print(unaColeccionPersonal.getListadoDocentesInvestigadores(categoriaInvestigacion))


    def ejecutarMenu(self, unaColeccionPersonal: ColeccionPersonal):
            os.system("clear")
            opcion = "0"
            while opcion != "8":
                print("Ingrese la opcion deseada")
                print("[1] Insertar un agente en una posicion determinada")
                print("[2] Agregar un agente a la coleccion")
                print("[3] Mostrar un agente dada una posicion de la lista")
                print("[4] Generar un listado ordenado por nombre de los agentes que se desempeñan como docentes investigadores dado un nombre de carrera")
                print("[5] Dada un area de investigacion, contar la cantidad de agentes que son docente investigador, y la cantidad de investigadores que trabajen en ese area")
                print("[6] Generar un listado que muestre nombre y apellido, tipo de agente y sueldo de todos los agentes, ordenado por apellido")
                print("[7] Dada una categoria de investigacion, listar apellido, nombre e importe extra por docencia e investigacion de todos los docentes investigadores que poseen esa categoria y mostrar el total de dindero que la Secretaria de Investigavion debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoria solicitada")
                print("[8] Guardar y salir")
                opcion = input("--> ")  
                os.system("clear")
                self.opcion(unaColeccionPersonal, opcion)
                input("Presione enter para continuar")
                os.system("clear")