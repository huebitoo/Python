
''' --------LIBRERIA RANDOM---------
COMANDOS: 
- RANDOM.RANDRANGE(X, Y, Z): Valor pseudo-aleatorio entero donde x es el menor número y el "y" es el máximo valor que puede tomar.
Además cabe recalcar el "z" es el multiplo por el cual se guiaran los números, ejemplo, si colocas z = 2, los numeros aleatorios seran solo pares.
- RANDOM.UNIFORM(X, Y): valor aleatorio decimal o entero pseudo-aleatorio con la misma lógica que el primer comando.
- RANDOM.CHOISE(X): despliega valores pseudo-aleatorios de listas, ejemplo, x=["mario", "pepe"], desplegará valores aleatorios de esa lista.
- RANDOM.SAMPLE(X, Y): sigue la misma lógica que el choise, pero este tiene la posibilidad de que en la variable "y" agregas cuantas variables de esa lista quieres desplegar.
'''
# CONTRASEÑAS ALEATORIAS

'''import random

letras = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0123456789" # Caracteres

def generador(longitud): # definimos una funcion.
    contraseña = ''.join(random.choice(letras) for a in range(longitud)) # haremos un for que recorra la n cantidad de longitud para poder crear la contraseña.
    return contraseña

longitud = 12
print(generador(longitud))'''

'''----------LIBRERIA PYGAME------------


-pygame.init(): Se usa para iniciar el juego.
-pygame.display.set_mode(x, y): Esta es nuestra ventana de juego, el "x" e "y" son las dimensiones en pixelesde nuestra pantalla.
-pygmae.display.set_caption(title, icontitle): Este es el  titulo que lleva la ventana acompañado de el icono que tambien tendra.
-pygame.display.update() actualiza la ventana cada vez que le hacemos una modificacion, va en la parte de eventos pero fuera del for.
-PANTALLA.fill(x) donde PANTALLA es nuestra variable que incluye las dimensiones de la pantalla y el comando fill es rellenar, el x es un color en hexadecimal.
-pygame.draw.rect(x, y, z) dibujará un rectangulo donde x es donde se mostrara (escribir la variable PANTALLA), y es el color en hexadecimal y z sera una coordenara () de cuatro variables donde las primeras dos indica
la distancia de la esquina superior izquierda del rectangulo y las otras dos son las dimensiones del rectangulo. Para activarla debes hacer un print(rectangulo) donde rectangulo es la variable con todo lo visto.
-pygame.draw.line(x, y, z, k) dibujara una linea siguiendo la misma lógica que el anterior pero donde k es el grosor en pixeles de la linea.
-pygame.draw.circle(x, y, z, k, t) dibujara un circulo siguiendo las mismas lógicas anteriores donde k es el radio y t será un agujero centrico en la circunferencia.
-pygame.draw.ellipse(x, y, z, k , t) dibujara un circulo siguiendo las mismas lógicas.
-pygame.image.load(x) cargará una imagen que tu coloques. Se llama a la imagen como si fuera un string. 
-PANTALLA.blit(x, y) cargara una imagen para usarla como fondo e y siendo coordenadas desde la esquina superior izquierda.



#Eventos
Se usa un while True para mantener la ventana abierta sino se cerrará.
-for event in pygam.event.get() es un ciclo para que este analizando cada momento que evento sucede en la ventana correspondiente.
-event.type == QUIT: Este evento es para que se active el botón de cerrar ventana.
    pygame.quit()
'''

import pygame

pygame.init() # INICIAR LA VENTANA
pantalla = pygame.display.set_mode((555, 260)) # PANTALLA MAS SUS DIMENSIONES
fondo = pygame.image.load("imagenes/fondo.jpg") # CARGAR UNA IMAGEN PARA LUEGO USARLA DE FONDO
icono = pygame.image.load("imagenes/miguelito.jpg") # CARGAR UNA IMAGEN PARA LUEGO USARLA DE ICONO
pygame.display.set_caption("Miguelito") # NOMBRE DEL PROGRAMA "TITLE"
pygame.display.set_icon(icono) # CARGARÁ EL ICONO
pantalla.blit(fondo, (0, 0)) # CARGARÁ LA IMAGEN
time = pygame.time.Clock()
target_fps = 60
# rect = pygame.draw.rect(pantalla, (200, 56, 26), (100, 100, 100, 300))
# print(rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
    pygame.display.update()
    time.tick(target_fps)
    



