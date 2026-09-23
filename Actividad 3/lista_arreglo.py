"""Implementación de una lista usando un arreglo dinámico.

La estructura guarda los elementos en un vector y mantiene el tamaño del
contenido por separado. Cuando el arreglo se llena, se crea uno nuevo con mayor
capacidad y se copian los datos existentes.
"""

# Dependencia: definido en la semana 04.
# Si ya lo tienes implementado, usa tu propia versión.

from array import array


class PosicionInvalidaError(IndexError):
    """Se lanza cuando se intenta acceder a una posición inexistente."""


class ListaArreglo:
    """Lista basada en un arreglo con capacidad dinámica.

    La lista soporta inserciones, eliminaciones, búsquedas por valor y acceso por
    posición. La estructura mantiene el contenido contiguo en memoria, lo que
    hace que el acceso por índice sea muy rápido.
    """

    CAPACIDAD_INICIAL = 4

    def __init__(self):
        """Inicializa una lista vacía con capacidad inicial y tamaño cero."""
        self._capacidad = self.CAPACIDAD_INICIAL
        self._datos = [None] * self._capacidad
        self._tamaño = 0

    def tamaño(self):
        """Devuelve la cantidad de elementos almacenados."""
        return self._tamaño

    def obtener(self, posicion):
        """Retorna el elemento que está en la posición indicada."""
        self._validar(posicion, incluir_final=False)
        return self._datos[posicion]

    def insertar(self, posicion, elemento):
        """Inserta un elemento en una posición determinada.

        Si el arreglo está lleno, se redimensiona antes de realizar la inserción
        para conservar el espacio necesario para el nuevo elemento.
        """
        self._validar(posicion, incluir_final=True)
        if self._tamaño == self._capacidad:
            self._redimensionar(self._capacidad * 2)
        # Se desplazan los elementos hacia la derecha para abrir hueco.
        for i in range(self._tamaño, posicion, -1):
            self._datos[i] = self._datos[i - 1]
        self._datos[posicion] = elemento
        self._tamaño += 1

    def eliminar(self, posicion):
        """Elimina y devuelve el elemento que está en la posición indicada."""
        self._validar(posicion, incluir_final=False)
        eliminado = self._datos[posicion]
        # Se corren los elementos hacia la izquierda para cubrir el hueco.
        for i in range(posicion, self._tamaño - 1):
            self._datos[i] = self._datos[i + 1]
        self._tamaño -= 1
        self._datos[self._tamaño] = None
        return eliminado

    def buscar(self, elemento):
        """Busca un valor y devuelve su índice o -1 si no existe."""
        for i in range(self._tamaño):
            if self._datos[i] == elemento:
                return i
        return -1

    def _validar(self, posicion, incluir_final):
        """Comprueba que una posición esté dentro del rango permitido."""
        limite = self._tamaño if incluir_final else self._tamaño - 1
        if not 0 <= posicion <= limite:
            raise PosicionInvalidaError(
                f"posicion {posicion} fuera de rango [0, {limite}]"
            )

    def _redimensionar(self, nueva_capacidad):
        """Crea un arreglo nuevo con mayor capacidad y copia el contenido actual."""
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self._tamaño):
            nuevos_datos[i] = self._datos[i]
        self._datos = nuevos_datos
        self._capacidad = nueva_capacidad

    def __len__(self):
        """Permite usar len(lista) como el tamaño actual de la estructura."""
        return self._tamaño

    def __getitem__(self, i):
        """Permite acceder al elemento por índice con lista[i]."""
        return self.obtener(i)

    def __iter__(self):
        """Itera sobre los elementos de la lista en orden natural."""
        for i in range(self._tamaño):
            yield self._datos[i]

    def __repr__(self):
        """Representación legible del contenido de la lista para pruebas y depuración."""
        return f"ListaArreglo({list(self)!r})"
