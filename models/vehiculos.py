import datetime

class Vehiculo:
    def __init__(self, tipo, altura, placa):
        self._tipo = tipo       #_ _ = Privado      _ = Protegido
        
        self._altura = altura
        self._placa = placa
        self._horaEntrada = None
        self._horaSalida = None
        self._espacioAsignado = None
        
    @property
    def tipo(self):
        return self._tipo
    @property
    def tipo(self):
        return self._altura
    @property
    def tipo(self):
        return self._placa
    @property
    def tipo(self):
        return self._horaEntrada
    @property
    def tipo(self):
        return self._horaSalida
    @property
    def tipo(self):
        return self._espacioAsignado
        

class FabricaVehiculos:
    
    @staticmethod
    def crear (tipo, placa):
        if tipo == "carro":
            return Vehiculo("Carro", 1.6, placa)
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
    def calcular_costo(self,vehiculo, horaEntrada, horaSalida):
        if not horaEntrada or not horaSalida:
            return 0
        duracion = horaSalida - horaEntrada
        horas = duracion.total_seconds()/3600
        horas = max(1, horas)
        tipo = vehiculo.tipo.lower()
        return self._tarifas[tipo] * horas

class GestorEspacios:
    def __init__(self):
        self._espacios ={
            "carro": 20,
            "moto":  30,
            "camion":5
        }
    
    def espacios_disponibles(self, tipo):
        return self._espacios[tipo]
    
    def asignar_espacio(self, vehiculo):
        tipo = vehiculo.tipo.lower()
        
        if not self.espacios_disponibles(tipo):
            return False
        
        self._espacios[tipo] -= 1
        return True
    
    def liberar_espacio(self, vehiculo):
        tipo = vehiculo.tipo.lower()
        self._espacios[tipo] += 1
        return True

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
        return self._vehiculos.copy()#Genera una copia del diccionario de vehículos
    
    def existe_placa(self,placa):
        return placa in self._vehiculos

class Parqueadero:
    def __init__(self):
        self._fabrica = FabricaVehiculos() #Llama todas las clases que fueron creadas previamente para usarse
        self._calculadora = CalculadoraTarifa()
        self._gestor_espacios = GestorEspacios()
        self._repositorio = RepositorioVehiculos()
    
    def ingresar_vehiculo(self, tipo, placa):
        try:
            if not self._gestor_espacios.espacios_disponibles(tipo):
                return False, f"No hay espacios disponibles para {tipo}"
            if self._repositorio.existe_placa(placa):
                return False, f"El vehículo con placa {placa} ya se encuentra registrado"
            
            vehiculo = self._fabrica.crear(tipo,placa)
            
            espacio = self._gestor_espacios.asignar_espacio(vehiculo)
            
            vehiculo._horaEntrada = datetime.datetime.now()
            return True, f"Vehículo {tipo} con placas {placa} fue ingresado exitosamente"
        
        except Exception as e:
            return False, str(e)
    
    def retirar_vehiculo(self, placa):
        try:
            vehiculo = self._repositorio.obtener_por_placa(placa)
            if not vehiculo:
                return False, f"El vehículo con placa {placa} no se encuentra en el parqueadero"
            vehiculo_liberado = self._gestor_espacios.liberar_espacio(vehiculo)
            if vehiculo_liberado is False:
                return False, f"No se pudo liberar el vehículo con placas {placa}"
            
            vehiculo.horaSalida = datetime.datetime.now()
            costo = self._calculadora.calcular_costo(vehiculo, vehiculo.horaEntrada, vehiculo.horaSalida)
            
            self._repositorio.eliminar(placa)
            return vehiculo, costo
        except Exception as e:
            return False, str(e)
        
    def consultar_estado(self):
        return self._repositorio.obtener_todos()
    
    def obtener_vehiculo_por_placa(self, placa):
        return self._repositorio.obtener_por_placa(placa)