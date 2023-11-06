from tkinter import *
import Pmw
from PIL import Image, ImageTk
from tkinter import ttk, PhotoImage


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("NetflixPicks")
        self.root.overrideredirect(True)
        root.iconbitmap(r"Imagenes\\Netflix.ico")
        root.configure(bg="#240B37")

        try:
            origina_image = Image.open(r"Imagenes\\Fondo NFPKS.jpg")
            image = origina_image.resize((300, 150))
            self.imagen = ImageTk.PhotoImage(image)
            
        except:
            print("No se pudo cargar la imagen")
        
        self.setup_window()
        self.create_widgets()

        usuario = str

    def setup_window(self): # Configurar la ventana principal
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def pantalla_principal(self):
        pass

    def create_widgets(self):  # Crea la ventana donde se va a trabajar
        self.frame0 = Frame(self.root, height=30, bg="Black")  # Marco superior
        self.frame0.pack(side="top", fill="both", expand=False)

        self.frame1 = LabelFrame(self.root, borderwidth=0, bg="#240B37")  # Ventana de trabajo
        self.frame1.pack(fill="both", expand=True, padx=10)

        self.frame2 = LabelFrame(self.root, borderwidth=0, height=30, bg="#240B37")  # Marco inferior
        self.frame2.pack(side="bottom", fill="both", expand=False)  

        cerrar_button = Button(self.frame0, text=" X ", command=self.close_window, borderwidth=0) # Boton para cerrar la app
        cerrar_button.place(relx=0.985, rely=0.2, anchor="ne")
        cerrar_button.config(bg="Black", font=("Helvetica", 12, "bold"), fg="White")

        self.label = Label(self.frame1, image=self.imagen, borderwidth=0)
        self.label.pack(pady=10)

        self.label_title = Label(self.frame0, text="NETFLIXPICKS", height=2) # Titulo de la app
        self.label_title.pack(side="top")
        self.label_title.config(bg="Black", font=("Bebas neue", 14, "bold"), fg="White")
        self.label_title.grid_columnconfigure(0, weight=1)

        balloon = Pmw.Balloon(self.root) # Decorador con la info del boton
        balloon.bind(cerrar_button, "Cerrar")

        next_button = Button(self.frame2, text="Continuar", width=12, height=2, bg="#240B37", font=("Bebas neue", 14, "bold"), fg="White", borderwidth=0) # Botón dinámico para avanzar
        next_button.pack(side="right", anchor="s", padx=10, pady=10)

        self.ini_window()

    def ini_window(self, *args): # Ventana dinámica que cambia con las preguntas
        self.q_frame = LabelFrame(self.frame1, bg="#240B37", borderwidth=0)
        self.q_frame.pack(fill='both', expand=True)
        self.q_frame.grid_rowconfigure(0, weight=1)        

        self.question_label_1 = Label(self.q_frame, text="Por favor ingresa tu nombre o usuario.", bg="#240B37", font=("Bebas neue", 14, "bold"), fg="White", borderwidth=0)
        self.question_label_1.pack(side="top", pady=10)

        # Variable de texto asociada al cuadro de entrada
        self.client_name_var = StringVar()
        self.usuario = Entry(self.q_frame, textvariable=self.client_name_var, width=50, justify="center")
        self.usuario.pack(pady=10, anchor="s")

        """# Crear un nuevo Frame para alinear los botones horizontalmente
        self.button_frame = LabelFrame(self.q_frame, borderwidth=0)
        self.button_frame.pack(pady=20)

        pelicula_button = Button(self.button_frame, text="Peliculas", width=12, height=2) # Botón dinámico para avanzar
        pelicula_button.pack(side="left", padx=10, pady=10)

        serie_button = Button(self.button_frame, text="Series", width=12, height=2) # Botón dinámico para avanzar
        serie_button.pack(side="left", padx=10, pady=10)
"""
    def close_window(self): # Cerrar la ventana
        self.root.destroy()
"""
    def enable_button(self, opcion_obligatoria, *args): # Habilitar el botón si hay texto en el cuadro de texto
        if len(self.opcion_obligatoria.get()) > 0:
            self.next_button["state"] = "normal"
        else:
            self.next_button["state"] = "disabled"
"""
    
def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
