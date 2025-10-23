# //--- MÓDULO DE VALIDACIONES (SOLO PARA COMPUTADORA) ---//

def validar_string(mensaje):
    """Pide un texto y se asegura de que no esté vacío."""
    while True:
        valor = input(mensaje)
        if valor.strip(): # saca espacios en blanco 
            return valor
        else:
            print("¡Error! No puedes dejar este campo vacío. Intenta de nuevo.")

def validar_entero_positivo(mensaje):
    """
    Pide un número entero positivo (como una cantidad).
    Valida que sea un número y que sea mayor a cero.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor_int = int(valor_str)
            
            if valor_int > 0:
                return valor_int # Si es número y es positivo, lo devolvemos
            else:
                print("¡Error! El valor debe ser positivo (mayor a 0).")
                
        except ValueError:
            print(f"¡Error! '{valor_str}' no es un número entero válido. Intenta de nuevo.")

def validar_decimal_positivo(mensaje):
    """
    Pide un número decimal (float) positivo (como un precio).
    Valida que sea un número y que sea mayor a cero.
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor_float = float(valor_str)
            
            if valor_float > 0:
                return valor_float # Si es un número y es positivo, lo devolvemos
            else:
                print("¡Error! El valor debe ser positivo (mayor a 0).")
                
        except ValueError:
            print(f"¡Error! '{valor_str}' no es un número válido. Intenta de nuevo.")

def validar_si_no(mensaje):
    """Pide 'S' o 'N' y no avanza hasta tener una respuesta válida."""
    while True:
        respuesta = input(mensaje).strip().upper() # Las convertimos a mayúsculas para no aver errores
        if respuesta == "S" or respuesta == "SI":
            return "S"
        elif respuesta == "N" or respuesta == "NO":
            return "N"
        else:
            print("Respuesta no válida. Por favor, ingresa 'S' (Sí) o 'N' (No).")
