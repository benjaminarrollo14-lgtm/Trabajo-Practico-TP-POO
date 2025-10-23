#ARCHIVO PRINCIPAL (LÓGICA DEL PROGRAMA)
# Este es el archivo principal pruevenlo aver si funca todo


from clases import Alumno, Nota
from validaciones import (validar_string, validar_legajo, 
                          validar_nota, validar_si_no)

def main():
    """Función principal que orquesta todo el programa."""
    print("--- Bienvenido al Sistema de Carga de Notas ---")
    
    # Esta es la lista principal que contendrá TODOS los objetos Alumno
    lista_alumnos = []

    # //--- BUCLE PRINCIPAL DE CARGA DE ALUMNOS ---//
    while True:
        print("\n--- Cargando Nuevo Alumno ---")
        
        # 1. Pedimos datos del alumno (usando nuestras validaciones)
        nombre = validar_string("Ingrese nombre completo: ")
        # Le pasamos la lista de alumnos para que valide legajos repetidos
        legajo = validar_legajo("Ingrese legajo (ej: 12345): ", lista_alumnos)
        
        # 2. Creamos el objeto Alumno
        alumno_actual = Alumno(nombre, legajo)
        
        print(f"\n--- Cargando Notas para {alumno_actual.nombreCompleto} ---")
        
        # //--- BUCLE INTERNO DE CARGA DE NOTAS ---//
        while True:
            catedra = validar_string("Ingrese nombre de la cátedra: ")
            nota_examen = validar_nota(f"Ingrese nota de {catedra} (0-10): ")
            
            # 2.1 Creamos el objeto Nota
            nueva_nota = Nota(catedra, nota_examen)
            
            # 2.2 Asociamos la nota con el alumno
            alumno_actual.agregar_nota(nueva_nota)
            
            # 2.3 Preguntamos si quiere cargar otra nota
            if validar_si_no("¿Desea cargar otra nota para este alumno? (S/N): ") == "N":
                # Validación: No puede salir sin cargar al menos 1 nota
                if len(alumno_actual.notas) == 0:
                    print("\n¡Atención! Debe cargar al menos una nota para continuar.")
                else:
                    break # Si ya tiene notas, rompe el bucle de NOTAS

        # 3. Agregamos el alumno (ya con sus notas) a la lista principal
        lista_alumnos.append(alumno_actual)
        print(f"¡Alumno {alumno_actual.nombreCompleto} cargado con éxito!")
        
        # 4. Preguntamos si quiere cargar otro alumno
        if validar_si_no("\n¿Desea cargar otro alumno? (S/N): ") == "N":
            break # Rompe el bucle de ALUMNOS

    # //--- ZONA DE REPORTE FINAL ---//
    # Cuando salimos del bucle principal, mostramos todo.
    
    print("\n\n==============================================")
    print("      REPORTE FINAL DE ALUMNOS Y NOTAS")
    print("==============================================")
    
    if len(lista_alumnos) == 0:
        print("No se cargó ningún alumno.")
        return # Termina el programa

    for alumno in lista_alumnos:
        print(f"\n----------------------------------------------")
        print(f"ALUMNO: {alumno.nombreCompleto} [Legajo: {alumno.legajo}]")
        print("Notas Cargadas:")
        
        for nota in alumno.notas:
            print(f"  > Cátedra: {nota.catedra} - Nota: {nota.notaExamen}")
            
        # 5. Usamos el método de la clase para obtener el promedio
        promedio = alumno.calcular_promedio()
        print(f"PROMEDIO GENERAL: {promedio:.2f}") # :.2f formatea a 2 decimales

    print(f"\n==============================================")
    print(f"Carga finalizada. Total de alumnos procesados: {len(lista_alumnos)}")

# //--- PUNTO DE ARRANQUE ---//
# Esta es la línea que le dice a Python que empiece
# ejecutando nuestra función 'main' cuando corremos este archivo.
if __name__ == "__main__":
    main()
