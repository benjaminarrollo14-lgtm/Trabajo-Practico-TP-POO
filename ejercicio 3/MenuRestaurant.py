# //--- ARCHIVO PRINCIPAL (EJERCICIO 3: RESTAURANT) ---//
# Este es el programa que se encarga de cargar el menú del restaurant.


# Importamos desde los archivos de este ejecio ejercicio el cual lo hice aparte porque me dio problemas
from clases_restaurant import Ingrediente, Plato
from validaciones_restaurant import (validar_string, validar_decimal_positivo, 
                                     validar_booleano_bebida, validar_si_no)

def main():
    """Función principal que orquesta la carga del menú."""
    print("--- Bienvenido al Sistema de Carga de Menú ---")
    
    # Esta es la lista principal que contendrá TODOS los objetos Plato
    platos_menu = []

    # //--- BUCLE PRINCIPAL DE CARGA DE PLATOS ---//
    while True:
        print("\n--- Cargando Nuevo Plato ---")
        
        # 1. Pedimos datos del Plato
        nombre = validar_string("Ingrese nombre del plato: ")
        precio = validar_decimal_positivo(f"Ingrese precio para '{nombre}': $")
        es_bebida = validar_booleano_bebida(f"¿'{nombre}' es una bebida? (S/N): ")
        
        # 2. Creamos el objeto Plato (reecho porque lo entendi mal)
        plato_actual = Plato(nombre, precio, es_bebida)
        
        # //--- ZONA DE CARGA DE INGREDIENTES ---//
        # La consigna dice: "Si el plato es de tipo Bebida entonces no 
        # [cite_start]se deben solicitar los ingredientes" ya corregido*
        
        if not plato_actual.esBebida: # Si NO es bebida (o sea, es comida)
            print(f"\n--- Cargando Ingredientes para {plato_actual.nombreCompleto} ---")
            
            while True:
                # 2.1 Pedimos datos del Ingrediente
                ing_nombre = validar_string("  Nombre del ingrediente: ")
                ing_cant = validar_decimal_positivo(f"  Cantidad de '{ing_nombre}': ")
                ing_unidad = validar_string(f"  Unidad de medida (ej: gr, kg, unidad): ")
                
                # 2.2 Creamos el objeto Ingrediente
                nuevo_ingrediente = Ingrediente(ing_nombre, ing_cant, ing_unidad)
                
                # 2.3 Asociamos el ingrediente con el plato
                plato_actual.agregar_ingrediente(nuevo_ingrediente)
                
                # 2.4 Preguntamos si quiere cargar otro ingrediente
                if validar_si_no("¿Desea agregar otro ingrediente a este plato? (S/N): ") == "N":
                    # [cite_start]Validación: "obligatorio que se asigne al menos 1 ingrediente" 
                    if len(plato_actual.ingredientes) == 0:
                        print("\n¡Atención! Debe cargar al menos 1 ingrediente para este plato.")
                    else:
                        break # Si ya tiene ingredientes, rompe el bucle de INGREDIENTES
        
        else: # Si SÍ es bebida
            print(f"'{plato_actual.nombreCompleto}' es una bebida, no se cargan ingredientes.")

        # 3. Agregamos el plato (ya con/sin ingredientes) a la lista principal
        platos_menu.append(plato_actual)
        print(f"¡Plato '{plato_actual.nombreCompleto}' cargado al menú!")
        
        # 4. Preguntamos si quiere cargar otro plato
        if validar_si_no("\n¿Desea cargar otro plato al menú? (S/N): ") == "N":
            break # Rompe el bucle de PLATOS

    # //--- ZONA DE REPORTE FINAL (IMPRESIÓN DEL MENÚ) ---//
    # [cite_start]Cuando salimos del bucle, mostramos el menú con el formato pedido [cite: 868-879]
    
    print("\n\n==============================================")
    print("                MENÚ DEL RESTAURANT")
    print("==============================================")
    
    if len(platos_menu) == 0:
        print("El menú está vacío. No se cargó ningún plato.")
        return # Termina el programa

    for plato in platos_menu:
        print(f"\n{plato.nombreCompleto}")
        print(f"Precio: ${plato.precio}")
        
        # Si NO es bebida Y TIENE ingredientes, los mostramos
        if not plato.esBebida and len(plato.ingredientes) > 0:
            print("Ingredientes:")
            # [cite_start]Imprimimos la cabecera de la tabla [cite: 873-875]
            print(f"  {'Nombre':<20} | {'Cantidad':<10} | {'Unidad de Medida':<15}")
            print(f"  {'-'*20:<20} | {'-'*10:<10} | {'-'*15:<15}")
            
            for ing in plato.ingredientes:
                # Usamos f-strings con formato para que se alinee lindo
                print(f"  {ing.nombre:<20} | {ing.cantidad:<10} | {ing.unidad_medida:<15}")
    
    print(f"\n==============================================")
    print("Fin del menú.")

# //--- PUNTO DE ARRANQUE ---//
if __name__ == "__main__":
    main()
