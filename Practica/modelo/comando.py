from datetime import datetime, date

class Comando:
    def __init__(self):
        self.__id = 0
        self.__nombre_usuario = ""
        self.__apellido_usuario = ""
        self._email = ""
        self.__comando = ""
        self.__lenguaje = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre_usuario(self):
        return self.__nombre_usuario

    @_nombre_usuario.setter
    def _nombre_usuario(self, value):
        self.__nombre_usuario = value

    @property
    def _apellido_usuario(self):
        return self.__apellido_usuario

    @_apellido_usuario.setter
    def _apellido_usuario(self, value):
        self.__apellido_usuario = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def _comando(self):
        return self.__comando

    @_comando.setter
    def _comando(self, value):
        self.__comando = value

    @property
    def _lenguaje(self):
        return self.__lenguaje

    @_lenguaje.setter
    def _lenguaje(self, value):
        self.__lenguaje = value

    def __str__(self):
        return f"{self._nombre_usuario} {self._apellido_usuario} {self._comando} {self._lenguaje}"

    @property
    def serializar(self):
        return {
            "id": self._id,
            "nombre_usuario": self._nombre_usuario,
            "apellido_usuario": self._apellido_usuario,
            "comando": self._comando,
            "lenguaje": self._lenguaje,
        }
        
    @staticmethod
    def deserializar(data):
        comando = Comando()
        comando._id = data["id"]
        comando._nombre_usuario = data["nombre_usuario"]
        comando._apellido_usuario = data["apellido_usuario"]
        comando._comando = data["comando"]
        comando._lenguaje = data["lenguaje"]
        return comando
