from Abstraccion import AireAcondicionado, Luces
from Implementacion import ControlRemoto, AplicacionMovil

# Nuestro aire acondicionado controlado por un control remoto
control_remoto = ControlRemoto()
mi_aire = AireAcondicionado(control_remoto)
mi_aire.encender()
mi_aire.apagar()

# Nuestras luces controladas por una aplicación móvil
app_movil = AplicacionMovil()
mis_luces = Luces(app_movil)
mis_luces.encender()
mis_luces.apagar()
