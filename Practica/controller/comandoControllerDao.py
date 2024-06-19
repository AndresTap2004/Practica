from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from controller.tda.linked.linkedList import LinkedList
from modelo.comando import Comando

class ComandoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Comando)
        self.__comando = None

    @property
    def _comando(self):
        if self.__comando == None:
            self.__comando = Comando()
        return self.__comando

    @_comando.setter
    def _comando(self, value):
        self.__comando = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._comando, pos)
        
    @property
    def save(self):
        try:
            self._comando._id = self._lista._length + 1 
            self._save(self._comando)
        except Exception as e:
            print("No se pudo guardar: " + e)