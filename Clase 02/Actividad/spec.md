# Especificación del TAD Carrito de Compras

## Ambigüedades del Requisito y Decisiones de Diseño
El requisito inicial ("necesito poder meter productos, sacar productos, saber cuántos hay de cada uno y cuánto llevo en total") presenta las siguientes ambigüedades, las cuales se definen a continuación:

### ¿Qué ocurre si se intenta sacar un producto que no está en el carrito?

- Decisión: Se lanzará una excepción de tipo ValueError.

- Razón: Intentar eliminar un producto inexistente indica un error de flujo en el punto de venta. Ocultarlo de manera silenciosa podría causar inconsistencias en el inventario o en la caja.

### ¿Qué sucede al ingresar o quedar con cantidad 0 de un producto?

- Decisión: Intentar agregar 0 unidades de un producto lanza un ValueError. Si al decrementar la cantidad de un producto existente mediante sacar() su cantidad llega exactamente a 0, el producto se elimina automáticamente de la estructura interna.

- Razón: Mantener registros con cantidad cero ensucia la representación gráfica del carrito y consume memoria innecesariamente. Las operaciones deben alterar cantidades positivas.

### ¿El carrito admite cantidades negativas?

- Decisión: No. Intentar agregar o retirar cantidades menores o iguales a cero lanzará un ValueError.

- Razón: Las cantidades deben representar magnitudes físicas reales. Reducir elementos debe hacerse explícitamente mediante la función sacar.

### ¿Qué devuelve «cuánto llevo» si el carrito está vacío?

- Decisión: obtener_total_unidades() retorna 0, obtener_total_precio() retorna 0.0, y consultar la cantidad de un producto ausente mediante obtener_cantidad(producto) retorna 0.

- Razón: Permite consultar los totales en la interfaz de la caja sin obligar al programa principal a capturar excepciones solo para mostrar subtotales en cero.

## Contrato Formal del TAD Carrito
### Tipos de Datos
- Producto: Tupla (nombre: str, precio: float)

- Cantidad: Entero strictly positivo (int > 0)

## Operaciones del TAD
- crear_carrito() -> Carrito: Crea e inicializa un carrito vacío.

- agregar(carrito, producto, cantidad: int) -> None:

  - Precondición: cantidad > 0 y precio >= 0.

  - Postcondición: Si la cantidad enviada es <= 0, lanza ValueError. Si el producto ya existía, suma la cantidad dada. Si no existía, crea el registro.

- sacar(carrito, producto, cantidad: int) -> None:

  - Precondición: El producto debe existir en el carrito y cantidad > 0.

  - Postcondición: Reduce la cantidad del producto. Si la cantidad llega a 0, remueve el producto. Si la cantidad es <= 0, si el producto no existe o la cantidad a sacar supera la existente, lanza ValueError.

- obtener_cantidad(carrito, producto) -> int:

  - Efecto: Retorna las unidades guardadas del producto. Retorna 0 si el producto no está en el carrito.

- obtener_total_unidades(carrito) -> int:

  - Efecto: Retorna la suma total de unidades de todos los productos en el carrito.

- obtener_total_precio(carrito) -> float:

  - Efecto: Retorna la suma del costo total de todos los ítems (cantidad * precio).