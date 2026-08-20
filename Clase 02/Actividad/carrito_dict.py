def crear_carrito():
    return {}


def agregar(carrito, producto, cantidad: int):
    if cantidad <= 0:
        raise ValueError("La cantidad a agregar debe ser mayor a cero.")
    
    if producto in carrito:
        carrito[producto] += cantidad
    else:
        carrito[producto] = cantidad


def sacar(carrito, producto, cantidad: int):
    if cantidad <= 0:
        raise ValueError("La cantidad a sacar debe ser mayor a cero.")
    if producto not in carrito:
        raise ValueError("El producto no está en el carrito.")
    if cantidad > carrito[producto]:
        raise ValueError("No se puede sacar más unidades de las disponibles.")
    
    carrito[producto] -= cantidad
    if carrito[producto] == 0:
        del carrito[producto]


def obtener_cantidad(carrito, producto):
    return carrito.get(producto, 0)


def obtener_total_unidades(carrito):
    return sum(carrito.values())


def obtener_total_precio(carrito):
    return sum(prod[1] * cant for prod, cant in carrito.items())