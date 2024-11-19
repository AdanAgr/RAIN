import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  
import RecommendationSystem 

class MultiSelectDropdown(tk.Toplevel):
    def __init__(self, parent, options, title="Seleccione opciones", background_image_path=None, icono_image_path="./fonts/icono.png"):
        super().__init__(parent)
        self.title(title)
        self.geometry("800x800")

        # Configurar el ícono de la ventana emergente
        if icono_image_path:
            icon_image = Image.open(icono_image_path)
            icon_photo = ImageTk.PhotoImage(icon_image)
            self.iconphoto(False, icon_photo)

        # Cargar y mostrar la imagen de fondo si se proporciona
        if background_image_path:
            self.bg_image = Image.open(background_image_path)
            self.bg_image = self.bg_image.resize((800, 800), Image.ANTIALIAS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.background_label = tk.Label(self, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Configurar el fondo transparente para los widgets de selección múltiple
        self.options = options
        self.selections = {}

        # Crear un checkbox para cada opción
        for option in options:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self, text=option, variable=var, bg="orange", font=("Milky Vintage", 12))
            chk.pack(anchor="w", padx=10, pady=2)
            self.selections[option] = var

        # Botón para confirmar selección
        self.confirm_button = tk.Button(self, text="Confirmar", command=self.confirm_selection, bg="orange", font=("Milky Vintage", 20))
        self.confirm_button.pack(pady=65)

    def confirm_selection(self):
        """Confirma la selección de opciones marcadas y cierra la ventana."""
        self.selected_options = [option for option, var in self.selections.items() if var.get()]
        self.destroy()

    def get_selected_options(self):
        """Devuelve las opciones seleccionadas después de cerrar el diálogo."""
        return self.selected_options


class App(tk.Tk):
    def __init__(self, icono_image_path="./fonts/icono.png"):
        super().__init__()
        self.title("Sistema de Recomendación")
        self.geometry("800x800")
        self.config(bg="lightblue")

        # Configurar el ícono de la ventana principal
        if icono_image_path:
            icon_image = Image.open(icono_image_path)
            icon_photo = ImageTk.PhotoImage(icon_image)
            self.iconphoto(False, icon_photo)

        # Variables para las imágenes de fondo específicas de cada categoría
        self.background_image_paths = {
            "generos": "./fonts/fondo_generos.jpg",  # Imagen de fondo para generos
            "epoca": "./fonts/fondo_epocas.jpg"      # Imagen de fondo para epoca
        }

        # Variables para almacenar las selecciones del usuario
        self.user_selection = {"generos": [], "epoca": []}
        self.usertags = ""
        self.user_id = tk.StringVar()

        # Etiqueta de introducción
        self.intro_label = tk.Label(self, text="Seleccione sus preferencias:", font=("Cinematografica", 30), bg="lightblue")
        self.intro_label.pack(pady=15)

        # Desplegable de generos
        self.label1 = tk.Label(self, text="generos:", font=("Corleone Due", 30), bg="lightblue")
        self.label1.pack(pady=5)
        self.dropdown1 = ttk.Combobox(self, values=["Seleccione opciones"], state="readonly")
        self.dropdown1.set("Seleccione opciones")
        self.dropdown1.bind("<Button-1>", lambda e: self.show_multiselect("generos", ["Acción", "Aventura", "Animación", "Para todos los públicos", "Comedia", "Policiaca", "Documental", "Drama", "Fantasía", "Cine Negro", "Terror", "Musical", "Misterio", "Romance", "Ciencia Ficción", "Thriller / Suspense", "Cine Bélico", "Western / Vaqueros"], self.dropdown1, "generos"))
        self.dropdown1.pack(pady=5)

        # Desplegable de epoca
        self.label2 = tk.Label(self, text="epoca:", font=("Corleone Due", 30), bg="lightblue")
        self.label2.pack(pady=5)
        self.dropdown2 = ttk.Combobox(self, values=["Seleccione opciones"], state="readonly")
        self.dropdown2.set("Seleccione opciones")
        self.dropdown2.bind("<Button-1>", lambda e: self.show_multiselect("epoca", ["Década de los 30's", "Década de los 40's", "Década de los 50's", "Década de los 60's", "Década de los 70's", "Década de los 80's", "Década de los 90`s", "Década de los 2000", "Actual"], self.dropdown2, "epoca"))
        self.dropdown2.pack(pady=5)

        # Caja de texto para escribir en bruto
        self.label_textbox = tk.Label(self, text="Escriba alguna palabra clave de su interés (máximo 50 palabras):", font=("Milky Vintage", 20), bg="lightblue")
        self.label_textbox.pack(pady=10)
        self.textbox = tk.Text(self, height=10, width=50, wrap="word", font=("Milky Vintage", 20))
        self.textbox.pack(pady=5)

        # Marco para el ID y el botón
        self.id_button_frame = tk.Frame(self, bg="lightblue")
        self.id_button_frame.pack(pady=20)

        # Entrada de texto para el ID de usuario (campo izquierdo)
        self.id_label = tk.Label(self.id_button_frame, text="ID:", font=("Milky Vintage", 20), bg="lightblue")
        self.id_label.grid(row=0, column=0, padx=5)
        self.id_entry = tk.Entry(self.id_button_frame, textvariable=self.user_id, font=("Milky Vintage", 20), width=10, justify="center")
        self.id_entry.grid(row=0, column=1, padx=5)
        self.id_entry.config(validate="key", validatecommand=(self.register(self.validate_id), "%P"))

        # Botón para recomendar (campo derecho)
        self.recommend_button = tk.Button(self.id_button_frame, text="Recomendar", command=self.recommend, font=("Milky Vintage", 24), bg="lightgreen", width=15)
        self.recommend_button.grid(row=0, column=2, padx=5)

    def validate_id(self, new_value):
        """Valida que el ID solo contenga hasta 5 dígitos numéricos."""
        return new_value.isdigit() and len(new_value) <= 5 or new_value == ""

    def get_user_selection(self):
        """Devuelve las selecciones de género y epoca del usuario."""
        return self.user_selection

    def get_user_text_tags(self):
        """Devuelve el texto de la caja de texto en bruto como una lista de palabras."""
        return self.usertags.split()

    def show_multiselect(self, title, options, dropdown_widget, category):
        """Abre el diálogo de selección múltiple y actualiza el desplegable con las selecciones."""
        # Usar la imagen de fondo específica para cada categoría
        background_image_path = self.background_image_paths.get(category)
        multi_select = MultiSelectDropdown(self, options, title, background_image_path)
        self.wait_window(multi_select)
        selected_options = multi_select.get_selected_options()
        dropdown_widget.set(", ".join(selected_options))
        self.user_selection[category] = selected_options

    def recommend(self):
        """Muestra la selección del usuario, almacena las opciones y el texto en las variables correspondientes."""
        # Obtener el texto de la caja y limitarlo a 50 palabras
        raw_text = self.textbox.get("1.0", "end").strip()
        words = raw_text.split()
        if len(words) > 50:
            messagebox.showwarning("Advertencia", "El texto excede el límite de 50 palabras, solo se usarán las primeras 50.")
            raw_text = " ".join(words[:50])

        self.usertags = raw_text
        selected_categories = "\n".join([f"{cat}: {', '.join(options)}" for cat, options in self.user_selection.items()])
        
        # Mostrar ID de usuario junto con la selección
        user_id_text = self.user_id.get() or 99999
        RecommendationSystem.recomendacion(generos= app.get_user_selection["generos"], decadas = app.get_user_selection["epoca"], tags = app.get_user_text_tags(), top_n = 5)

if __name__ == "__main__":
    app = App()
    app.mainloop()  
    print(app.get_user_selection()) 
    print(app.get_user_text_tags()) 
    print(app.user_id.get()) 