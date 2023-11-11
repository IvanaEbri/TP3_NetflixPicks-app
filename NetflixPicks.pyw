from tkinter import *
import Pmw
from PIL import Image, ImageTk
from app_logic import *

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("NetflixPicks")
        self.root.overrideredirect(True)
        root.iconbitmap(r"Imagenes\\Netflix.ico")
        root.configure(bg="#240B37")

        self.app = NetflixPicks() # Vinculación con el módulo de consultas.

        # Declaracion de variables
        self.current_view = 0
        self.views = []
        self.lista_seleccionados = []
        self.client_name = ""
        self.selection = ""

        try: # Carga de la imagen de fondo de las primeras vistas
            origina_image = Image.open(r"Imagenes\\Fondo NFPKS.jpg")
            image = origina_image.resize((300, 150))
            self.imagen = ImageTk.PhotoImage(image)            
        except:
            print("No se pudo cargar la imagen")

        self.setup_window()
        self.create_widgets()
        self.ini_window()

    def setup_window(self): # Configurar la ventana principal.
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.window_w = window_width

    def create_widgets(self):  # Crea la ventana donde se va a trabajar.
        self.frame0 = Frame(self.root, height=30, bg="Black")  # Marco superior
        self.frame0.pack(side="top", fill="both", expand=False)

        self.frame1 = LabelFrame(self.root, borderwidth=0, bg="#240B37")  # Ventana de trabajo
        self.frame1.pack(fill="both", expand=True, padx=10)

        self.frame2 = LabelFrame(self.root, borderwidth=0, height=30, bg="#240B37")  # Marco inferior
        self.frame2.pack(side="bottom", fill="x", expand=False) 

        cerrar_button = Button(self.frame0, text=" X ", command=self.close_window, borderwidth=0) # Boton para cerrar la app
        cerrar_button.place(relx=0.985, rely=0.2, anchor="ne")
        cerrar_button.config(bg="Black", font=("Helvetica", 12, "bold"), fg="White")

        self.label_title = Label(self.frame0, text="NETFLIXPICKS", height=2) # Titulo de la app
        self.label_title.pack(side="top")
        self.label_title.config(bg="Black", font=("Bebas neue", 14, "bold"), fg="White")
        self.label_title.grid_columnconfigure(0, weight=1)

        balloon = Pmw.Balloon(self.root) # Decorador con la info del boton
        balloon.bind(cerrar_button, "Cerrar")     

        self.next_button = Button(self.frame2, text="Continuar", command=self.next_view, width=12, height=1, bg="#240B37", font=("Bebas neue", 14, "bold"), fg="White", borderwidth=0) # Botón dinámico para avanzar
        self.next_button.pack(side="right", anchor="s", padx=10, pady=10)        
        self.next_button["state"] = "disabled" # Desactivar el botón inicial

    def ini_window(self): # Itinera las veistas cargadas.
        self.q_frame = LabelFrame()
        self.client_name_var = StringVar()
        self.views = [
            self.view1,
            self.view2,
            self.view3,
            self.view4,
            self.view5,
            self.view6
        ]
        self.update_view()

    def next_view(self): # Avanza a la vista siguiente.
        if self.client_name == "":
            self.return_name()

        if self.current_view < len(self.views):
            self.current_view += 1
            self.update_view()

    def view1(self): # Vista Num. 1.
        """Vista inicial que permite conocer a quien se va a asistir."""
        self.label = Label(self.frame1, image=self.imagen, borderwidth=0)
        self.label.pack(pady=10)
          
        self.q_frame = LabelFrame(self.frame1, bg="#240B37", borderwidth=0)
        self.q_frame.pack(fill="none", expand=True)
        self.q_frame.grid_rowconfigure(0, weight=1)

        self.question_label_1 = Label(self.q_frame, text="Por favor ingresa tu nombre o usuario.", bg="#240B37", font=("Bebas neue", 14, "bold"), fg="White")
        self.question_label_1.pack(side="top", pady=10)

        # Variable de texto asociada al cuadro de entrada
        self.client_name_var = StringVar()
        self.usuario = Entry(self.q_frame, textvariable=self.client_name_var,font=(10), width=50, justify="center")
        self.usuario.pack(pady=10, anchor="s")

        self.usuario.bind("<Return>", lambda event=None: self.next_button.invoke()) # Vincular el evento Enter en el cuadro de texto al botón

        self.client_name_var.trace("w", self.enable_button)  # Verificar cuando se ingresa un nombre

        self.usuario.focus_set() # Colocar el cursor en el cuadro de texto al abrir la ventana

    def view2(self): # Vista Num. 2.
        """Vista de bienvenida con las opciones para elegir la asistencia."""
        self.question_label_1 = Label(self.q_frame, text=f"¡BIENVENIDO/A {self.client_name}! \n SELECCIONE UNA OPCIÓN PARA AYUDARLE", bg="#240B37", font=("Bebas neue", 12, "bold"), fg="White", borderwidth=0)
        self.question_label_1.pack(side="top")

        self.q_frame2 = LabelFrame(self.frame1, bg="#240B37", borderwidth=0)
        self.q_frame2.pack(fill="none", expand=False, pady=10)
        self.q_frame2.grid_rowconfigure(0, weight=1)   

        self.button_pelicula = Button(self.q_frame2, relief="raised", text="PELÍCULAS", width=10, height=2, command=self.seleccion_peliculas, compound="center", bg="White", font=("Bebas neue", 12, "bold"), fg="Black")
        self.button_serie = Button(self.q_frame2, relief="raised", text="SERIES", width=10, height=2, command=self.seleccion_series, compound="center", bg="White", font=("Bebas neue", 12, "bold"), fg="Black")
        self.button_pelicula.pack(side=LEFT, padx=15)
        self.button_serie.pack(side=RIGHT, padx=15)

        self.next_button["state"] = "disabled" # Desactivar el botón inicial

    def view3(self): # Vista Num. 3.
        """Vista que permite dar la primera eleccion de las preferencias de busqueda."""
        self.label.destroy()
        self.q_frame2.destroy()
        self.question_label_1 = Label(self.q_frame, text=self.selection.upper(), bg="#240B37", font=("Bebas neue", 16, "bold"), fg="White", borderwidth=0)
        self.question_label_1.pack(side="top", pady=15)

        self.question_label_2 = Label(self.q_frame, text=f"  {self.app.question_text[0]}  ", bg="White", font=("Bebas neue", 16, "bold"), fg="Black", borderwidth=0, height=2)
        self.question_label_2.pack(side="top", pady=10, padx=15)
        self.app.select_options(self.app.question[0])

        self.botones()
 
    def view4(self):  # Vista Num. 4.
        """Vista que permite dar la segunda eleccion de las preferencias de busqueda."""
        self.q_frame2.destroy()
        self.app.comunication[self.app.question[0]]=self.lista_seleccionados
        self.lista_seleccionados = []
        self.question_label_1 = Label(self.q_frame, text=self.selection.upper(), bg="#240B37", font=("Bebas neue", 16, "bold"), fg="White", borderwidth=0)
        self.question_label_1.pack(side="top", pady=15)

        self.question_label_2 = Label(self.q_frame, text=f"  {self.app.question_text[1]}  ", bg="White", font=("Bebas neue", 16, "bold"), fg="Black", borderwidth=0, height=2)
        self.question_label_2.pack(side="top", pady=10)

        self.app.select_options(self.app.question[1])
        self.botones()

    def view5(self): # Vista Num. 5.
        """Vista que permite dar la tercera eleccion de las preferencias de busqueda."""
        self.q_frame2.destroy()
        self.app.comunication[self.app.question[1]]=self.lista_seleccionados
        self.lista_seleccionados = []
        self.question_label_1 = Label(self.q_frame, text=self.selection.upper(), bg="#240B37", font=("Bebas neue", 16, "bold"), fg="White", borderwidth=0)
        self.question_label_1.pack(side="top", pady=15)

        self.question_label_2 = Label(self.q_frame, text=f"  {self.app.question_text[2]}  ", bg="White", font=("Bebas neue", 16, "bold"), fg="Black", borderwidth=0, height=2)
        self.question_label_2.pack(side="top", pady=10)

        self.app.select_options(self.app.question[2])
        self.botones()        

    def view6(self): # Vista Num. 6 y final.
        """Vista final del programa, se muestran los resultados de las busquedas."""
        self.q_frame2.destroy()
        self.app.comunication[self.app.question[2]]=self.lista_seleccionados
        self.question_label_1 = Label(self.q_frame, text=F"¡¡{self.client_name.upper()}!! \n\n LE SUGERIMOS LA SIGUIENTE SELECCION DE {self.selection.upper()}", bg="#240B37", font=("Bebas neue", 16, "bold"), fg="White", borderwidth=0)
        self.question_label_1.pack(side="bottom", pady=10)    
        
        self.next_button.configure(text="Salir", command=self.close_window)

        print(self.app.comunication)

    def update_view(self): # Verifica las vistas, elimina la anterior y carga la nueva.
        if hasattr(self, 'q_frame'):
            for widget in self.q_frame.winfo_children():
                widget.destroy()
        self.views[self.current_view]()
        self.actualizar_boton()
    
    def enable_button(self, *args): # Habilitar el botón si hay texto en el cuadro de texto.
        if len(self.usuario.get()) > 0:
            self.next_button["state"] = "normal"
        else:
            self.next_button["state"] = "disabled"

    def close_window(self): # Cerrar la ventana.
        self.root.destroy()

    def return_name(self, event=None): # Obtiene el nombre de la barra.
        self.client_name = self.client_name_var.get().upper()  

    def seleccion_peliculas(self): # Funciones asignadas a la seleccion de peliculas.
        self.button_pelicula.config(relief="sunken", font=("Bebas neue", 13))
        self.button_serie.config(relief="raised", font=("Bebas neue", 12, "bold"))
        self.next_button["state"] = "normal"
        self.selection = self.app.selection[0]
        self.app.comunication[self.app.selected]= self.selection

    def seleccion_series(self): # Funciones asignadas a la seleccion de series.
        self.button_serie.config(relief="sunken", font=("Bebas neue", 13))
        self.button_pelicula.config(relief="raised", font=("Bebas neue", 12, "bold"))
        self.next_button["state"] = "normal"
        self.selection = self.app.selection[1]
        self.app.comunication[self.app.selected]= self.selection

    def apretar_button(self, boton, texto): # Funcion para cambiar el estado del boton y agregar la selección. 
        if texto in self.lista_seleccionados:
            # Si el botón ya está en la lista, quitarlo
            self.lista_seleccionados.remove(texto)
            boton.config(relief="raised", font=("Bebas neue", 12, "bold"))
        else:
            # Si el botón no está en la lista, agregarlo
            self.lista_seleccionados.append(texto)
            boton.config(relief="sunken", font=("Bebas neue", 13))
            print(texto)   
        self.actualizar_boton()  

    def botones(self): # Funcion que crea los botones segun lo que se necesite. 
        self.button_a = Button(self.q_frame, relief="raised", command=lambda : self.apretar_button(self.button_a, self.app.button1), text=self.app.button1, width=10, height=2, compound="center", bg="White", font=("Bebas neue", 12, "bold"), fg="Black")
        self.button_a.pack(side="left", padx=15, pady=20)

        self.button_b = Button(self.q_frame, relief="raised", command=lambda : self.apretar_button(self.button_b, self.app.button2), text=self.app.button2, width=10, height=2, compound="center", bg="White", font=("Bebas neue", 12, "bold"), fg="Black")
        self.button_b.pack(side="left", padx=15, pady=20)

        self.button_c = Button(self.q_frame, relief="raised", command=lambda : self.apretar_button(self.button_c, self.app.button3), text=self.app.button3, width=10, height=2, compound="center", bg="White", font=("Bebas neue", 12, "bold"), fg="Black")
        self.button_c.pack(side="left", padx=15, pady=20)

        self.button_d = Button(self.q_frame, relief="raised", command=lambda : self.apretar_button(self.button_d, self.app.button4), text=self.app.button4, width=10, height=2, compound="center", bg="White", font=("Bebas neue", 12, "bold"), fg="Black")
        self.button_d.pack(side="left", padx=15)

    def actualizar_boton(self):
        if self.lista_seleccionados:
            self.next_button["state"] = "normal"
        else:
            self.next_button["state"] = "disabled"

    def mostrar_resultados(self):
        
        self.resultados = self.app.result()
        for i in range(len(self.resultados)):
            print(f'{i+1} - {self.resultados[i]}')


def main():
    root = Tk()
    application = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
