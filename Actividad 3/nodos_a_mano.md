# Nodos a mano

## 1) Estado inicial

```text
A -> B -> C -> None
```

- `A` apunta a `B`
- `B` apunta a `C`
- `C` apunta a `None`

Cada nodo tiene dos partes:
- `dato`: el valor almacenado
- `siguiente`: la referencia al siguiente nodo

## 2) Qué pasa si se reasigna `A.siguiente` antes de guardar `B`

```python
B = Nodo("B")
C = Nodo("C")
A = Nodo("A")

A.siguiente = C
# Se pierde la referencia original a B
```

Esto rompe la cadena porque el enlace de `A` se cambia a `C` sin conservar la referencia a `B`.

## 3) Por qué se pierde el acceso a `B`

Si antes de reasignar no guardamos `B` en otra variable, entonces el único camino que conocíamos hacia ese nodo queda cortado:

```text
A -> C -> None
```

`B` queda inaccesible desde la estructura y ya no se puede recorrer desde `A`.

## 4) Orden correcto

La forma segura es:

```python
c = Nodo("C")
b = Nodo("B", c)
a = Nodo("A", b)
```

Primero se guarda la referencia a `B`, y luego se cambia el enlace cuando se quiere reenganchar la cadena:

```python
referencia_b = b
A.siguiente = c
```

Así se conserva la referencia a `B` y se evita perder el acceso a la cadena original.

## Diagrama final

```text
A -> B -> C -> None
```

El orden correcto es fundamental porque los nodos están conectados por referencias y no por índices.
