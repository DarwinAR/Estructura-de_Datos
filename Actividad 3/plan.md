# Plan de trabajo

## 1. Revisar la base

- Revisar la implementación de `ListaArreglo`.
- Confirmar contrato público con errores esperados y parámetros.

## 2. Implementar nodos y lista enlazada

- Crear `Nodo` con `dato` y `siguiente`.
- Definir `ListaEnlazada` con `cabeza`, `cola` y `tamaño`.
- Implementar insertar, obtener, eliminar y buscar.
- Garantizar que `_cola` se actualice en casos limite.

## 3. Pruebas de extremos

- Lista vacía.
- Un único elemento.
- Borrar primero.
- Borrar último.
- Verificar que `tamaño` quede correcto.

## 4. Comparación con 5.000 elementos

- Medir las operaciones con frecuencias del enunciado.
- Registrar costos teóricos y medidos.
- Calcular el costo diario.
- Formular una recomendación sustentada por medición.

## 5. Validación final

- Ejecutar `pytest` en la carpeta de la actividad.
- Revisar que el repositorio quede ordenado y los archivos estén completos.
