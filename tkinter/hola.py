from tkinter import *

raiz = Tk() # creamos una ventana 

raiz.title("Ventana de pruebas") # colocamos un titulo aa la ventana

raiz.resizable(1,1) # impide la modificacion de la ventana, funciona con valores boolean o "1" y "0". El primer termino corresponde al "x" (width) y el otro a "y" (height)

# raiz.iconbitmap("C:/Users/campo/OneDrive/Escritorio/python/python/programas/imagenes/descarga_1.ico") # Es para cambiar el icono, le colocamos la ruta de la foto. Usar slash normal
raiz.geometry("800x600") # Dimensiones de la ventana

# configuracion de la ventana. BG es background y le definimos el color, 
raiz.config(bg="blue") 

raiz.config(border=10, cursor="pirate", relief="groove")

miFrame = Frame() #creas un espacio contenedor

# adjunta el frame dentro a la raiz, con el side definimos donde se va a anclar (right, left, bottom), con anchor mueves a las esquinas o lo redimencionas (n, s, w, e)
# fill es para rellenar los demas lados en el que colaste el frame (x, y) y con both rellena vertical u horizontal (se debe combinar con expand), expand rellena el y (True)
# EJEMPLO = miFrame.pack(fill="both", expand="True") 
miFrame.pack() 

miFrame.config(bg="green", width=400, height=400) # puedes agregar mas ajustes

miFrame.config(border=10) # bordes de espesor 10

miFrame.config(relief="sunken") # forma del borde (groove, sunken)

miFrame.config(cursor="hand2") # cambia el cursor (hand2, pirate)


# ------------------------- LABEL ------------------------------
milabel = Label(miFrame, text="Hola que hace", fg="green", font=("Arial", 10)) # desplegarun label, donde se contiene y su texto, hay muchas funciones como fg, font, etc

# milabel.place(x= 50, y=100) a diferencia del pack, el place situa el label dentro de un espacio (el frame)
milabel.grid(row=0, column=0, padx=20, pady=10) # lo mostramos pero el con grid, asi usamos mejor el espacio y dividiremos todo en columnas y filas, el sticky posiciona a la direccion que le digas (n, s, w, e)


# ------------------------------ ENTRY ------------------------
minombre=StringVar() # creamos una variable string que va a estar asociado al cuadro de texto que vamos a usar, asi cuando se active este autocompletara el cuadro

cuadrotexto = Entry(miFrame, textvariable=minombre) # generamos un cuadro de texto, podemos agregarlo incluso dentro de la raiz o el frame

cuadrotexto.grid(row=0, column=1, padx=20, pady=10) # el padx, pady hace la separacion de los elemento dentro de el frame o contenedor en el que está

cuadrotexto.config(fg="red", justify="center") # Tambien podemos configurart el justificado de las palabras (center, right, left...)

cuadrotexto.config(show="*") # de esta manera cada vez que ingresemos un dato a nuestro cuadro de texto, esta transformara las letras a lo que nosotros querramos


# ------------------- TEXT AND BUTTON ------------------------
comentarioslabel = Label(miFrame, text= "Comentarios: ") # creamos un label solamente

comentarioslabel.grid(row=1, column=0, padx=20, pady=10)

textocomentario = Text(miFrame, width=16, height=4) # creamos un text que guarda muchisimo mas texto. Podemos modificar sus dimensiones

textocomentario.grid(row=1, column=1) # posicion del text

scrollbar = Scrollbar(miFrame, command=textocomentario.yview) # creamos un scrollbar, el command lo usamos para ver el scrollbar en este caso en el textocomentarios y el yview decimos que muestre el y, por lo que el scrollbar baja y sube, puede ir de derecha a izquierda

scrollbar.grid(row=1, column=2, sticky="nsew")

textocomentario.config(yscrollcommand=scrollbar.set) # posicion del scroll

def codigoboton(): # creamos una funcion de autorelleno
    minombre.set("juan") # entonces cuando se presione enviar, se activiara el comando que es la funcion (esta) y colocara el nombre dentro de el texto de hola que hace

botonenvio = Button(miFrame, text="Enviar", command=codigoboton) # configuracion del boton

botonenvio.grid(row=2, column=0) # dimensiones y posicion




raiz.mainloop() # la desplegamos, es un bucle infinito para mostrarla. Esto debe estar siempre al final