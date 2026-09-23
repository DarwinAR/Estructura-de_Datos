# Especificación del proyecto

## Objetivo

Implementar una lista enlazada que respete el contrato de la lista arreglo, sin usar `list` para almacenar internamente los datos.

## Restricciones

- No se deben modificar las pruebas de la carpeta `Actividad_2`.
- Debe existir una estructura basada en nodos y referencias.
- Debe mantenerse una representación consistente con `cabeza`, `cola` y `tamaño` cuando corresponda.
- Los métodos públicos deben seguir el mismo contrato: `tamaño`, `obtener`, `insertar`, `eliminar`, `buscar`, con el mismo comportamiento esperado.
- Las pruebas deben ejecutarse al final con `pytest`.

## Alcance

1. Revisión del contrato de `ListaArreglo`.
2. Implementación de `Nodo` y de `ListaEnlazada`.
3. Validación de casos límite.
4. Documentación de comparación con 5.000 elementos.
