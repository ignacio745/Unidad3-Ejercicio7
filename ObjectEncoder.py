from ColeccionPersonal import ColeccionPersonal
from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from PersonalApoyo import PersonalApoyo
from DocenteInvestigador import DocenteInvestigador
import json

class ObjectEncoder:

    def decodificarDiccionario(self, d):
        retorno = None
        if "__class__" not in d:
            retorno = d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "ColeccionPersonal":
                unaColeccionPersonal = class_()
                personas = d["personas"]
                for i in range(len(personas)):
                    dPersona = personas[i]
                    class_name = dPersona["__class__"]
                    class_ = eval(class_name)
                    atributos = dPersona["__atributos__"]
                    unaPersona = class_(**atributos)
                    unaColeccionPersonal.agregarElemento(unaPersona)
            retorno = unaColeccionPersonal
        return retorno
    

    def guardarJSONArchivo(self, diccionario, nombreArchivo):
        archivo = open(nombreArchivo, "w", encoding="UTF-8")
        json.dump(diccionario, archivo, indent=4)
        archivo.close()
    

    def leerJSONArchivo(self, nombreArchivo):
        archivo = open(nombreArchivo, encoding="UTF-8")
        diccionario = json.load(archivo)
        archivo.close()
        return diccionario