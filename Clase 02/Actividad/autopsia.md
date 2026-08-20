# Autopsia del Error: Alias de Memoria entre Cajas
1. El Código Defectuoso
El sistema anterior inicializaba las dos cajas de la tienda compartiendo la misma estructura en memoria:

# Código defectuoso original
carrito_compartido = crear_carrito()
caja_1 = carrito_compartido
caja_2 = carrito_compartido

# Al registrar un producto desde la caja_2:
agregar(caja_2, ("Gaseosa", 2500.0), 1)
Al consultar obtener_total_unidades(caja_1), el producto también aparecía en la caja 1, modificando ambas cajas al tiempo.

2. Diagramas del Modelo de Memoria
Estado Inicial (Antes de modificar caja_2)
caja_1 y caja_2 son dos variables independientes en el Stack, pero ambas almacenan un puntero que apunta a la misma dirección de memoria.

[ STACK / Variables ]              [ HEAP / Objetos en Memoria ]

   caja_1 -----------------------> +----------------------------+
                                   |  list (id: 0x7f90)         |
   caja_2 -----------------------> |  []                        |
                                   +----------------------------+

Estado Posterior (Después de agregar(caja_2, ...) )
Al invocar la función agregar sobre caja_2, la lista almacenada en el Heap sufre una mutación. Como caja_1 referencia exactamente a ese mismo objeto en memoria, la modificación es visible desde ambas cajas.

[ STACK / Variables ]              [ HEAP / Objetos en Memoria ]

   caja_1 -----------------------> +----------------------------+
                                   |  list (id: 0x7f90)         |
   caja_2 -----------------------> |  [ (("Gaseosa", 2500), 1) ]|
                                   +----------------------------+

3. Diagnóstico Técnico y Corrección
Diagnóstico
La falla no ocurre por una "copia mal realizada", sino por la presencia de un alias (referencia compartida). En Python, la asignación = no duplica estructuras mutables (como listas o diccionarios); únicamente copia la referencia en memoria. Por ende, caja_1 y caja_2 terminan apuntando al mismo contenedor.

Corrección del Código
Para resolver el problema, cada caja debe invocar directamente la función constructora crear_carrito(), reservando un bloque de memoria totalmente independiente en el Heap para cada variable:


# Código corregido
caja_1 = crear_carrito()
caja_2 = crear_carrito()

# Ahora caja_2 muta únicamente su propio carrito
agregar(caja_2, ("Gaseosa", 2500.0), 1)
Diagrama de Memoria Corregido


[ STACK / Variables ]              [ HEAP / Objetos en Memoria ]

   caja_1 -----------------------> +----------------------------+
                                   |  list (id: 0x7f90)  []     |
                                   +----------------------------+

   caja_2 -----------------------> +----------------------------+
                                   |  list (id: 0x8e12)         |
                                   |  [ (("Gaseosa", 2500), 1) ]|
                                   +----------------------------+