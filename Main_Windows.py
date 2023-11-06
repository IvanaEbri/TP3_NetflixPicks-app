import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("NetflixPicks")
        self.root.overrideredirect(True)
        self.root.configure(bg="#240B37")

        # Cargar la imagen de fondo
        try:
            image = Image.open(r"Imagenes\\palomitas.jpg")
            self.background_image = ImageTk.PhotoImage(image)
            transp = Image.open(r"Imagenes\\fondo_transparente.png")
            self.background_transp = ImageTk.PhotoImage(transp)
            
        except:
            print("No se pudo cargar la imagen")      

        # Crear una etiqueta para mostrar la imagen de fondo
        background_label = tk.Label(root, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Función para cerrar la ventana
        def cerrar_ventana():
            self.root.destroy()

        # Botón para cerrar la ventana
        cerrar_button = tk.Button(self.root, text=" x ", command=cerrar_ventana)
        cerrar_button.pack()
        cerrar_button.place(relx=0.98, rely=0.03, anchor="ne")
        cerrar_button.configure(background="red")

        # Calcular las dimensiones de la ventana principal (1/3 de la pantalla)
        window_width = screen_width // 3
        window_height = screen_height // 3

        # Calcular la posición de la ventana al centro de la pantalla
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana principal
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Etiqueta y cuadro de texto para ingresar el nombre del cliente
        self.label = tk.Label(self.root, text="Ingrese su nombre:")
        self.label.pack(pady=10)
        

        # Configura la fuente para el texto en negrita y tamaño grande
        font1 = ("Helvetica", 9, "bold")
        self.label.config(font=font1)
        font2 = ("Helvetica", 12, "bold")
        cerrar_button.config(font=font2)

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

    def enable_button(self, *args): # Habilitar el botón si hay texto en el cuadro de texto
        if len(self.name_entry.get()) > 0:
            self.start_button["state"] = "normal"
        else:
            self.start_button["state"] = "disabled"

    def start_application(self, event=None): # Obtener el nombre del cliente
        client_name = self.name_entry.get()
        
        
        # Ocultar la ventana principal
        self.root.withdraw()

        # Mostrar la ventana de saludo y opciones
        self.show_greeting_window(client_name)

    def show_greeting_window(self, client_name):
        greeting_window = tk.Toplevel(self.root)
        greeting_window.title("NetflixPicks")
        greeting_window.overrideredirect(True)
        
        # Cargar la imagen de fondo
        try:
            image = Image.open("Imagenes/palomitas.jpg")
            self.background_image = ImageTk.PhotoImage(image)
        except:
            print("No se pudo cargar la imagen")

        # Cargar el icono personalizado
        try:
            greeting_window.iconbitmap(r"Imagenes/netflix.ico")
        except:
            print("No se pudo cargar el icono")

        # Crear una etiqueta para mostrar la imagen de fondo
        background_label = tk.Label(greeting_window, image=self.background_image)
        background_label.place(relwidth=1, relheight=1) 
  
        # Establece el mismo tamaño y posición que la ventana principal
        greeting_window.geometry(f"{self.root.winfo_width()}x{self.root.winfo_height()}+{self.root.winfo_x()}+{self.root.winfo_y()}")

        # Crear un cuadro de texto para el saludo
        greeting_label = tk.Label(greeting_window, text=f"Bienvenido/a, {client_name}!\nSelecciona una opción para que te podamos ayudar!")
        greeting_label.pack()

        # Configura la fuente para el texto en negrita y tamaño grande
        font = ("Helvetica", 9, "bold")
        greeting_label.config(font=font)

        # Botones cuadrados al lado uno del otro con imagen de fondo
        movie_button = tk.Button(greeting_window,  text="Películas", width=10, height=2, command=self.select_movie, compound="center")
        series_button = tk.Button(greeting_window, text="Series", width=10, height=2, command=self.select_series, compound="center")

        # Coloca los botones uno al lado del otro
        movie_button.pack(side=tk.LEFT, padx=10)
        series_button.pack(side=tk.LEFT, padx=10)

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
