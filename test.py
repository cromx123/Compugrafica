# Programa: lab1.py implementación del algoritmo de Bresenham
# Autores : Vicente Santos 
#           Cristobal Gallardo         
# Fecha   : 22/10/2024

# Importar bibliotecas necesarias
import math
import random   
from Libgraphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        """Inicializa el botón en la ventana gráfica `win` con el centro, ancho, alto y etiqueta."""
        w, h = width / 2, height / 2
        x, y = center.getX(), center.getY()
        
        # Crear rectángulo para el botón
        self.rect = Rectangle(Point(x - w, y - h), Point(x + w, y + h))
        self.rect.setFill("lightgray")  # Color de fondo del botón
        self.rect.draw(win)
        
        
        self.label = Text(center, label)
        self.label.draw(win)
        
        self.deactivated = False  # Estado del botón (activo/inactivo)
    
    def is_clicked(self, p):
        """Devuelve True si el botón está activo y el punto `p` está dentro del botón."""
        return (self.rect.getP1().getX() <= p.getX() <= self.rect.getP2().getX() and
                self.rect.getP1().getY() <= p.getY() <= self.rect.getP2().getY())

    def undraw(self):
        self.rect.undraw() 
        self.label.undraw()  
        
    def activate(self):
        """Activa el botón (cambia el borde a negro y lo vuelve clicable)."""
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.deactivated = False

    def desactivate(self):
        """Desactiva el botón (cambia el borde a gris claro y lo hace no clicable)."""
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.deactivated = True
    
    def desactivate2(self):
        """Desactiva el botón (cambia el borde a gris claro y lo hace no clicable)."""
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.deactivated = False
    
    def cambio_texto(self, win, center):
        self.label.undraw()
        self.label = Text(center, "Reiniciar")
        self.label.draw(win)


personaje_elementos = []

def undraw_personaje(win, pixel_size):
    global personaje_elementos
    for elemento in personaje_elementos:
        x, y = elemento  
        undraw_pixel(x, y, win, pixel_size)
    personaje_elementos = []
    vaciar_personaje()
        
def draw_personaje(win, puntos_rotados, pixel_size):
    undraw_personaje(win, pixel_size)
    for x, y in puntos_rotados:
        draw_pixel(x, y, win, pixel_size, color="black")  
                 
def personaje(xc=5, xy=5, r=3, largo_cuerpo = -5, win=None, pixel_size = 2):
    global personaje_elementos  # Usamos una lista global para almacenar los elementos
    personaje_elementos = [] 
    print('\n Creando personaje...')
    partidacuello = xy-r
    
    # Dibuja cabeza
    CircleBresenham(xc, xy, r, win, pixel_size)
    
    
    # Dibuja cuerpo
    LineaBresenham(xc, partidacuello, xc, largo_cuerpo, win, pixel_size)
    
    # Dibuja brazos
    LineaBresenham(xc + 4, partidacuello - 2, xc - 4, partidacuello - 2, win, pixel_size)
    LineaBresenham(xc - 4, partidacuello - 2, xc + 3, partidacuello - 2, win, pixel_size)
    
    
    # Dibuja pierna izquierda e derecha
    LineaBresenham(xc, largo_cuerpo, xc - 4, largo_cuerpo - 4, win, pixel_size)
    LineaBresenham(xc, largo_cuerpo, xc + 4, largo_cuerpo - 4, win, pixel_size)
    personaje_elementos = get_personaje_puntos()
    return personaje_elementos

def Rotacion(win, puntos, angle_deg = 1, xr=0, yr=0, pixel_size= 2):
    print('\nRotación respecto a un punto arbitrario...')
    angle_rad = math.radians(angle_deg)
    undraw_personaje(win,pixel_size)
    puntos_rotados = []
    for x, y in puntos:
        x_rot = xr + (x - xr) * math.cos(angle_rad) - (y - yr) * math.sin(angle_rad)
        y_rot = yr + (x - xr) * math.sin(angle_rad) + (y - yr) * math.cos(angle_rad)
        puntos_rotados.append((int(x_rot), int(y_rot)))
        
    draw_personaje(win, puntos_rotados, pixel_size)
    return puntos_rotados


def Traslacion(win, xc, xy, desplazamiento_x=0, desplazamiento_y=0, largo_personaje=-5, pixel_size = 2):
    print('\n Traslacion usando vectores...')
    
    # Trasladar todos los puntos
    nuevos_puntos = []
    for P in personaje_elementos:
        # Realiza la traslación sumando los vectores
        P_prime = [P[0] + desplazamiento_x, P[1] + desplazamiento_y]
        nuevos_puntos.append(P_prime)
    
    draw_personaje(win, nuevos_puntos, pixel_size)
    # Define el vector de posición inicial y de traslación
    PP = [xc, xy]
    T_tr = [desplazamiento_x, desplazamiento_y]
    
    # Realiza la traslación sumando los vectores
    P_prime = [PP[0] + T_tr[0], PP[1] + T_tr[1]]
    nuevo_xc, nuevo_xy = P_prime
    return nuevo_xc, nuevo_xy, largo_personaje + desplazamiento_y, nuevos_puntos
    
def Escalamiento(win, puntos, xc = 0, yc = 0, x_active = 0, y_active = 0, pixel_size = 2):
    print('\nEscalamiento...')
    global personaje_elementos
    undraw_personaje(win,pixel_size)
    pixel_size *= 2
    if pixel_size > 32:
        pixel_size = 32
    if x_active == 1 and y_active == 1:
        escala_x = 2 
        escala_y = 2 
    elif x_active == 1:
        escala_x = 2 
        escala_y = 1
    elif y_active == 1:
        escala_x = 1 
        escala_y = 2 
    else:
        escala_x = 1
        escala_y = 1 
        
    puntos_escalados = []
    for x, y in puntos:
        x_esc = xc + (x - xc) * escala_x
        y_esc = yc + (y - yc) * escala_y
        puntos_escalados.append((int(x_esc), int(y_esc)))
    personaje_elementos = puntos_escalados
    
    draw_personaje(win, personaje_elementos, pixel_size)
    return puntos_escalados, pixel_size

def Reductor(win, puntos, xc = 0, yc = 0, x_active = 0, y_active = 0, pixel_size = 2):
    print('\nEscalamiento...')
    global personaje_elementos
    undraw_personaje(win,pixel_size)
    pixel_size //= 2
    if pixel_size < 1:
        pixel_size = 1
    if x_active == 1 and y_active == 1:
        escala_x = 2 
        escala_y = 2 
    elif x_active == 1:
        escala_x = 2 
        escala_y = 1
    elif y_active == 1:
        escala_x = 1 
        escala_y = 2 
    else:
        escala_x = 1
        escala_y = 1 
    
    puntos_escalados = []
    for x, y in puntos:
        x_esc = xc + (x - xc) / escala_x
        y_esc = yc + (y - yc) / escala_y
        puntos_escalados.append((int(x_esc), int(y_esc)))
    personaje_elementos = puntos_escalados
    
    draw_personaje(win, personaje_elementos, pixel_size)
    return puntos_escalados, pixel_size

def TodoAlPersonaje(win,xc, xy, largo_cuerpo, pixel_size = 2):
    print('\n El azar...')
    #pixel_size = random.randint(1, 4) * 2
    distanciax = random.randint(-20, 20)
    distanciay = random.randint(-20, 20)
    xc, xy, largo_cuerpo, personaje_elementos = Traslacion(win, xc, xy, desplazamiento_x = distanciax, desplazamiento_y= distanciay, largo_personaje = largo_cuerpo, pixel_size= pixel_size)
    x_active = random.randint(0, 1)
    y_active = random.randint(0, 1)
    num = random.randint(0, 10)
    if(num % 2):
        personaje_elementos, pixel_size = Escalamiento(win, personaje_elementos, xc = xc, yc = xy, x_active= x_active, y_active= y_active, pixel_size= pixel_size)
    else:
        personaje_elementos, pixel_size = Reductor(win, personaje_elementos, xc = xc, yc = xy, x_active= x_active, y_active= y_active, pixel_size= pixel_size)
    grados = random.randint(-360, 360)
    personaje_elementos = Rotacion(win, personaje_elementos, grados, xc, xy, pixel_size=pixel_size)
    
    return xc, xy, largo_cuerpo, personaje_elementos, pixel_size

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def leer_variable(nombre):
    while True:
        a = input(f'{nombre} ')
        try:
            a = int(a)
            return a
        except ValueError:
            print('La variable no es un número entero, vuelva a intentarlo.')

# Función principal
def main():
    global personaje_elementos
    # Inicialización de variables
    width = 1000
    height = 1000
    pixel_size = 2
    # Coordenadas de los botones en el borde superior derecho
    button_width = 120
    button_height = 30
    x_position = 350
    y_start = 50
    spacing = 40
    xc = 5
    xy = 5
    r = 3
    largo_cuerpo = -5
    
    # Inicializar la ventana
    win = GraphWin("Stickman with Pixel Grid", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)
    win.setBackground("white")

    # LLamar al menu
    print("\n\tBienvenidos al Programa de Representaciones Graficas")
    print("\nAutores : \n  Vicente Santos\n  Cristobal Gallardo")
    print("\n\n")
    print("El punto (0,0) se mostrara en azul")
    
    # Crear un objeto de texto
    saludo_text = Text(Point(0, 5 * spacing), "¡Hola, Bienvenidos al Programa de Representaciones Graficas!")
    saludo_text.setSize(15)          
    saludo_text.setStyle("bold")      
    saludo_text.draw(win)
    
    autores_text = Text(Point(0, 3 * spacing), "Autores: \nVicente Santos\nCristobal Gallardo")
    saludo_text.setSize(15) 
    autores_text.setStyle("bold")      
    autores_text.draw(win)
    
    iniciar_button = Button(win, Point(0, -50), button_width + 30, button_height, "Empezar programa")
    salir_button = Button(win, Point(0, -50 - spacing), button_width + 30, button_height, "Salir")
    
    iniciar_button.activate()
    salir_button.activate()
    
    while True:
        click_point = win.getMouse()
        
        if iniciar_button.is_clicked(click_point):
            # Borrar pantalla de inicio
            saludo_text.undraw()          
            autores_text.undraw()
            iniciar_button.undraw()     
            salir_button.undraw()
            print("Mensaje y botón borrados")
            program_on = 1
            break  
        
        elif salir_button.is_clicked(click_point):
            win.close()
            program_on =  0

            break
    if program_on == 1:
        
        # Crear botones en el borde superior derecho
        crear_personaje_button = Button(win, Point(x_position, y_start + 3 * spacing), button_width, button_height, "Crear personaje")
        traslacion_button = Button(win, Point(x_position, y_start), button_width, button_height, "Traslación")
        traslacion_button_left = Button(win, Point(x_position - 110, y_start), 30, 30, "<")
        traslacion_button_top = Button(win, Point(x_position - 80, y_start), 30, 30, "^")
        traslacion_button_down = Button(win, Point(x_position + 80, y_start), 30, 30, "v")
        traslacion_button_right = Button(win, Point(x_position + 110, y_start), 30, 30, ">")
        rotacion_button = Button(win, Point(x_position, y_start + spacing), button_width, button_height, "Rotación")
        ingresar_texto_rotacion= Entry(Point(x_position - 95, y_start + spacing), 6)
        ingresar_texto_rotacion.setFill("lightgray")
        escalamiento_button = Button(win, Point(x_position, y_start + 2 * spacing), button_width, button_height, "Escalamiento")
        escalamiento_button_x = Button(win, Point(x_position - 80, y_start + 2 * spacing), 30, 30, "x")
        escalamiento_button_y = Button(win, Point(x_position - 110, y_start + 2 * spacing), 30, 30, "y")
        escalamiento_button_plus = Button(win, Point(x_position + 80, y_start + 2 * spacing), 30, 30, " + ")
        escalamiento_button_minus = Button(win, Point(x_position + 110, y_start + 2 * spacing), 30, 30, " - ")
        todo_al_personaje = Button(win, Point(x_position, y_start - spacing), button_width, button_height, "Todo al azar")
        salir_button = Button(win, Point(x_position, y_start - 2 * spacing), button_width, button_height, "Salir")
        
        error_text = Text(Point(0, 5 * spacing), "Ingrese un número valido")
        error_text.setSize(18) 
        error_text.setTextColor("red")
        error_text.setStyle("bold")   
        mensaje = 0
        # Activar los botones
        crear_personaje_button.activate()
        salir_button.activate()
        botones_activos = 0
        x_active = 1
        y_active = 1
        
        # Esperar a que el usuario haga clic en uno de los botones
        while True:
            click_point = win.getMouse()
            
            if crear_personaje_button.is_clicked(click_point):
                
                
                traslacion_button.activate()
                rotacion_button.activate()
                escalamiento_button.activate()
                escalamiento_button_plus.activate()
                escalamiento_button_minus.activate()    
                escalamiento_button_x.activate()
                escalamiento_button_y.activate()
                traslacion_button_left.activate()
                traslacion_button_top.activate()
                traslacion_button_down.activate()
                traslacion_button_right.activate()
                todo_al_personaje.activate()
                
                if(botones_activos!=1):
                    ingresar_texto_rotacion.draw(win)
                    crear_personaje_button.cambio_texto(win, Point(x_position, y_start + 3 * spacing))
                    
                else:
                    undraw_personaje(win,pixel_size)
                    xc = 5
                    xy = 5
                    r = 3
                    largo_cuerpo = -5
                    pixel_size = 2
                
                personaje_elementos = personaje(xc, xy, r, largo_cuerpo, win, pixel_size)
                print("El personaje fue dibujado")
                
                
                botones_activos = 1
                

            elif rotacion_button.is_clicked(click_point):
                if botones_activos == 1:
                    texto = ingresar_texto_rotacion.getText()
                    
                    try:
                        grados = int(texto)
                        error_text.undraw()  
                        personaje_elementos = Rotacion(win, personaje_elementos, grados, xc, xy, pixel_size=pixel_size)
                    except ValueError:
                        print("Error: Ingresa un número entero.")
                        error_text.setText("Error: Ingresa un número entero.")
                        if mensaje == 0:
                            error_text.draw(win)
                            mensaje = 1
                        ingresar_texto_rotacion.setText("")
                
            elif escalamiento_button_plus.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón Aumento de Escalamiento clicado!")
                    escalamiento_button_plus.activate()
                    escalamiento_button_minus.desactivate()
                    personaje_elementos, pixel_size = Escalamiento(win, personaje_elementos, xc = xc, yc = xy, x_active= x_active, y_active= y_active, pixel_size= pixel_size)
                    

            elif escalamiento_button_minus.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón Disminución de Escalamiento clicado!")
                    escalamiento_button_minus.activate()
                    escalamiento_button_plus.desactivate()
                    personaje_elementos, pixel_size = Reductor(win, personaje_elementos, xc = xc, yc = xy, x_active= x_active, y_active= y_active,  pixel_size= pixel_size)
                    
            elif escalamiento_button_x.is_clicked(click_point):
                if botones_activos == 1:
                    if  x_active == 1:
                        escalamiento_button_x.desactivate2()
                        x_active = 0
                    else:
                        escalamiento_button_x.activate()
                        x_active = 1

            elif escalamiento_button_y.is_clicked(click_point):
                if botones_activos == 1:
                    if  y_active == 1:
                        escalamiento_button_y.desactivate2()
                        y_active = 0
                    else:
                        escalamiento_button_y.activate()
                        y_active = 1
            
            elif traslacion_button_left.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón izquierda de traslación clicado!")
                    xc, xy, largo_cuerpo, personaje_elementos = Traslacion(win, xc, xy, desplazamiento_x = -5, largo_personaje = largo_cuerpo, pixel_size= pixel_size)
                    
            elif traslacion_button_top.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón arriba de traslación clicado!")
                    xc, xy, largo_cuerpo, personaje_elementos = Traslacion(win, xc, xy, desplazamiento_y = 5, largo_personaje = largo_cuerpo, pixel_size= pixel_size)
                    
            elif traslacion_button_down.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón abajo de traslación clicado!")
                    xc, xy, largo_cuerpo, personaje_elementos = Traslacion(win, xc, xy, desplazamiento_y = -5, largo_personaje = largo_cuerpo, pixel_size= pixel_size)
                    
            elif traslacion_button_right.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón derecha de traslación clicado!")
                    xc, xy, largo_cuerpo, personaje_elementos = Traslacion(win, xc, xy, desplazamiento_x = 5, largo_personaje = largo_cuerpo, pixel_size= pixel_size)
            
            elif todo_al_personaje.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón todo al personaje clicado!")
                    xc, xy, largo_cuerpo, personaje_elementos, pixel_size = TodoAlPersonaje(win, xc, xy, largo_cuerpo, pixel_size= pixel_size)
                    
            elif salir_button.is_clicked(click_point):
                win.close()
                break

# Comprobar si este script se está ejecutando directamente

main()