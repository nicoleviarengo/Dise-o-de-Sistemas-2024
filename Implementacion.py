# Define la interfaz para las acciones del controlador, que luego 
# es implementada por diferentes clases especificas 

# Implementacion del controlador
class Controlador:
    def encender(self):
        pass

    def apagar(self):
        pass

# Dispositivos que funcionan como controlador
# Puede ser un celular, control remoto, etc.

class ControlRemoto(Controlador):
    def encender(self):
        print("Encender el dispositivo con el control remoto")

    def apagar(self):
        print("Apagar el dispositivo con el control remoto")

class AplicacionMovil(Controlador):
    def encender(self):
        print("Encender el dispositivo con la aplicación móvil")

    def apagar(self):
        print("Apagar el dispositivo con la aplicación móvil")
