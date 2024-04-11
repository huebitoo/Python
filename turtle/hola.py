import turtle as t

ventana = t.Screen()  # ventana
ventana.bgcolor("white")  # background
tortuga = t.Turtle()  # Flecha
tortuga.speed(0.4)  # Velocidad
tortuga.color("red")  # Color de la flecha

tortuga.penup()
tortuga.goto(0, -300)  # Mover la tortuga hacia abajo para centrar el círculo
tortuga.pendown()

tortuga.circle(300)

# CREACION 2

tortuga = t.Turtle()  # Flecha
tortuga.speed(0.4)  # Velocidad
tortuga.color("red")  # Color de la flecha
tortuga.penup()
tortuga.goto(100, -280)  # Mover la tortuga hacia abajo para centrar el círculo
tortuga.pendown()
largo = 205
for i in range(9):
    tortuga.right(-40)
    tortuga.forward(largo)
    

ventana.exitonclick()
