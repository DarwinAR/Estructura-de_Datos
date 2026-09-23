"""Implementación de una lista enlazada simple.

Cada elemento se guarda en un nodo que conserva una referencia al siguiente.
La estructura permite insertar y eliminar en posiciones específicas sin mover
todos los elementos contiguamente en memoria, aunque el acceso aleatorio exige
recorrer la lista desde la cabeza.
"""

from nodo import Nodo


class PosicionInvalidaError(IndexError):
    """Se lanza cuando una posición no existe en la lista enlazada."""


class ListaEnlazada:
    """Lista enlazada simple con referencia a la cabeza y a la cola.

    La implementación mantiene:
        - _cabeza: primer nodo de la lista.
        - _cola: último nodo de la lista.
        - _tamaño: número de nodos almacenados.
    """

    def __init__(self):
        """Inicializa una lista enlazada vacía."""
        self._cabeza = None
        self._cola = None
        self._tamaño = 0

    def tamaño(self):
        """Devuelve la cantidad de elementos en la lista."""
        return self._tamaño

    def obtener(self, posicion):
        """Obtiene el valor del nodo ubicado en la posición indicada."""
        self._validar(posicion, incluir_final=False)
        return self._nodo_en(posicion).dato

    def insertar(self, posicion, elemento):
        """Inserta un elemento en la posición indicada.

        Si la posición es 0, se agrega al inicio; si es igual al tamaño, se agrega
        al final; en otro caso, se inserta en el medio.
        """
        self._validar(posicion, incluir_final=True)
        if posicion == 0:
            self._insertar_al_inicio(elemento)
        elif posicion == self._tamaño:
            self._insertar_al_final(elemento)
        else:
            self._insertar_en_medio(posicion, elemento)
        self._tamaño += 1

    def eliminar(self, posicion):
        """Elimina el elemento en la posición indicada y devuelve su valor."""
        self._validar(posicion, incluir_final=False)
        if posicion == 0:
            dato = self._eliminar_primero()
        else:
            dato = self._eliminar_no_primero(posicion)
        self._tamaño -= 1
        return dato

    def buscar(self, elemento):
        """Busca el primer índice donde aparece el elemento; retorna -1 si no existe."""
        actual = self._cabeza
        indice = 0
        while actual is not None:
            if actual.dato == elemento:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1

    def _insertar_al_inicio(self, elemento):
        """Inserta un nuevo nodo al inicio de la lista."""
        nuevo = Nodo(elemento, self._cabeza)
        self._cabeza = nuevo
        if self._cola is None:
            self._cola = nuevo

    def _insertar_al_final(self, elemento):
        """Agrega un nuevo nodo al final de la lista y actualiza la cola."""
        nuevo = Nodo(elemento)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo

    def _insertar_en_medio(self, posicion, elemento):
        """Inserta un nodo entre dos nodos ya existentes."""
        anterior = self._nodo_en(posicion - 1)
        nuevo = Nodo(elemento, anterior.siguiente)
        anterior.siguiente = nuevo

    def _eliminar_primero(self):
        """Elimina el primer nodo y devuelve su dato."""
        nodo = self._cabeza
        self._cabeza = nodo.siguiente
        if self._cabeza is None:
            self._cola = None
        return nodo.dato

    def _eliminar_no_primero(self, posicion):
        """Elimina un nodo que no es el primero, actualizando también la cola si es necesario."""
        anterior = self._nodo_en(posicion - 1)
        objetivo = anterior.siguiente
        dato = objetivo.dato
        anterior.siguiente = objetivo.siguiente
        # Si se elimina el último nodo, la cola debe apuntar al nodo anterior.
        if objetivo.siguiente is None:
            self._cola = anterior
        return dato

    def _nodo_en(self, posicion):
        """Recorre la lista hasta llegar a la posición indicada y devuelve ese nodo."""
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual

    def _validar(self, posicion, incluir_final):
        """Valida que la posición sea válida para la operación solicitada."""
        limite = self._tamaño if incluir_final else self._tamaño - 1
        if not 0 <= posicion <= limite:
            raise PosicionInvalidaError(
                f"posicion {posicion} fuera de rango [0, {limite}]"
            )

    def __len__(self):
        """Permite usar len(lista) para conocer el tamaño actual."""
        return self._tamaño

    def __getitem__(self, i):
        """Permite acceder al elemento con la sintaxis lista[i]."""
        return self.obtener(i)

    def __iter__(self):
        """Genera los elementos de la lista en orden secuencial."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __repr__(self):
        """Muestra una representación legible de la lista enlazada."""
        return f"ListaEnlazada({list(self)!r})"
