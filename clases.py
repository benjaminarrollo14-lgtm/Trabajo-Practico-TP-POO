# MÓDULO DE CLASES (MODELO DE DATOS) 
# Pibes aca Adefinimos los "moldes" para nuestros objetos.
# Estas clases no "hacen" nada por sí solas, solo
# definen cómo son los Alumnos y las Notas si encuntran algo mal lo anotan y lo cambian porfa.

class Nota:
    """Define la estructura de una nota individual."""
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra
        self.notaExamen = notaExamen

class Alumno:
    """Define la estructura de un alumno y sus métodos."""
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = [] # Un Alumno "TIENE UNA" lista de Notas

    # //--- Métodos del Alumno ---//
    def agregar_nota(self, nota_objeto):
        """Recibe un objeto Nota y lo agrega a la lista interna."""
        self.notas.append(nota_objeto)
        print(f"Nota de {nota_objeto.catedra} agregada correctamente.")

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de las notas del alumno."""
        if len(self.notas) == 0:
            return 0 # Para evitar la división por cero si no tiene notas

        suma_total = 0
        for nota in self.notas:
            suma_total += nota.notaExamen

        return suma_total / len(self.notas)
