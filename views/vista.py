import datetime

class VistaConsola:
    def mostrar_menu_principal(self):
        print("Bienvenido al sistema parqueadero")
        print("1. Ingresar vehículo")
        print("1. Retirar vehículo")
        print("1. Consultar estado del parqueadero")
        print("1. Ver vehículos estacionados")
        print("0. Salir")
    
    def pedir_opcion(self):
        while True:
            try:
                opcion = input("Selecciona una opción: ")
                return int(opcion)
            except ValueError:
                print("Seleccione una opción válida: ")
    
    def mostrar_menu_vehículos(self):
        print("Tipo de vehículo")
        print("1. Carro")
        print("2. Moto")
        print("3. Camión")
        print("0. Salir")
        
    def pedir_vehículo(self):
        while True:
            self.mostrar_menu_vehículos
            opcion = self.pedir_opcion
            if opcion == 1:
                return "carro"
            elif opcion == 2:
                return "moto"
            elif opcion == 3:
                return "camion"
            elif opcion == 0:
                return None
            else:
                print("Selecciona una opción correcta")
    
    def pedir_placa(self):
        while True:
            placa = input("Ingrese la placa del vehículo: ").strip().upper()
            if len(placa) == 6:
                return placa
            else:
                print("Por favor ingrese una placa válida.")
    
    def mostrar_mensaje_exito(self, mensaje):
        print(f"✅{mensaje}")
    def mostrar_mensaje_error(self, mensaje):
        print(f"❌{mensaje}")
    def mostrar_mensaje_informativo(self,mensaje):
        print(f"❕{mensaje}")
    
    def mostrar_estado_parqueadero(self, estado):
        print(f"Estado del parqueadero")
        
        for tipo, info in estado.items():
            tipo_nombre = tipo.capitalize()
            print(f"{tipo_nombre}: {info['ocupados']} ocupados, {info['disponibles']} disponibles")
    
    def mostrar_vehiculos_estacionados(self, vehiculos):
        if not vehiculos:
            print("No hay vehículos estacionados")
            return
        for placa, vehiculo in vehiculos.items():
            hora_entrada = vehiculo.horaEntrada.strftime("%I:%M:%S:%p")
            espacio = vehiculo.espacioAsignado
            print(f"Vehiculo: {vehiculo.tipo}, Placa: {placa} Entrada: {hora_entrada}, Espacio: {espacio}")
    
    def mostrar_ticket_salida(self, vehiculo, costo):
        print("Ticket de salida")
        print(f"Placa: {vehiculo.placa}")
        print(f"Tipo: {vehiculo.tipo}")
        
        if vehiculo.horaEntrada:
            hora_entrada = vehiculo.horaEntrada.strftime("%I:%M:%S%p")
            print(f"Entrada: {hora_entrada}")
        if vehiculo.horaSalida:
            hora_salida = vehiculo.horaSalida.strftime("%I:%M:%S%p")
            print(f"Salida: {hora_salida}")
        
        if vehiculo.horaEntrada and vehiculo.horaSalida:
            duracion = vehiculo.horaSalida - vehiculo.horaEntrada
            horas = duracion.total_seconds()/3600
            print(f"Duración: {horas:.2f}")
        
        print(f"Costo: {costo}")
        
    def pedir_placa_retiro(self):
        pass
    
    def despedida(self):
        print("Gracias por usar el parqueadero")