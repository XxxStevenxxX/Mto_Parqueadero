from models.vehiculos import FabricaVehiculos
from views.vista import mostrar_resultados, pedir_tipo_vehiculo
from models.vehiculos import Parqueadero
from views.vista import VistaConsola


class ControladorParqueadero:
    def __init__(self):
        self._parqueadero = Parqueadero()
        self._vista = VistaConsola
    
    def iniciar_app(self):
        while True:
            self._vista.mostrar_menu_principal()
            opcion = self._vista.pedir_opcion()
            
            if opcion == 1:
                self.ingresar_vehiculo()
            elif opcion == 2:
                self.retirar_vehiculo()
            elif opcion == 3:
                self.mostrar_estado_parqueadero()
            elif opcion == 4:
                self.mostrar_vehiculos_estacionados()
            elif opcion == 5:
                self._vista.despedida()
                break
    
    def ingresar_vehiculo(self):
        try:
            tipo = self._vista.pedir_tipo_vehiculo()
            placa = self._vista.pedir_placa()
            
            exito, mensaje = self._parqueadero.ingresar_vehiculo(tipo, placa)
            
            if exito:
                self._vista.mostrar_mensaje_exito(mensaje)
            else:
                self._vista.mostrar_mensaje_error(mensaje)
        except Exception as e:
            self._vista.mostrar_mensaje_error(str(e))
    
    def retirar_vehiculo(self):
        try:
            placa = self._vista.pedir_placa_retiro()
            vehiculo, costo = self._parqueadero.retirar_vehiculo()
            
            if vehiculo is not False:
                self._vista.mostrar_ticket_salida(vehiculo, costo)
            else:
                self._vista.mostrar_mensaje_error(vehiculo)
        except Exception as e:
            self._vista.mostrar_mensaje_error(str(e))
    
    def iniciar_app():
        controlador = ControladorParqueadero()
        controlador.iniciar_app