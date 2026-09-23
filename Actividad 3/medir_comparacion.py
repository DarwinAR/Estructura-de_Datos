"""Mide y compara el rendimiento de dos implementaciones de lista."""

from time import perf_counter  # Importa una función para medir el tiempo con precisión.

from lista_arreglo import ListaArreglo  # Importa la lista basada en un arreglo.
from lista_enlazada import ListaEnlazada  # Importa la lista basada en nodos enlazados.

CANTIDAD_CANCIONES = 5000  # Define la cantidad de elementos usados en cada prueba.
REPETICIONES = 20  # Define cuántas veces se repite cada prueba.


def medir(funcion):  # Recibe la operación cuyo rendimiento se desea medir.
    """Ejecuta una operación varias veces y devuelve su tiempo promedio."""
    inicio = perf_counter()             # Guarda el momento exacto antes de iniciar la prueba.
    for _ in range(REPETICIONES):       # Repite la operación para obtener una medición más estable.
        funcion()                       # Ejecuta la operación recibida.
    tiempo_total = perf_counter() - inicio  # Calcula cuánto duraron todas las repeticiones.
    return tiempo_total / REPETICIONES      # Devuelve el tiempo promedio de una repetición.


def crear_lista(implementacion):  # Recibe el tipo de lista que se va a construir.
    """Crea una lista con 5.000 elementos para las pruebas."""
    lista = implementacion()  # Crea una lista vacía de la implementación recibida.
    for i in range(CANTIDAD_CANCIONES):  # Repite el proceso 5.000 veces.
        lista.insertar(lista.tamaño(), i)  # Inserta cada elemento al final de la lista.
    return lista  # Devuelve la lista completa.


def insertar_al_principio(implementacion):  # Mide el rendimiento de insertar al inicio.
    """Inserta 5.000 elementos en la primera posición."""
    lista = implementacion()  # Crea una lista vacía.
    for i in range(CANTIDAD_CANCIONES):  # Repite la inserción 5.000 veces.
        lista.insertar(0, i)  # Inserta el elemento actual en la posición cero.


def recorrer(implementacion):  # Mide el tiempo de recorrer todos los elementos.
    """Recorre la lista completa y suma sus elementos."""
    lista = crear_lista(implementacion)  # Crea una lista con 5.000 elementos.
    total = 0  # Inicializa el acumulador de la suma.
    for elemento in lista:  # Recorre cada elemento de la lista.
        total += elemento  # Suma el elemento actual al acumulador.
    return total  # Devuelve la suma para completar la operación.


def ir_a_n(implementacion):  # Mide el rendimiento de acceder a una posición concreta.
    """Obtiene el elemento ubicado en la posición 2.500."""
    lista = crear_lista(implementacion)  # Crea una lista con 5.000 elementos.
    return lista.obtener(2500)  # Obtiene el elemento ubicado en la posición central.


def borrar_actual(implementacion):  # Mide el rendimiento de borrar y volver a insertar.
    """Elimina el primer elemento y coloca otro en su lugar."""
    lista = crear_lista(implementacion)  # Crea una lista con 5.000 elementos.
    for i in range(100):  # Repite la simulación 100 veces.
        lista.eliminar(0)  # Elimina el elemento que está en la primera posición.
        lista.insertar(0, i)  # Inserta un nuevo elemento al comienzo.


def ejecutar(implementacion):  # Ejecuta todas las pruebas para un tipo de lista.
    """Devuelve los tiempos medidos para las cuatro operaciones."""
    return {  # Construye un diccionario con cada operación y su tiempo promedio.
        "insertar_primero": medir(lambda: insertar_al_principio(implementacion)),  # Mide insertar al inicio.
        "recorrer": medir(lambda: recorrer(implementacion)),  # Mide recorrer toda la lista.
        "ir_a_n": medir(lambda: ir_a_n(implementacion)),  # Mide acceder a la posición 2.500.
        "borrar_actual": medir(lambda: borrar_actual(implementacion)),  # Mide eliminar y reinsertar.
    }


resultados = {  # Guarda los resultados de las dos implementaciones.
    "arreglo": ejecutar(ListaArreglo),  # Ejecuta las pruebas para la lista arreglo.
    "enlazada": ejecutar(ListaEnlazada),  # Ejecuta las pruebas para la lista enlazada.
}

for nombre, valores in resultados.items():  # Recorre los resultados de cada implementación.
    print(nombre)  # Imprime el nombre de la implementación.
    for operacion, segundos in valores.items():  # Recorre cada operación y su tiempo.
        print(f"  {operacion}: {segundos:.8f} s")  # Muestra el tiempo con ocho decimales.

frecuencias = {  # Define cuántas veces ocurre cada operación durante un día.
    "insertar_primero": 40,  # Se insertan elementos al inicio 40 veces.
    "recorrer": 3,  # Se recorre toda la lista 3 veces.
    "ir_a_n": 200,  # Se accede a una posición 200 veces.
    "borrar_actual": 15,  # Se borra la canción actual 15 veces.
}

for nombre, valores in resultados.items():  # Calcula el costo diario de cada implementación.
    costo = sum(  # Suma el costo de todas las operaciones del día.
        frecuencias[operacion] * valores[operacion]  # Multiplica frecuencia diaria por tiempo medido.
        for operacion in frecuencias  # Repite el cálculo para cada operación.
    )
    print(f"costo_diario_{nombre}: {costo:.8f} s")  # Imprime el costo diario estimado.
