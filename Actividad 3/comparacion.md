# Comparación: lista arreglo vs. lista enlazada

## Frecuencias diarias

- Insertar al principio: 40
- Recorrer toda la lista: 3
- Ir a canción N: 200
- Borrar canción actual: 15

## Complejidad teórica

| Operación | ListaArreglo | ListaEnlazada |
|---|---|---|
| Insertar primero | O(n) | O(1) |
| Recorrer | O(n) | O(n) |
| Ir a N | O(1) | O(n) |
| Borrar actual | O(n) | O(n) |

## Costo diario

$$
Costo\ diario = 40 \times costo\_insertar + 3 \times costo\_recorrer + 200 \times costo\_ir\_a\_N + 15 \times costo\_borrar
$$

La operación que más diferencia a ambas estructuras es `Ir a canción N`, porque la lista enlazada debe recorrer hasta la posición N y la lista arreglo puede acceder por índice directamente.

## Tabla final de comparación

| Operación | Arreglo teórico | Arreglo medido | Enlazada teórica | Enlazada medida |
|---|---|---|---|---|
| Insertar al principio | O(n) | 0.74170618 s | O(1) | 0.00217470 s |
| Recorrer toda la lista | O(n) | 0.00247828 s | O(n) | 0.00263105 s |
| Ir a canción número N | O(1) | 0.00197782 s | O(n) | 0.00222218 s |
| Borrar canción actual | O(n) | 0.06191606 s | O(n) | 0.00219557 s |

Las mediciones se obtuvieron ejecutando `medir_comparacion.py` con 5.000 canciones
y 20 repeticiones por operación. Cada valor corresponde al promedio de una ejecución.

## Costo diario

Con las frecuencias dadas:

- Insertar al principio = 40
- Recorrer = 3
- Ir a canción N = 200
- Borrar actual = 15

$$
Costo\ diario = 40 \times costo\_insertar + 3 \times costo\_recorrer + 200 \times costo\_ir\_a\_N + 15 \times costo\_borrar
$$

Los valores medidos dan:

- Arreglo: 30.99998585 s
- Enlazada: 0.57225078 s

## Recomendación

La lista enlazada gana con las frecuencias actuales.

### ¿Por qué?

La diferencia más fuerte está en `insertar al principio` y `borrar actual`, donde la lista enlazada se comporta mucho mejor que la lista arreglo. Aunque el acceso por posición `Ir a canción N` favorece al arreglo, la frecuencia de inserción y borrado hace que la lista enlazada resulte mucho más eficiente en total.

### ¿Qué tendría que cambiar para invertir la recomendación?

Para que la lista arreglo gane, la frecuencia de `Ir a canción N` tendría que aumentar mucho. Podemos estimar el punto de cambio igualando los costos diarios de cada estructura.

Sea `f` la frecuencia diaria de `Ir a canción N`:

$$
C_{arreglo}(f) = 40 \cdot 0.74170618 + 3 \cdot 0.00247828 + f \cdot 0.00197782 + 15 \cdot 0.06191606
$$

$$
C_{enlazada}(f) = 40 \cdot 0.00217470 + 3 \cdot 0.00263105 + f \cdot 0.00222218 + 15 \cdot 0.00219557
$$

Si igualamos los costos diarios de ambas estructuras, el punto de cambio se alcanza cuando la frecuencia de `Ir a la canción N` crece mucho. Con estas mediciones, ese valor aproximado es de:

- 124.720 accesos por día

Es decir, la lista arreglo solo sería mejor si la operación `Ir a la canción N` ocurriera aproximadamente 124.720 veces al día. Eso está muy lejos de las 200 veces actuales, por lo que la recomendación sigue siendo la lista enlazada.

### PUNTO CLAVE

`Ir a canción N` sí favorece al arreglo, pero no basta para compensar el costo diario de insertar y borrar en la estructura actual. Con las frecuencias reales del enunciado, la lista enlazada es la recomendación correcta.
