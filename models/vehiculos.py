import datetime


class Vehiculo:
    def __init__(self, tipo, altura, placa):
        self._tipo = tipo  # _ = atributo protegido (convención)
        self._altura = altura
        self._placa = placa
        self._horaEntrada = None
        self._horaSalida = None
        self._espacioAsignado = None

    # Atributos de solo lectura
    @property
    def tipo(self):
        return self._tipo

    @property
    def altura(self):
        return self._altura

    @property
    def placa(self):
        return self._placa

    # Atributos que cambian durante la vida del vehículo en el parqueadero
    @property
    def horaEntrada(self):
        return self._horaEntrada

    @horaEntrada.setter
    def horaEntrada(self, valor):
        self._horaEntrada = valor

    @property
    def horaSalida(self):
        return self._horaSalida

    @horaSalida.setter
    def horaSalida(self, valor):
        self._horaSalida = valor

    @property
    def espacioAsignado(self):
        return self._espacioAsignado

    @espacioAsignado.setter
    def espacioAsignado(self, valor):
        self._espacioAsignado = valor


class FabricaVehiculos:
    @staticmethod
    def crear(tipo, placa):
        if tipo == "carro":
            return Vehiculo("carro", 1.6, placa)
        elif tipo == "moto":
            return Vehiculo("moto", 1.20, placa)
        elif tipo == "camion":
            return Vehiculo("camion", 3.0, placa)
        else:
            raise ValueError("Tipo de vehículo no válido")


class CalculadoraTarifa:
    def __init__(self):
        self._tarifas = {
            "carro": 2000,
            "moto": 1000,
            "camion": 5000
        }

    def calcular_costo(self, vehiculo, horaEntrada, horaSalida):
        if not horaEntrada or not horaSalida:
            return 0
        duracion = horaSalida - horaEntrada
        horas = duracion.total_seconds() / 3600
        horas = max(1, horas)  # Se cobra mínimo 1 hora
        tipo = vehiculo.tipo.lower()
        return round(self._tarifas[tipo] * horas)


class GestorEspacios:
    def __init__(self):
        self._capacidad = {
            "carro": 20,
            "moto": 30,
            "camion": 5
        }
        # Códigos de los espacios ocupados por tipo, p. ej. {"CAR-01", "CAR-02"}
        self._ocupados = {tipo: set() for tipo in self._capacidad}

    def tipo_valido(self, tipo):
        return tipo in self._capacidad

    def espacios_disponibles(self, tipo):
        return self._capacidad[tipo] - len(self._ocupados[tipo])

    def estado(self):
        """Devuelve {tipo: {'ocupados': n, 'disponibles': m}}."""
        return {
            tipo: {
                "ocupados": len(self._ocupados[tipo]),
                "disponibles": self.espacios_disponibles(tipo),
            }
            for tipo in self._capacidad
        }

    def asignar_espacio(self, vehiculo):
        """Reserva el primer espacio libre y devuelve su código (None si no hay)."""
        tipo = vehiculo.tipo.lower()
        for numero in range(1, self._capacidad[tipo] + 1):
            codigo = f"{tipo[:3].upper()}-{numero:02d}"
            if codigo not in self._ocupados[tipo]:
                self._ocupados[tipo].add(codigo)
                return codigo
        return None

    def liberar_espacio(self, vehiculo):
        tipo = vehiculo.tipo.lower()
        if vehiculo.espacioAsignado in self._ocupados[tipo]:
            self._ocupados[tipo].remove(vehiculo.espacioAsignado)
            return True
        return False


class RepositorioVehiculos:
    def __init__(self):
        self._vehiculos = {}

    def guardar(self, vehiculo):
        self._vehiculos[vehiculo.placa] = vehiculo
        return True

    def obtener_por_placa(self, placa):
        return self._vehiculos.get(placa)

    def eliminar(self, placa):
        if placa in self._vehiculos:
            del self._vehiculos[placa]
            return True
        return False

    def obtener_todos(self):
        return self._vehiculos.copy()  # Copia para no exponer el diccionario interno

    def existe_placa(self, placa):
        return placa in self._vehiculos


class Parqueadero:
    def __init__(self):
        self._fabrica = FabricaVehiculos()
        self._calculadora = CalculadoraTarifa()
        self._gestor_espacios = GestorEspacios()
        self._repositorio = RepositorioVehiculos()

    def ingresar_vehiculo(self, tipo, placa):
        """Devuelve (exito, mensaje)."""
        try:
            tipo = tipo.lower()
            placa = placa.upper()

            if not self._gestor_espacios.tipo_valido(tipo):
                return False, f"Tipo de vehículo no válido: {tipo}"
            if self._repositorio.existe_placa(placa):
                return False, f"El vehículo con placa {placa} ya se encuentra registrado"
            if not self._gestor_espacios.espacios_disponibles(tipo):
                return False, f"No hay espacios disponibles para {tipo}"

            vehiculo = self._fabrica.crear(tipo, placa)
            vehiculo.espacioAsignado = self._gestor_espacios.asignar_espacio(vehiculo)
            vehiculo.horaEntrada = datetime.datetime.now()
            self._repositorio.guardar(vehiculo)

            return True, (f"Vehículo {tipo} con placa {placa} fue ingresado "
                          f"exitosamente en el espacio {vehiculo.espacioAsignado}")
        except Exception as e:
            return False, str(e)

    def retirar_vehiculo(self, placa):
        """Devuelve (vehiculo, costo) si sale bien, o (None, mensaje_de_error)."""
        try:
            placa = placa.upper()
            vehiculo = self._repositorio.obtener_por_placa(placa)
            if vehiculo is None:
                return None, f"El vehículo con placa {placa} no se encuentra en el parqueadero"

            if not self._gestor_espacios.liberar_espacio(vehiculo):
                return None, f"No se pudo liberar el espacio del vehículo con placa {placa}"

            vehiculo.horaSalida = datetime.datetime.now()
            costo = self._calculadora.calcular_costo(
                vehiculo, vehiculo.horaEntrada, vehiculo.horaSalida)

            self._repositorio.eliminar(placa)
            return vehiculo, costo
        except Exception as e:
            return None, str(e)

    def consultar_estado(self):
        """Ocupación por tipo de vehículo."""
        return self._gestor_espacios.estado()

    def obtener_vehiculos(self):
        """Todos los vehículos estacionados, {placa: Vehiculo}."""
        return self._repositorio.obtener_todos()

    def obtener_vehiculo_por_placa(self, placa):
        return self._repositorio.obtener_por_placa(placa)
