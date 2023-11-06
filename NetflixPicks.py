from tkinter import *
import Pmw

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("NetflixPicks")
        self.root.overrideredirect(True)
        
        self.setup_window()
        self.create_widgets()

    def setup_window(self): # Configurar la ventana principal
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def create_widgets(self):  # Crea la ventana donde se va a trabajar
        self.frame0 = Frame(self.root, height=40)  # Marco superior
        self.frame0.pack(side="top", fill="both", expand=False)

        self.frame1 = LabelFrame(self.root, borderwidth=0)  # Ventana de trabajo
        self.frame1.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame2 = LabelFrame(self.root, borderwidth=0, height=30)  # Marco inferior
        self.frame2.pack(side="bottom", fill="both", expand=False)  

        cerrar_button = Button(self.frame0, text=" x ", background="red", command=self.close_window) # Boton para cerrar la app
        cerrar_button.place(relx=0.985, rely=0.2, anchor="ne")
        cerrar_button.config(font=("Helvetica", 12, "bold"))

        self.label_title = Label(self.frame0, text="NetflixPicks", height=2) # Titulo de la app
        self.label_title.pack(side="top")
        self.label_title.config(font=("Calibri", 12, "bold"))
        self.label_title.grid_columnconfigure(0, weight=1)

        balloon = Pmw.Balloon(self.root) # Decorador con la info del boton
        balloon.bind(cerrar_button, "Cerrar")

        next_button = Button(self.frame2, text="Continuar", width=12, height=2) # Botón dinámico para avanzar
        next_button.pack(side="right", anchor="s", padx=10, pady=10)

        self.question_window()

    def question_window(self, *args): # Ventana dinámica que cambia con las preguntas
        self.q_frame = LabelFrame(self.frame1)
        self.q_frame.pack(fill='both', expand=True)
        self.q_frame.grid_rowconfigure(0, weight=1)

        self.question_label_1 = Label(self.q_frame, text="Bienvenido", font=("Calibri", 12))
        self.question_label_1.pack(side="top")

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
