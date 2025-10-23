# //--- ARCHIVO PRINCIPAL (EJERCICIO 5: GESTIÓN BARRIO) ---//
# Este programa permite cargar 1 barrio, con N viviendas,
# y cada vivienda con N habitaciones. Al final, ejecuta
# todos los métodos de cálculo pedidos.

from clases_barrio import Habitacion, Vivienda, Barrio
from validaciones_barrio import (validar_string, validar_entero_positivo,
                                 validar_decimal_positivo, validar_si_no)

def main():
    """Función principal que orquesta la carga y el reporte."""
    print("--- Bienvenido al Sistema de Gestión de Barrios ---")
    
    # //--- 1. CARGA DEL BARRIO ---//
    barrio_nombre = validar_string("Ingrese nombre del Barrio: ")
    barrio_empresa = validar_string(f"Constructora de '{barrio_nombre}': ")
    
    # Creamos el objeto principal
    mi_barrio = Barrio(barrio_nombre, barrio_empresa)
    print(f"¡Barrio '{mi_barrio.nombre}' creado!")

    # //--- 2. BUCLE DE CARGA DE VIVIENDAS ---//
    while True:
        print("\n--- Cargando Nueva Vivienda ---")
        viv_calle = validar_string("  Calle: ")
        viv_num = validar_entero_positivo(f"  Número de calle (para {viv_calle}): ")
        viv_manz = validar_string("  Manzana (ej: 'A', 'B-10'): ")
        viv_casa = validar_entero_positivo("  Número interno de casa: ")
        viv_terr = validar_decimal_positivo("  Superficie del Terreno (m²): ")
        
        # Creamos el objeto Vivienda
        vivienda_actual = Vivienda(viv_calle, viv_num, viv_manz, viv_casa, viv_terr)

        # //--- 3. BUCLE DE CARGA DE HABITACIONES ---//
        while True:
            print(f"\n  --- Agregando habitaciones a {viv_calle} {viv_num} ---")
            hab_nombre = validar_string("    Nombre de habitación (ej: Cocina, Dormitorio 1): ")
            hab_m2 = validar_decimal_positivo(f"    Metros cuadrados de '{hab_nombre}': ")
            
            # Creamos el objeto Habitacion
            habitacion_actual = Habitacion(hab_nombre, hab_m2)
            
            # Asociamos la habitación con la vivienda
            vivienda_actual.agregar_habitacion(habitacion_actual)
            
            if validar_si_no("    ¿Agregar otra habitación a esta vivienda? (S/N): ") == "N":
                break # Rompe el bucle de HABITACIONES

        # Asociamos la vivienda (ya con sus habitaciones) con el barrio
        mi_barrio.agregar_vivienda(vivienda_actual)
        
        if validar_si_no("\n¿Desea agregar otra vivienda al barrio? (S/N): ") == "N":
            break # Rompe el bucle de VIVIENDAS

    # //--- 4. ZONA DE REPORTE FINAL ---//
    # Aquí ejecutamos todos los métodos pedidos 
    
    print("\n\n==============================================")
    print(f"      REPORTE FINAL DEL BARRIO: {mi_barrio.nombre}")
    print(f"      Constructora: {mi_barrio.empresaConstructora}")
    print("==============================================")
    
    if len(mi_barrio.viviendas) == 0:
        print("El barrio no tiene viviendas cargadas.")
        return # Termina el programa

    # --- Ejecución Método (a) ---
    total_terreno_barrio = mi_barrio.getSuperficieTotalTerreno()
    print(f"[Método a] Superficie TOTAL del terreno del barrio: {total_terreno_barrio:.2f} m²")

    # --- Ejecución Método (c) y (d) ---
    # (Calculamos 'd' primero, ya que 'c' se prueba dentro de 'd')
    print("\nCalculando superficie cubierta...")
    total_cubierta_barrio = mi_barrio.getSuperficieTotalCubierta()
    print(f"[Método d] Superficie TOTAL CUBIERTA del barrio: {total_cubierta_barrio:.2f} m²")
    
    # --- Ejecución Método (b) ---
    print("\n--- Consultar Terreno por Manzana ---")
    manzana_consulta = validar_string("Ingrese la manzana que desea consultar: ")
    total_terreno_manzana = mi_barrio.getSuperficieTotalTerrenoXManzana(manzana_consulta)
    
    if total_terreno_manzana > 0:
        print(f"[Método b] Superficie de terreno para la manzana '{manzana_consulta}': {total_terreno_manzana:.2f} m²")
    else:
        print(f"[Método b] No se encontraron viviendas en la manzana '{manzana_consulta}'.")

    print("\n==============================================")
    print(f"Gestión finalizada. Total de viviendas en el barrio: {len(mi_barrio.viviendas)}")


# //--- PUNTO DE ARRANQUE ---//
if __name__ == "__main__":
    main()
