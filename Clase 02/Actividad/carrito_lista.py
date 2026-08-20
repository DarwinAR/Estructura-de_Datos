def crear_carrito():
    return []


def agregar(carrito, producto, cantidad: int):
    if cantidad <= 0:
        raise ValueError("La cantidad a agregar debe ser mayor a cero.")
    
    for i, (prod, cant) in enumerate(carrito):
        if prod == producto:
            carrito[i] = (prod, cant + cantidad)
            return
    carrito.append((producto, cantidad))


def sacar(carrito, producto, cantidad: int):
    if cantidad <= 0:
        raise ValueError("La cantidad a sacar debe ser mayor a cero.")
    
    for i, (prod, cant) in enumerate(carrito):
        if prod == producto:
            if cantidad > cant:
                raise ValueError("No se puede sacar más unidades de las disponibles.")
            elif cantidad == cant:
                carrito.pop(i)
            else:
                carrito[i] = (prod, cant - cantidad)
            return
            
    raise ValueError("El producto no está en el carrito.")


def obtener_cantidad(carrito, producto):
    for prod, cant in carrito:
        if prod == producto:
            return cant
    return 0


def obtener_total_unidades(carrito):
    return sum(cant for _, cant in carrito)


def obtener_total_precio(carrito):
    return sum(prod[1] * cant for prod, cant in carrito)