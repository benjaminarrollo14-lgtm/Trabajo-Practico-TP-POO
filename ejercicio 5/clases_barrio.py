# //--- MÓDULO DE CLASES (PARA EJERCICIO 5) ---//

# --- Clase Nivel 3: Habitacion ---
class Habitacion:
    """Define la estructura de una habitación.""" 
    def __init__(self, nombre, metrosCuadrados):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados 

# --- Clase Nivel 2: Vivienda ---
class Vivienda:
    """Define la estructura de una vivienda y sus métodos.""" 
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = [] # Una Vivienda "TIENE UNA" lista de Habitaciones 

    # --- Métodos de Vivienda ---
    def agregar_habitacion(self, hab_obj):
        """Recibe un objeto Habitacion y lo agrega a la lista."""
        self.habitaciones.append(hab_obj)
        print(f"  > Habitación '{hab_obj.nombre}' agregada a la vivienda.")

    def getMetrosCuadradosCubiertos(self):
        """
        Retorna el total de m2 cubiertos (suma de habitaciones).
        Valida que no sea mayor a la superficie del terreno.
        """ 
        total_cubierto = 0
        for hab in self.habitaciones:
            total_cubierto += hab.metrosCuadrados
            
        # Validación pedida en el punto c)
        if total_cubierto > self.superficieTerreno:
            # "emita una excepción con el mensaje..." [cite: 666]
            raise Exception(f"¡Error en Vivienda {self.calle} {self.numero}! La superficie cubierta ({total_cubierto}m²) no puede ser mayor a la del terreno ({self.superficieTerreno}m²).")
            
        return total_cubierto

# --- Clase Nivel 1: Barrio ---
class Barrio:
    """Define la estructura de un Barrio y sus métodos.""" 
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = [] # Un Barrio "TIENE UNA" lista de Viviendas 

    # --- Métodos de Barrio ---
    def agregar_vivienda(self, viv_obj):
        """Recibe un objeto Vivienda y lo agrega a la lista."""
        self.viviendas.append(viv_obj)
        print(f"Vivienda en {viv_obj.calle} {viv_obj.numero} agregada al barrio.")

    def getSuperficieTotalTerreno(self):
        """(Método a) Suma la superficie de terreno de todas las viviendas.""" 
        total_terreno = 0
        for viv in self.viviendas:
            total_terreno += viv.superficieTerreno
        return total_terreno

    def getSuperficieTotalTerrenoXManzana(self, manzana_buscada):
        """(Método b) Suma el terreno solo de una manzana específica.""" 
        total_manzana = 0
        for viv in self.viviendas:
            # Comparamos la manzana de la vivienda con la buscada
            if viv.manzana.upper() == manzana_buscada.upper():
                total_manzana += viv.superficieTerreno
        return total_manzana

    def getSuperficieTotalCubierta(self):
        """
        (Método d) Suma los m2 cubiertos de todas las viviendas.
        Reutiliza el método getMetrosCuadradosCubiertos() de la vivienda.
        """ 
        total_cubierta_barrio = 0
        for viv in self.viviendas:
            # Aquí "reutilizamos" el método del punto c)
            try:
                total_cubierta_barrio += viv.getMetrosCuadradosCubiertos()
            except Exception as e:
                # Si una casa tiene un error, lo informamos pero seguimos sumando
                print(f"  [AVISO] Se omitió una vivienda del cálculo: {e}")
                
        return total_cubierta_barrio
