import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import carrito_lista
import carrito_dict

@pytest.fixture(params=[carrito_lista, carrito_dict])
def mod(request):
    return request.param


def test_carrito_vacio_retorna_cero(mod):
    c = mod.crear_carrito()
    assert mod.obtener_total_unidades(c) == 0
    assert mod.obtener_total_precio(c) == 0.0
    assert mod.obtener_cantidad(c, ("Manzana", 1500.0)) == 0


def test_agregar_productos_y_acumular_cantidades(mod):
    c = mod.crear_carrito()
    p1 = ("Manzana", 1500.0)
    
    mod.agregar(c, p1, 2)
    mod.agregar(c, p1, 3)
    
    assert mod.obtener_cantidad(c, p1) == 5
    assert mod.obtener_total_unidades(c) == 5
    assert mod.obtener_total_precio(c) == 7500.0


def test_sacar_producto_parcial_y_total(mod):
    c = mod.crear_carrito()
    p1 = ("Leche", 3000.0)
    
    mod.agregar(c, p1, 4)
    mod.sacar(c, p1, 2)
    assert mod.obtener_cantidad(c, p1) == 2
    
    mod.sacar(c, p1, 2)  # Llega a cero, debe eliminarse
    assert mod.obtener_cantidad(c, p1) == 0
    assert mod.obtener_total_unidades(c) == 0


def test_sacar_producto_inexistente_lanza_error(mod):
    c = mod.crear_carrito()
    p1 = ("Pan", 2000.0)
    
    with pytest.raises(ValueError):
        mod.sacar(c, p1, 1)


def test_sacar_mas_de_lo_existente_lanza_error(mod):
    c = mod.crear_carrito()
    p1 = ("Pan", 2000.0)
    mod.agregar(c, p1, 2)
    
    with pytest.raises(ValueError):
        mod.sacar(c, p1, 5)


def test_agregar_cantidad_invalida_lanza_error(mod):
    c = mod.crear_carrito()
    p1 = ("Café", 5000.0)
    
    with pytest.raises(ValueError):
        mod.agregar(c, p1, 0)
        
    with pytest.raises(ValueError):
        mod.agregar(c, p1, -3)


def test_sacar_cantidad_invalida_lanza_error(mod):
    c = mod.crear_carrito()
    p1 = ("Café", 5000.0)
    mod.agregar(c, p1, 2)
    
    with pytest.raises(ValueError):
        mod.sacar(c, p1, 0)
        
    with pytest.raises(ValueError):
        mod.sacar(c, p1, -1)