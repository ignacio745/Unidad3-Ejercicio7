from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from Personal import Personal
from zope.interface import implementer
from IColeccion import IColeccion
from Nodo import Nodo


@implementer(IColeccion)
class ColeccionPersonal:
    __comienzo = None
    __actual = None
    __tope = 0

    

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
    
    def insertarElemento(self, unaPersona: Personal, pos: int):
        if not isinstance(pos, int) or pos < 0:
            raise IndexError("Indice invalido")

        unNodo = Nodo(unaPersona)
        if pos == 0:
            unNodo.setSiguiente(self.__comienzo)
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        else:
            i = 1
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                i += 1
                aux = aux.getSiguiente()
            if i == pos:
                unNodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(unNodo)
            else:
                raise IndexError("Indice fuera de rango")
        
        self.__tope += 1
        
            
    
    def agregarElemento(self, unaPersona: Personal):
        unNodo = Nodo(unaPersona)
        
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(unNodo)
        
        self.__tope += 1
    


    def mostrarElemento(self, pos: int):
        if pos < 0 or self.__comienzo == None:
            raise IndexError("Indice invalido")
        
        else:
            i = 0
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                aux = aux.getSiguiente()
                i += 1
            if i == pos:
                unaPersona = aux.getPersona()
                print(unaPersona)
            else:
                raise IndexError("Indice fuera de rango")
            
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Personal:
        
        if self.__actual == None:
            self.__actual = self.__comienzo
            raise StopIteration
        
        else:
            unaPersona = self.__actual.getPersona()
            self.__actual = self.__actual.getSiguiente()
            return unaPersona
    
    
    def ordenarPersonal(self, metodoComparacion):
        # La k conserva el primer nodo del ultimo par ordenado para saber si el ordenamiento ha terminado
        # La cota conserva el segundo nodo del ultimo par ordenado para saber si quedan nodos que ordenar en la iteracion actual
        # unNodo es el nodo que se esta ordenando actualmente
        
        
        if self.__comienzo != None:
            
            k = None
            cota = None
            
            while k != self.__comienzo:
                
                k = self.__comienzo
                unNodo = self.__comienzo
                while unNodo.getSiguiente() != cota:
                    

                    if metodoComparacion(unNodo.getSiguiente().getPersona()) < metodoComparacion(unNodo.getPersona()):
                        
                        unaPersona = unNodo.getPersona()
                        unNodo.setPersona(unNodo.getSiguiente().getPersona())
                        unNodo.getSiguiente().setPersona(unaPersona)
                        k = unNodo
                    
                    unNodo = unNodo.getSiguiente()
                

                cota = k.getSiguiente()
            

    def getListadoAgentesInvestigadores(self, nombreCarrera: str) -> str:
        """
        Retorna un listado ordenado por nombre con los datos de los agentes que se desempeñan como docentes investigadores en una carrera.

        Parametros
        ----------
        nombreCarrera: str
            El nombre de la carrera
        """

        self.ordenarPersonal(Personal.getNombre)
        cadena = "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}\n".format("Cuil", "Apellido", "Nombre", "Categoria incentivos", "Importe extra")
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getCarrera().lower() == nombreCarrera.lower():
                cadena += "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20.2f}\n".format(unaPersona.getCuil(), unaPersona.getApellido(), unaPersona.getNombre(), unaPersona.getCategoriaIncentivos(), unaPersona.getImporteExtra())
        return cadena
    

    def contarDocentesInvestigadores(self, nombreAreaInvestigacion: str, clase) -> tuple:
        """
        Retorna una tupla con la cantidad de docentes investigadores y la cantidad de investigadores de un area de investigacion en ese orden.
        
        Parametros
        ----------
        nombreAreaInvestigacion: str
            El nombre del area de investigacion a contar.
        """

        contadorDocentesInvestigadores = 0
        contadorInvestigadores = 0
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getAreaInvestigacion().lower() == nombreAreaInvestigacion.lower():
                contadorDocentesInvestigadores += 1
            elif isinstance(unaPersona, Investigador) and unaPersona.getAreaInvestigacion().lower() == nombreAreaInvestigacion.lower():
                contadorInvestigadores += 1
        return (contadorDocentesInvestigadores, contadorInvestigadores)
    


    def getListadoPersonal(self):
        self.ordenarPersonal(Personal.getApellido)
        cadena = "{0:<20}{1:<20}{2:<20}{3:<20}\n".format("Nombre", "Apellido", "Tipo de agente", "Sueldo")
        for unaPersona in self:
            cadena += "{0:<20}{1:<20}{2:<20}{3:<20}\n".format(unaPersona.getNombre(), unaPersona.getApellido(), unaPersona.__class__.__name__, unaPersona.getSueldo())
        return cadena
    

    def getListadoDocentesInvestigadores(self, categoria: str):
        cadena = "{0:<20}{1:<20}{2:<20}\n".format("Apellido", "Nombre", "Importe extra")
        total = 0
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getCategoriaIncentivos().lower() == categoria.lower():
                cadena += "{0:<20}{1:<20}{2:<20}\n".format(unaPersona.getApellido(), unaPersona.getNombre(), unaPersona.getImporteExtra())
                total += unaPersona.getImporteExtra()
        cadena += "Importe total en concepto de incentivos: {0:.2f}\n".format(total)
        return cadena
    

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            personas = [unaPersona.toJSON() for unaPersona in self]
        )
        return d