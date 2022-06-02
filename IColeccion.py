from zope.interface import Interface

class IColeccion(Interface):
    def insertarElemento(self, elemento: object, pos:int):
        """
        Inserta un elemento en una posicion valida de la coleccion
        """
        
        pass
    
    def agregarElemento(self, elemento: object):
        """
        Agrega un elemento al final de la coleccion
        """
        
        pass

    def mostrarElemento(self, pos: int):
        """
        Muestra un elemento dada una posicion de la coleccion
        """
        
        pass