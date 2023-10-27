import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("NetflixPicks")

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las dimensiones de la ventana principal (1/3 de la pantalla)
        window_width = screen_width // 3
        window_height = screen_height // 3

        # Calcular la posición de la ventana al centro de la pantalla
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana principal
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Etiqueta y cuadro de texto para ingresar el nombre del cliente
        self.label = tk.Label(root, text="Ingrese su nombre:")
        self.label.pack(pady=10)

        # Variable de texto asociada al cuadro de entrada
        self.client_name_var = tk.StringVar()
        self.name_entry = tk.Entry(root, textvariable=self.client_name_var)
        self.name_entry.pack(expand=True, pady=10)

        # Crear un marco para los botones y centrarlos
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True)

        # Botón para iniciar la aplicación
        self.start_button = ttk.Button(button_frame, text="Iniciar Aplicación", command=self.start_application)
        self.start_button.grid(row=0, column=0)

        # Centra los botones horizontalmente en el frame
        button_frame.grid_columnconfigure(0, weight=1)

        # Centra el frame verticalmente en la ventana
        button_frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento Enter en el cuadro de texto al botón
        self.name_entry.bind("<Return>", self.start_application)

        # Desactivar el botón inicial
        self.start_button["state"] = "disabled"

        # Verificar cuando se ingresa un nombre
        self.client_name_var.trace("w", self.enable_button)

    def enable_button(self, *args):
        # Habilitar el botón si hay texto en el cuadro de texto
        if len(self.name_entry.get()) > 0:
            self.start_button["state"] = "normal"
        else:
            self.start_button["state"] = "disabled"

    def start_application(self, event=None):
        # Obtener el nombre del cliente
        client_name = self.name_entry.get()
        
        # Ocultar la ventana principal
        self.root.withdraw()

        # Mostrar la ventana de saludo y opciones
        self.show_greeting_window(client_name)

    def show_greeting_window(self, client_name):
        greeting_window = tk.Toplevel(self.root)
        greeting_window.title("NetflixPicks")

        # Establece el mismo tamaño y posición que la ventana principal
        greeting_window.geometry(f"{self.root.winfo_width()}x{self.root.winfo_height()}+{self.root.winfo_x()}+{self.root.winfo_y()}")

        # Crear un cuadro de texto para el saludo
        greeting_label = tk.Label(greeting_window, text=f"Bienvenido, {client_name}!\nSelecciona una opcion para que te podamos ayudar!")
        greeting_label.pack()

        # Crear un marco para los botones y centrarlos
        button_frame = tk.Frame(greeting_window)
        button_frame.pack(expand=True)

        # Botones cuadrados al lado uno del otro
        movie_button = tk.Button(button_frame, text="Películas", width=10, height=2, command=self.select_movie)
        series_button = tk.Button(button_frame, text="Series", width=10, height=2, command=self.select_series)

        movie_button.pack(side=tk.LEFT, padx=10)
        series_button.pack(side=tk.LEFT, padx=10)

        # Centra los botones horizontalmente en el frame
        button_frame.grid_columnconfigure(0, weight=1)

        # Centra el frame verticalmente en la ventana
        button_frame.grid_rowconfigure(0, weight=1)


    def select_movie(self):
        # Lógica para seleccionar película
        pass

    def select_series(self):
        # Lógica para seleccionar serie
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
