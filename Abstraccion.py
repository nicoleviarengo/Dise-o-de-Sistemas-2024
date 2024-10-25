# Tenemos distintos dispositivos que queremos controlar
class Dispositivo:
    def __init__(self, controlador):
        self.controlador = controlador

    def encender(self):
        self.controlador.encender()

    def apagar(self):
        self.controlador.apagar()

#Dispositivos especificos
class AireAcondicionado(Dispositivo):
    pass

class Luces(Dispositivo):
    pass