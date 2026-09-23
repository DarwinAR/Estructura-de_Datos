"""Pruebas de casos límite para la lista enlazada.

Estas pruebas cubren situaciones especiales que suelen romper la lógica de la
estructura, como listas vacías, un solo elemento y eliminación de los extremos.
"""

import pytest
from lista_enlazada import ListaEnlazada, PosicionInvalidaError


def test_lista_vacia():
    """Una lista nueva debe permanecer vacía y con cabeza y cola nulas."""
    lista = ListaEnlazada()
    assert lista.tamaño() == 0
    assert list(lista) == []


def test_lista_con_un_elemento():
    """Con un solo elemento, ambos apuntadores deben referenciar al mismo nodo."""
    lista = ListaEnlazada()
    lista.insertar(0, "único")
    assert lista.tamaño() == 1
    assert lista._cabeza.dato == "único"
    assert lista._cola.dato == "único"
    assert list(lista) == ["único"]


def test_borrar_primero():
    """Eliminando el primer elemento debe actualizar la cabeza y mantener el resto."""
    lista = ListaEnlazada()
    for valor in ["a", "b", "c"]:
        lista.insertar(lista.tamaño(), valor)
    assert lista.eliminar(0) == "a"
    assert list(lista) == ["b", "c"]
    assert lista.tamaño() == 2
    assert lista._cabeza.dato == "b"


def test_borrar_ultimo_actualiza_cola():
    """Si se elimina el último nodo, la cola debe apuntar al nuevo último elemento."""
    lista = ListaEnlazada()
    for valor in ["a", "b", "c"]:
        lista.insertar(lista.tamaño(), valor)
    assert lista.eliminar(2) == "c"
    assert list(lista) == ["a", "b"]
    assert lista.tamaño() == 2
    assert lista._cola.dato == "b"
    assert lista._cola.siguiente is None


def test_eliminar_de_vacia_lanza():
    """Eliminar en una lista vacía debe disparar una excepción de posición inválida."""
    with pytest.raises(PosicionInvalidaError):
        ListaEnlazada().eliminar(0)
