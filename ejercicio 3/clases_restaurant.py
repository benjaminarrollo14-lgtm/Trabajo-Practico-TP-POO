# //--- MÓDULO DE CLASES (SOLO PARA RESTAURANT) ---//
# Aquí definimos los "moldes" para nuestros objetos.

class Ingrediente:
    """Define la estructura de un ingrediente."""
    def __init__(self, nombre, cantidad, unidad_medida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida

class Plato:
    """Define la estructura de un plato del menú."""
    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes = [] # Un Plato "TIENE UNA" lista de Ingredientes

    # //--- Métodos del Plato ---//
    
    def agregar_ingrediente(self, ingrediente_obj):
        """Recibe un objeto Ingrediente y lo agrega a la lista interna."""
        self.ingredientes.append(ingrediente_obj)
        print(f"Ingrediente '{ingrediente_obj.nombre}' agregado al plato.")
