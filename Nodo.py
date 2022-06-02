from __future__ import annotations
from typing import TYPE_CHECKING
from Personal import Personal

if TYPE_CHECKING:
    from Nodo import Nodo

class Nodo:
    __persona = None
    __siguiente = None

    def __init__(self, unaPersona: Personal):
        self.__persona = unaPersona
        self.__siguiente = None
    
    def getPersona(self) -> Personal:
        return self.__persona
    
    def setSiguiente(self, siguiente: Nodo):
        self.__siguiente = siguiente
    
    def getSiguiente(self) -> Nodo | None:
        return self.__siguiente
    
    def setPersona(self, unaPersona: Personal):
        self.__persona = unaPersona