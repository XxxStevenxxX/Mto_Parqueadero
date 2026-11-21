NOMBRES_TIPO = {"carro": "Carro", "moto": "Moto", "camion": "Camión"}


class VistaConsola:
    def mostrar_menu_principal(self):
        print("\n=== Bienvenido al sistema de parqueadero ===")
        print("1. Ingresar vehículo")
        print("2. Retirar vehículo")
        print("3. Consultar estado del parqueadero")
        print("4. Ver vehículos estacionados")
        print("0. Salir")

    def pedir_opcion(self):
        while True:
            try:
                opcion = input("Selecciona una opción: ")
                return int(opcion)
            except ValueError:
                print("Seleccione una opción válida (un número).")

    def mostrar_menu_vehiculos(self):
        print("\nTipo de vehículo")
        print("1. Carro")
        print("2. Moto")
        print("3. Camión")
        print("0. Cancelar")

    def pedir_tipo_vehiculo(self):
        while True:
            self.mostrar_menu_vehiculos()
            opcion = self.pedir_opcion()
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

    def pedir_placa(self, mensaje="Ingrese la placa del vehículo: "):
        while True:
            placa = input(mensaje).strip().upper()
            if len(placa) == 6 and placa.isalnum():
                return placa
            print("Por favor ingrese una placa válida (6 letras o números).")

    def pedir_placa_retiro(self):
        return self.pedir_placa("Ingrese la placa del vehículo a retirar: ")

    def mostrar_mensaje_exito(self, mensaje):
        print(f"✅ {mensaje}")

    def mostrar_mensaje_error(self, mensaje):
        print(f"❌ {mensaje}")

    def mostrar_mensaje_informativo(self, mensaje):
        print(f"❕ {mensaje}")

    def mostrar_estado_parqueadero(self, estado):
        print("\nEstado del parqueadero")
        for tipo, info in estado.items():
            tipo_nombre = NOMBRES_TIPO.get(tipo, tipo.capitalize())
            print(f"{tipo_nombre}: {info['ocupados']} ocupados, {info['disponibles']} disponibles")

    def mostrar_vehiculos_estacionados(self, vehiculos):
        if not vehiculos:
            print("No hay vehículos estacionados")
            return
        print("\nVehículos estacionados")
        for placa, vehiculo in vehiculos.items():
            hora_entrada = vehiculo.horaEntrada.strftime("%I:%M:%S %p")
            espacio = vehiculo.espacioAsignado
            print(f"Vehículo: {NOMBRES_TIPO.get(vehiculo.tipo, vehiculo.tipo)}, Placa: {placa}, "
                  f"Entrada: {hora_entrada}, Espacio: {espacio}")

    def mostrar_ticket_salida(self, vehiculo, costo):
        print("\n--- Ticket de salida ---")
        print(f"Placa: {vehiculo.placa}")
        print(f"Tipo: {NOMBRES_TIPO.get(vehiculo.tipo, vehiculo.tipo)}")

        if vehiculo.horaEntrada:
            print(f"Entrada: {vehiculo.horaEntrada.strftime('%I:%M:%S %p')}")
        if vehiculo.horaSalida:
            print(f"Salida: {vehiculo.horaSalida.strftime('%I:%M:%S %p')}")

        if vehiculo.horaEntrada and vehiculo.horaSalida:
            duracion = vehiculo.horaSalida - vehiculo.horaEntrada
            horas = duracion.total_seconds() / 3600
            print(f"Duración: {horas:.2f} horas")

        print(f"Costo: ${costo:,}")

    def despedida(self):
        print("Gracias por usar el parqueadero")
