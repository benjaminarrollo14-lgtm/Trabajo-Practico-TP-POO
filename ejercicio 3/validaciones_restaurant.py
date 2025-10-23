# //--- MÓDULO DE VALIDACIONES (SOLO PARA RESTAURANT) ---//
# Funciones "humanas" para pedir datos de forma segura.

def validar_string(mensaje):
    """Pide un texto y se asegura de que no esté vacío."""
    while True:
        valor = input(mensaje)
        if valor.strip(): # .strip() saca espacios en blanco
            return valor
        else:
            print("¡Error! No puedes dejar este campo vacío. Intenta de nuevo.")

def validar_decimal_positivo(mensaje):
    """
    Pide un número decimal (float) positivo (como un precio o cantidad).
    Valida que sea un número y que sea mayor a cero.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor_float = float(valor_str)
            
            if valor_float > 0:
                return valor_float # Si es número y es positivo, lo devolvemos
            else:
                print("¡Error! El valor debe ser positivo (mayor a 0).")
                
        except ValueError:
            print(f"¡Error! '{valor_str}' no es un número válido. Intenta de nuevo.")

def validar_booleano_bebida(mensaje):
    """
    Pide 'S' o 'N' y devuelve un valor Booleano (True/False).
    'S' (Sí) -> True (Es bebida)
    'N' (No) -> False (No es bebida, es comida)
    """
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "S" or respuesta == "SI":
            return True # Es bebida
        elif respuesta == "N" or respuesta == "NO":
            return False # No es bebida
        else:
            print("Respuesta no válida. Por favor, ingresa 'S' (Sí) o 'N' (No).")

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
