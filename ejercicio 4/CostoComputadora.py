# //--- ARCHIVO PRINCIPAL (EJERCICIO 4: COMPUTADORA) ---//
# Importamos desde los archivos locales de ESTE ejercicio
from clases_computadora import ComponenteCPU, Computadora
from validaciones_computadora import (validar_string, validar_entero_positivo,
                                      validar_decimal_positivo, validar_si_no)

def cotizar_una_computadora():
    """
    Esta función encapsula toda la lógica para cotizar UNA PC.
    Así podemos llamarla varias veces si el usuario quiere.
    """
    print("\n--- Nueva Cotización de Computadora ---")
    
    # 1. Pedimos datos de la PC
    comp_marca = validar_string("Ingrese marca de la computadora: ")
    comp_modelo = validar_string("Ingrese modelo (ej: X64K): ")
    
    # 2. Creamos el objeto de computadora( ahora correjido creo)
    pc_actual = Computadora(comp_marca, comp_modelo)
    
    print(f"\n--- Cargando Componentes para {pc_actual.marca} {pc_actual.modelo} ---")
    
    # //--- BUCLE DE CARGA DE COMPONENTES ---//
    while True:
        item_nombre = validar_string("  Nombre del componente (ej: Placa Madre): ")
        item_marca = validar_string(f"  Marca de '{item_nombre}': ")
        item_cant = validar_entero_positivo(f"  Cantidad de '{item_nombre}': ")
        item_precio = validar_decimal_positivo(f"  Precio (x unidad) de '{item_nombre}': $")
        
        # 2.1 Creamos el objeto ComponenteCPU
        nuevo_componente = ComponenteCPU(item_nombre, item_marca, item_cant, item_precio)
        
        # 2.2 Asociamos el componente con la PC
        pc_actual.agregar_componente(nuevo_componente)
        
        # 2.3 Preguntamos si quiere cargar otro componente o si no quiere
        if validar_si_no("¿Desea agregar otro componente? (S/N): ") == "N":
            #esto ya es simplemente par agregarle un poco mas de logica
            if len(pc_actual.componentes) == 0:
                print("\n¡Atención! Debe cargar al menos 1 componente para cotizar.")
            else:
                break # Rompe el bucle de COMPONENTES aplicado por lo que dijo el profe en una clase

    # //--- ZONA DE REPORTE FINAL (COTIZACIÓN) ---//
    # Usamos f-strings formateados para que se vea como la tabla del TP
    
    print("\n\n===============================================================================")
    print(f"            COTIZACIÓN: {pc_actual.marca} {pc_actual.modelo}")
    print("===============================================================================")
    print(f" {'Componente':<20} | {'Marca':<15} | {'Cant.':<6} | {'Precio x U':<15} | {'SubTotal':<15}")
    print(f" {'-'*20:<20} | {'-'*15:<15} | {'-'*6:<6} | {'-'*15:<15} | {'-'*15:<15}")

    for comp in pc_actual.componentes:
        subtotal = comp.get_subtotal()
        print(f" {comp.componente:<20} | {comp.marca:<15} | {comp.cantidad:<6} | ${comp.precio:<14.2f} | ${subtotal:<14.2f}")
    print(f"{'-'*79}")
    # Usamos los métodos de la clase para obtener los cálculos segun lo que pidan sin que llegue  tirar error
    precio_venta, costo_total, ganancia = pc_actual.calcular_precio_venta()

    # (alinear a la derecha) para los totales
    print(f"{'Costo Total:':>63} | ${costo_total:<15.2f}")
    print(f"{'Ganancia Sugerida:':>63} | ${ganancia:<15.2f}")
    print(f"{'PRECIO VENTA SUGERIDO:':>63} | ${precio_venta:<15.2f}")
    print("===============================================================================\n")


def main():
    """Función principal que controla el flujo del programa."""
    print("--- Bienvenido al Cotizador de Computadoras ---")
    
    # //--- BUCLE PRINCIPAL DEL PROGRAMA ---//
    # Este bucle maneja la repetición de cotizaciones
    while True:
        cotizar_una_computadora() # Llamamos a la función que hace todo el trabajo
        
        respuesta = validar_si_no("¿Desea cotizar una NUEVA computadora? (S/N): ")
        if respuesta == "N":
            break # Termina el programa
            
    print("\nGracias por usar el cotizador. ¡Hasta luego!")

# //--- PUNTO DE ARRANQUE ---//
if __name__ == "__main__":
    main()
