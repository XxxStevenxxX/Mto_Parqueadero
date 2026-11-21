from models.vehiculos import Parqueadero
from views.vista import VistaConsola


class ControladorParqueadero:
    def __init__(self):
        self._parqueadero = Parqueadero()
        self._vista = VistaConsola()

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
            elif opcion == 0:
                self._vista.despedida()
                break
            else:
                self._vista.mostrar_mensaje_error("Opción no válida")

    def ingresar_vehiculo(self):
        try:
            tipo = self._vista.pedir_tipo_vehiculo()
            if tipo is None:
                self._vista.mostrar_mensaje_informativo("Ingreso cancelado")
                return
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
            vehiculo, resultado = self._parqueadero.retirar_vehiculo(placa)

            if vehiculo is not None:
                self._vista.mostrar_ticket_salida(vehiculo, resultado)  # resultado = costo
            else:
                self._vista.mostrar_mensaje_error(resultado)  # resultado = mensaje de error
        except Exception as e:
            self._vista.mostrar_mensaje_error(str(e))

    def mostrar_estado_parqueadero(self):
        estado = self._parqueadero.consultar_estado()
        self._vista.mostrar_estado_parqueadero(estado)

    def mostrar_vehiculos_estacionados(self):
        vehiculos = self._parqueadero.obtener_vehiculos()
        self._vista.mostrar_vehiculos_estacionados(vehiculos)


def iniciar_app():
    controlador = ControladorParqueadero()
    controlador.iniciar_app()
