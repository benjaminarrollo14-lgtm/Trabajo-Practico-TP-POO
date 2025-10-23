# //--- MÓDULO DE VALIDACIONES (EL EXTRA) ---//
# La idea de este archivo es tener funciones "humanas"
# para pedir datos. Es para poder verificar que los datos que ingrese no esten mal,
# estas funciones le volverán a preguntar hasta que sea el dato correcto

def validar_string(mensaje):
    """Pide un texto y se asegura de que no esté vacío."""
    while True:
        valor = input(mensaje)
        if valor.strip(): # .strip() saca espacios en blanco
            return valor
        else:
            print("¡Error! No puedes dejar este campo vacío. Intenta de nuevo.")

def validar_legajo(mensaje, alumnos_existentes):
    """
    Pide un número entero para el legajo.
    Valida que sea un número y que no esté repetido.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor_int = int(valor_str)
            
            # //--- Chequeo de legajo único ---//
            legajo_repetido = False
            for alumno in alumnos_existentes:
                if alumno.legajo == valor_int:
                    legajo_repetido = True
                    break
            
            if legajo_repetido:
                print(f"¡Error! El legajo {valor_int} ya existe. Ingresa uno diferente.")
            else:
                return valor_int # Si es número y no está repetido, lo devolvemos

        except ValueError:
            print(f"¡Error! '{valor_str}' no es un número entero. Intenta de nuevo.")

def validar_nota(mensaje):
    """
    Pide un número decimal (float) para la nota.
    Valida que sea un número y que esté entre 0 y 10.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor_float = float(valor_str)
            
            if 0 <= valor_float <= 10:
                return valor_float # Si es número y está en rango, lo devolvemos
            else:
                print("¡Error! La nota debe estar entre 0 y 10.")
                
        except ValueError:
            print(f"¡Error! '{valor_str}' no es un número válido. Intenta de nuevo.")

def validar_si_no(mensaje):
    """Pide 'S' o 'N' y no avanza hasta tener una respuesta válida."""
    while True:
        respuesta = input(mensaje).strip().upper() # Pasamos a mayúsculas
        if respuesta == "S" or respuesta == "SI":
            return "S"
        elif respuesta == "N" or respuesta == "NO":
            return "N"
        else:
            print("Respuesta no válida. Por favor, ingresa 'S' (Sí) o 'N' (No).")
