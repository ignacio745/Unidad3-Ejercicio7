from zope.interface import Interface

class IColeccion(Interface):
    def insertarElemento(elemento: object, pos:int):
        """
        Inserta un elemento en una posicion valida de la coleccion
        """
        
        pass
    
    def agregarElemento(elemento: object):
        """
        Agrega un elemento al final de la coleccion
        """
        
        pass

    def mostrarElemento(pos: int):
        """
        Muestra un elemento dada una posicion de la coleccion
        """
        
        pass