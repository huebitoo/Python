# Importación de las bibliotecas necesarias
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox

# Función que se ejecuta al hacer clic en el botón "Descargar"
def accion():
    # Obtener el enlace del video desde la entrada de texto
    enlace = videos.get()
    
    # Crear un objeto YouTube con el enlace proporcionado
    video = YouTube(enlace)
    
    # Obtener la mejor resolución disponible para el video
    descarga = video.streams.get_highest_resolution()
    
    direccion_personalizada = direccion_entry.get()
    if direccion_personalizada:
        descarga.download(output_path=direccion_personalizada)
    else:
        descarga.download()
    
    # Descarga el video  
    descarga.download()

# Función que muestra una ventana de información sobre el creador
def popup():
    Messagebox.showinfo("Sobre el creador", "Creado solo para la descarga de videos de Youtube, si quieres mas informacion visita mi github https://github.com/huebitoo")

def direccion():
    ruta = direccion_entry.get()
    if ruta:
        Messagebox.showinfo("Cambio de dirección", f"La dirección de descarga se cambió a:\n{ruta}")
    else:
        Messagebox.showwarning("Cambio de dirección", "La dirección de descarga no puede estar vacía.")


# Crear y configurar la ventana principal de Tkinter
root = Tk()
root.config(bd=15)
root.title("Script descargar videos")

# Cargar y mostrar una imagen en la ventana
image = PhotoImage(file="C:/Users/campo/OneDrive/Escritorio/codigo/python/turtle/logo.png")
foto = Label(root, image=image, bd=0)
foto.grid(row=0, column=0)

# Crear un menú en la parte superior de la ventana
menubar = Menu(root)
root.config(menu=menubar)

# Crear un submenú bajo la etiqueta "Para mas información"
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Para mas información", menu=helpmenu)

# Añadir una opción al submenú para mostrar información del autor
helpmenu.add_command(label="Informacion del autor", command=popup)

# Añadir una opción al menú principal para cerrar la aplicación
menubar.add_command(label="Salir", command=root.destroy)

# Mostrar instrucciones en la ventana
instrucciones = Label(root, text="Programa creado en python para descargar videos de Youtube\n Para usarlo solo inserte el link del video de Youtube!")
instrucciones.grid(row=0, column=1)

# Crear una entrada de texto para el enlace del video
videos = Entry(root)
videos.grid(row=1, column=1)

# Crear un botón para iniciar la descarga del video
boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

# Crear una entrada de texto para la ruta de guardado
direccion_entry = Entry(root)
direccion_entry.grid(row=3, column=1)

# Crear un botón para cambiar la dirección de descarga
cambiar_direccion_boton = Button(root, text="Cambiar dirección", command=direccion)
cambiar_direccion_boton.grid(row=4, column=1)



# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
