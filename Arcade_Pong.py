#Importamos el modulo 
import turtle

# Configuramos la ventana del juego
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

# Creamos la paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("red")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Creamos la paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("blue")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

# Creamos la pelota del juego 
pelota = turtle.Turtle()
pelota.speed(40)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 3  # Cambio en la posición (velocidad) en el eje X 
pelota.dy = -3  # Cambio en la posición (velocidad) en el eje Y

# Creamos el marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.hideturtle() # Escondemos la tortuga 
marcador.color("white")
marcador.penup()
marcador.goto(0,260)
scoreA = 0
scoreB = 0
marcador.write(f"Jugador A: {scoreA}  Jugador B: {scoreB}", align="center", font=("Arial",18,"normal"))


# Creamos funciones para mover las paletas hacia arriba y hacia abajo
def paleta_izquierda_arriba():
    # Mientras la paleta no haya llegado al limite del tablero esta subirá
    y = paleta_izquierda.ycor()
    if y < 250:
        y += 20
    paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    # Mientras la paleta no haya llegado al limite del tablero esta bajará
    y = paleta_izquierda.ycor()
    if y > -250:
        y -= 20
    paleta_izquierda.sety(y)

def paleta_derecha_arriba():
    # Mientras la paleta no haya llegado al limite del tablero esta subirá
    y = paleta_derecha.ycor()
    if y < 250:
        y += 20
    paleta_derecha.sety(y)

def paleta_derecha_abajo():
    # Mientras la paleta no haya llegado al limite del tablero esta bajará
    y = paleta_derecha.ycor()
    if y > -250:
        y -= 20
    paleta_derecha.sety(y)

# Configuramos la ventana para que ejecute las funciones anteriores según
# las instrucciones de los jugadores
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")

# Creamos una variable para un bucle while:
juego = True

# Iniciamos el bucle del juego
while juego:
    ventana.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Revisa los bordes de la pantalla
    if pelota.ycor() > 290:
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.dy *= -1

    if pelota.xcor() > 390:
        scoreA+=1
        marcador.clear()
        marcador.write(f"Jugador A: {scoreA}  Jugador B: {scoreB}", align="center", font=("Arial",18,"normal"))
        pelota.goto(0, 0)
        pelota.dx *= -1

    if pelota.xcor() < -390:
        scoreB+=1
        marcador.clear()
        marcador.write(f"Jugador A: {scoreA}  Jugador B: {scoreB}", align="center", font=("Arial",18,"normal"))
        pelota.goto(0, 0)
        pelota.dx *= -1

    # Revisa colisiones con las paletas
    if (pelota.xcor() > 340) and (pelota.xcor() < 350)  and (pelota.ycor() < paleta_derecha.ycor() + 50 and pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.dx *= -1

    elif (pelota.xcor() < -340) and (pelota.xcor() > -350)  and (pelota.ycor() < paleta_izquierda.ycor() + 50 and pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.dx *= -1
    
    elif scoreA == 3:
        marcador.clear()
        marcador.goto(0,100)
        marcador.write(f"Gana el jugador A!!!", align="center", font=("Arial",25,"normal"))
        juego = False

    elif scoreB == 3:
        marcador.clear()
        marcador.goto(0,100)
        marcador.write(f"Gana el jugador B!!!", align="center", font=("Arial",25,"normal"))
        juego = False
        
ventana.mainloop()