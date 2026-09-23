import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. ESTRUCTURA DE DATOS (NODO Y LISTA)
# ==========================================

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None  # Apunta siempre al último elemento para facilitar el Undo

    def agregar(self, dato):
        """Agrega un nuevo nodo al final de la lista."""
        nuevo = Nodo(dato)

        if not self.cabeza:
            self.cabeza = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def deshacer(self):
        """Elimina el último nodo agregado (Undo)."""
        if not self.ultimo:
            return None  # La lista está vacía

        nodo_eliminado = self.ultimo

        # Caso 1: Solo había un nodo en la lista
        if self.cabeza == self.ultimo:
            self.cabeza = None
            self.ultimo = None
        # Caso 2: Hay más de un nodo
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None

        return nodo_eliminado.dato

    def obtener_elementos(self):
        """Devuelve una lista con todos los elementos actuales para mostrarlos."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos


# ==========================================
# 2. INTERFAZ GRÁFICA (TKINTER)
# ==========================================

class AppDeshacer:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista Doblemente Enlazada - Agregar y Deshacer")
        self.root.geometry("450x400")
        self.root.configure(bg="#1e1e2e")

        self.lista = ListaDoblementeEnlazada()

        # --- Entrada de texto ---
        lbl_instruccion = tk.Label(
            root, text="Ingrese un elemento:", font=("Arial", 11),
            bg="#1e1e2e", fg="#cdd6f4"
        )
        lbl_instruccion.pack(pady=(20, 5))

        self.entry_dato = tk.Entry(root, font=("Arial", 12), width=25)
        self.entry_dato.pack(pady=5)

        # --- Botones ---
        frame_btn = tk.Frame(root, bg="#1e1e2e")
        frame_btn.pack(pady=15)

        btn_agregar = tk.Button(
            frame_btn, text="➕ Agregar", command=self.agregar_elemento,
            bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold"), width=10
        )
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_deshacer = tk.Button(
            frame_btn, text="↩ Deshacer", command=self.deshacer_elemento,
            bg="#f38ba8", fg="#11111b", font=("Arial", 10, "bold"), width=10
        )
        btn_deshacer.grid(row=0, column=1, padx=10)

        # --- Visualización de la Lista ---
        lbl_lista_titulo = tk.Label(
            root, text="Estado actual de la Lista:", font=("Arial", 11, "bold"),
            bg="#1e1e2e", fg="#89b4fa"
        )
        lbl_lista_titulo.pack(pady=(15, 5))

        self.lbl_contenido = tk.Label(
            root, text="[ Lista vacía ]", font=("Arial", 11),
            bg="#2b2b3b", fg="#ffffff", width=40, height=4, relief="groove",
            wraplength=350
        )
        self.lbl_contenido.pack(pady=5)

    def agregar_elemento(self):
        texto = self.entry_dato.get().strip()
        if texto:
            self.lista.agregar(texto)
            self.entry_dato.delete(0, tk.END)
            self.actualizar_vista()
        else:
            messagebox.showwarning("Campo vacío", "Escribe algo para agregar.")

    def deshacer_elemento(self):
        eliminado = self.lista.deshacer()
        if eliminado is None:
            messagebox.showinfo("Información", "No hay elementos para deshacer.")
        else:
            self.actualizar_vista()

    def actualizar_vista(self):
        elementos = self.lista.obtener_elementos()
        if elementos:
            # Mostramos la estructura enlazada gráficamente
            texto_pantalla = " <-> ".join(elementos)
            self.lbl_contenido.config(text=f"None <-> {texto_pantalla} <-> None")
        else:
            self.lbl_contenido.config(text="[ Lista vacía ]")


# ==========================================
# 3. EJECUCIÓN
# ==========================================

if __name__ == "__main__":
    root = tk.Tk()
    app = AppDeshacer(root)
    root.mainloop()