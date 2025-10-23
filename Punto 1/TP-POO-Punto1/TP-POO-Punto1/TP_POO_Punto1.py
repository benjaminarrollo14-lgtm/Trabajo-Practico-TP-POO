#
# PUNTO 1 - CELDAS MATRIZ
#

#Clase Celda con Atributos fila, columna y valor.
class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor

#
class Matriz:
    def __init__(self):
        #Va a almacenar instancias de la clase Celda
        self.celdasMatriz = []

    # Metodos

    #Verifica si la fila y columna ya existen
    def existe_celda(self, fila: int, columna: int) -> bool:
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True #Celda ya existe
        return False #Celda no existe

    def agregar_celda(self, fila: int, columna: int, valor: str) -> bool:
        #Crea una celda valida y la agrega si no existe.
        if self.existe_celda(fila, columna):
            print(f"Error: La celda en ({fila}, {columna}) ya fue asignada.")
            return False
        else:
            #Crea la instancia de la clase Celda
            nueva_celda = Celda(fila, columna, valor)
            #Agrega la instancia a la lista celdasMatriz
            self.celdasMatriz.append(nueva_celda)
            print(f"Celda ({fila}, {columna}) con valor '{valor}' agregada")
            return True

    def mostrar_celdas(self):
        print("\n--- Valores Cargados en la Matriz ---")
        if not self.celdasMatriz:
            print("La matriz esta vacia.")
            return

        for celda in self.celdasMatriz:
            # Usando el metodo __repr__ definido en clase Celda
            print(celda)
        print("---------------")

    def obtener_valor(self, fila: int, columna: int) -> str:
        # Retorna valor almacenado para una fila y columna dada.
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor #Retorna el valor si encuentra la celda
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

def main():
    mi_matriz = Matriz()

    while True:
        #Pide el valor de la celda
        valor = input("Ingrese un valor para la celda (O ingrese 'FIN' para terminar): ").strip()

        #Condicion de salida
        if valor.upper() == "FIN":
            break

        try:
            #Pide la posicion (Filas y columnas)
            fila = int(input("Ingrese la fila (entero): ").strip())
            columna = int(input("Ingrese la columna (entero): ").strip())

            #Agrega la celda
            mi_matriz.agregar_celda(fila, columna, valor)

        except ValueError:
            print("Error: Debe ingresar numeros enteros como filas y columnas (Numeros sin decimales)")

    mi_matriz.mostrar_celdas()

    print("\n--- Busqueda de Valor ---")
    try:
        f_buscar = int(input("Ingrese la fila para buscar: ").strip())
        c_buscar = int(input("Ingrese la columna para buscar: ").strip())

        resultado = mi_matriz.obtener_valor(f_buscar, c_buscar)
        print(f"Resultado de la busqueda en ({f_buscar}, {c_buscar}): {resultado}")
    except ValueError:
        print("Error: La fila y la columna de busqueda deben ser numeros enteros (Numeros sin decimales)")

if __name__ == "__main__":
    main()