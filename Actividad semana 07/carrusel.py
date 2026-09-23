import tkinter as tk

# ==========================================
# 1. ESTRUCTURA DE DATOS (NODOS Y LISTA)
# ==========================================

class NodoCancion:
    """Nodo individual de la lista circular."""
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None


class PlaylistCircular:
    """Lista Doblemente Enlazada Circular."""
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def agregar_cancion(self, titulo, artista, album, duracion):
        nuevo = NodoCancion(titulo, artista, album, duracion)

        # Caso 1: La lista está vacía
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.actual = nuevo
            return

        # Caso 2: Insertar al final manteniendo los enlaces circulares
        ultimo = self.cabeza.anterior

        ultimo.siguiente = nuevo
        nuevo.anterior = ultimo
        nuevo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo

    def siguiente(self):
        """Avanza al siguiente nodo."""
        if self.actual:
            self.actual = self.actual.siguiente

    def anterior(self):
        """Retrocede al nodo anterior."""
        if self.actual:
            self.actual = self.actual.anterior


# ==========================================
# 2. INTERFAZ GRÁFICA CON TKINTER
# ==========================================

class ReproductorGraficoApp:
    def __init__(self, root, playlist):
        self.root = root
        self.root.title("Reproductor Musical - Lista Circular")
        self.root.geometry("420x360")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.playlist = playlist

        # --- Tarjeta Contenedora Principal ---
        card = tk.Frame(root, bg="#2b2b3b", bd=2, relief="groove")
        card.pack(padx=20, pady=20, fill="both", expand=True)

        # Icono gráfico / Arte de disco
        self.lbl_icono = tk.Label(
            card, text="💿", font=("Segoe UI Emoji", 42), bg="#2b2b3b", fg="#89b4fa"
        )
        self.lbl_icono.pack(pady=(15, 5))

        # Título de la canción
        self.lbl_titulo = tk.Label(
            card, text="", font=("Arial", 14, "bold"), bg="#2b2b3b", fg="#ffffff"
        )
        self.lbl_titulo.pack(pady=2)

        # Artista
        self.lbl_artista = tk.Label(
            card, text="", font=("Arial", 11), bg="#2b2b3b", fg="#a6adc8"
        )
        self.lbl_artista.pack(pady=1)

        # Álbum y Duración
        self.lbl_detalles = tk.Label(
            card, text="", font=("Arial", 9, "italic"), bg="#2b2b3b", fg="#7f849c"
        )
        self.lbl_detalles.pack(pady=(2, 15))

        # --- Botones de Control ---
        frame_botones = tk.Frame(card, bg="#2b2b3b")
        frame_botones.pack(pady=10)

        # Botón Anterior
        self.btn_ant = tk.Button(
            frame_botones, text="⏮ Anterior", command=self.anterior_cancion,
            bg="#f38ba8", fg="#11111b", font=("Arial", 10, "bold"),
            width=10, relief="flat", cursor="hand2"
        )
        self.btn_ant.grid(row=0, column=0, padx=10)

        # Botón Siguiente
        self.btn_sig = tk.Button(
            frame_botones, text="Siguiente ⏭", command=self.siguiente_cancion,
            bg="#89b4fa", fg="#11111b", font=("Arial", 10, "bold"),
            width=10, relief="flat", cursor="hand2"
        )
        self.btn_sig.grid(row=0, column=1, padx=10)

        # Cargar vista inicial
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        """Refresca la interfaz gráfica con los datos del nodo actual."""
        if self.playlist.actual:
            nodo = self.playlist.actual
            self.lbl_titulo.config(text=nodo.titulo)
            self.lbl_artista.config(text=f"Artista: {nodo.artista}")
            self.lbl_detalles.config(text=f"Álbum: {nodo.album}  •  {nodo.duracion}")
        else:
            self.lbl_titulo.config(text="Playlist vacía")
            self.lbl_artista.config(text="")
            self.lbl_detalles.config(text="")

    def siguiente_cancion(self):
        """Desplaza el puntero 'actual' hacia el nodo siguiente."""
        self.playlist.siguiente()
        self.actualizar_pantalla()

    def anterior_cancion(self):
        """Desplaza el puntero 'actual' hacia el nodo anterior."""
        self.playlist.anterior()
        self.actualizar_pantalla()


# ==========================================
# 3. EJECUCIÓN DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    # Instanciamos la lista circular
    mi_playlist = PlaylistCircular()

    # Agregamos los nodos a la lista circular
    mi_playlist.agregar_cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", "5:55")
    mi_playlist.agregar_cancion("Hotel California", "Eagles", "Hotel California", "6:30")
    mi_playlist.agregar_cancion("Smooth Criminal", "Michael Jackson", "Bad", "4:17")
    mi_playlist.agregar_cancion("Starman", "David Bowie", "Ziggy Stardust", "4:14")

    # Iniciar la interfaz con Tkinter
    root = tk.Tk()
    app = ReproductorGraficoApp(root, mi_playlist)
    root.mainloop()