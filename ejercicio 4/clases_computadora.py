# //--- MÓDULO DE CLASES (SOLO PARA COMPUTADORA) ---//

class ComponenteCPU:
    """Define la estructura de un componente de hardware."""
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    # //--- Métodos del Componente ---//
    
    def get_subtotal(self):
        """Calcula y devuelve el subtotal (cantidad * precio)"""
        return self.cantidad * self.precio

class Computadora:
    """Define la estructura de una PC y sus cálculos."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = [] #los componentes derivados correctamente esta vez

    # //--- Métodos de la Computadora ---//
    
    def agregar_componente(self, comp_obj):
        """Recibe un objeto ComponenteCPU y lo agrega a la lista."""
        self.componentes.append(comp_obj)
        print(f"Componente '{comp_obj.componente}' agregado a la PC.")

    def calcular_costo_total(self):
        """Suma los subtotales de todos sus componentes."""
        costo_total = 0
        for comp in self.componentes:
            # Usamos el método de la otra clase
            costo_total += comp.get_subtotal()
        return costo_total

    def calcular_precio_venta(self):
        """
        Calcula el precio de venta sugerido basado en el costo total,
        [cite_start]tal como lo pide el TP[cite: 903].
        """
        costo = self.calcular_costo_total()
        
        # Aca en el tp diceque 40% si es MENOR a 50000, 30% si es MAYOR a 50000.
      # (Si es exactamente 50000, usará el 40% por esta lógica o deveria serlo)
        [cite_start]
        
        
        if costo > 50000:
            ganancia = costo * 0.30 # 30% de ganancia
        else:
            ganancia = costo * 0.40 # 40% de ganancia
            
        precio_final = costo + ganancia
        
        # Devolvemos todo bien separado para el reporte
        return precio_final, costo, ganancia
