"""Pruebas generales para validar el comportamiento esperado de ambas listas.

Estas pruebas verifican que las implementaciones cumplan con el contrato de una
lista: tamaño, inserción, obtención, borrado y validación de índices.
"""

import pytest

from lista_arreglo import ListaArreglo
from lista_enlazada import ListaEnlazada


IMPLEMENTACIONES = [ListaArreglo, ListaEnlazada]


@pytest.mark.parametrize("implementacion", IMPLEMENTACIONES)
def test_lista_vacia(implementacion):
    """La lista recién creada debe estar vacía y no tener elementos."""
    lista = implementacion()
    assert lista.tamaño() == 0
    assert list(lista) == []


@pytest.mark.parametrize("implementacion", IMPLEMENTACIONES)
def test_insertar_obtener_y_tamaño(implementacion):
    """Se debe poder insertar elementos y leerlos por índice."""
    lista = implementacion()
    lista.insertar(0, "a")
    lista.insertar(1, "c")
    lista.insertar(1, "b")
    assert list(lista) == ["a", "b", "c"]
    assert lista.obtener(1) == "b"
    assert lista.tamaño() == 3


@pytest.mark.parametrize("implementacion", IMPLEMENTACIONES)
def test_eliminar_y_buscar(implementacion):
    """La eliminación debe devolver el valor correcto y la búsqueda debe localizarlo."""
    lista = implementacion()
    for valor in ["a", "b", "a"]:
        lista.insertar(lista.tamaño(), valor)
    assert lista.buscar("a") == 0
    assert lista.buscar("x") == -1
    assert lista.eliminar(1) == "b"
    assert list(lista) == ["a", "a"]


@pytest.mark.parametrize("implementacion", IMPLEMENTACIONES)
def test_posiciones_invalidas(implementacion):
    """Cualquier acceso fuera del rango debe lanzar una excepción de índice."""
    lista = implementacion()
    with pytest.raises(IndexError):
        lista.obtener(0)
    with pytest.raises(IndexError):
        lista.eliminar(0)
    with pytest.raises(IndexError):
        lista.insertar(1, "x")
