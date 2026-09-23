"""Definición del nodo que se usa para construir una lista enlazada.

Cada nodo almacena un valor y una referencia al siguiente elemento de la
cadena. Esta clase es la pieza base sobre la que se construye la estructura
de datos de la lista enlazada.
"""


class Nodo:
    """Representa un elemento individual de una lista enlazada.

    Atributos:
        dato: valor que guarda el nodo.
        siguiente: referencia al siguiente nodo en la lista; es None cuando
            el nodo es el último.
    """

    def __init__(self, dato, siguiente=None):
        """Crea un nodo con un valor y, opcionalmente, el siguiente enlace."""
        self.dato = dato
        self.siguiente = siguiente

    def __repr__(self):
        """Devuelve una representación legible del nodo para depuración."""
        return f"Nodo({self.dato!r})"
