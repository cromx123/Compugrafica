# Programa: lab1.py implementación del algoritmo de Bresenham
# Autores : Vicente Santos 
#           Cristobal Gallardo         
# Fecha   : 22/10/2024

# Importar bibliotecas necesarias
import math
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
        
        # Crear el texto para la etiqueta del botón
        self.label = Text(center, label)
        self.label.draw(win)
        
        self.deactivated = False  # Estado del botón (activo/inactivo)
    
    def is_clicked(self, p):
        """Devuelve True si el botón está activo y el punto `p` está dentro del botón."""
        return (self.rect.getP1().getX() <= p.getX() <= self.rect.getP2().getX() and
                self.rect.getP1().getY() <= p.getY() <= self.rect.getP2().getY())

    def undraw(self):
        self.rect.undraw()  # Borrar el rectángulo del botón
        self.label.undraw()  # Borrar el texto del botón
        
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

def personaje(xc=5, xy=5, r=3, win=None, pixel_size=2):
    print('\n Saliendo...')
    partidacuello = xy-r
    largo_cuerpo= -5

    # Dibuja cabeza
    CircleBresenham(xc, xy, r, win, pixel_size)
    # Dibuja cuerpo
    LineaBresenham(xc, partidacuello, xc, largo_cuerpo, win, pixel_size)
    # Dibuja brazos
    LineaBresenham(xc + 3, partidacuello - 2, xc - 4, partidacuello - 2, win, pixel_size)
    # Dibuja pierna izquierda
    LineaBresenham(xc, largo_cuerpo, xc - 4, largo_cuerpo - 4, win, pixel_size)
    # Dibuja pierna derecha
    LineaBresenham(xc, largo_cuerpo, xc + 4, largo_cuerpo - 4, win, pixel_size)


def Rotacion(win):
    print('\nRotación...')
    angle_deg = leer_variable("Introduce el ángulo de rotación en grados:")
    angle_rad = math.radians(angle_deg)

    # Puntos originales del personaje
    puntos = [(5, 5), (5, -5), (8, -2), (1, -2), (1, -9), (9, -9)]
    xc, yc = 0, 0  # Centro de rotación

    # Calcular la rotación
    puntos_rotados = []
    for x, y in puntos:
        x_rot = xc + (x - xc) * math.cos(angle_rad) - (y - yc) * math.sin(angle_rad)
        y_rot = yc + (x - xc) * math.sin(angle_rad) + (y - yc) * math.cos(angle_rad)
        puntos_rotados.append((int(x_rot), int(y_rot)))
        
    personaje(win=win, xc=0, xy=0)
    for x, y in puntos_rotados:
        draw_pixel(x * 2, y * 2, win, 2, "red")  # Dibujar cada punto en rojo

    
def Traslacion():
    print('\n Traslacion...')

def Escalamiento(win):
    print('\n Escalamiento...')
    personaje(xc = 10,xy = 10 , win=win)

def Todo_al_personaje():
    print('\n Saliendo...')

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
    # Inicialización de variables
    width = 1000
    height = 1000

    # Coordenadas de los botones en el borde superior derecho
    button_width = 120
    button_height = 30
    x_position = 350
    y_start = 50
    spacing = 40

    # Inicializar la ventana
    win = GraphWin("Stickman with Pixel Grid", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)

    # LLamar al menu
    print("\n\tBienvenidos al Programa de Representaciones Graficas")
    print("\nAutores : \n  Vicente Santos\n  Cristobal Gallardo")
    print("\n\n")
    print("El punto (0,0) se mostrara en azul")
    
    # Crear un objeto de texto
    saludo_text = Text(Point(0, 5 * spacing), "¡Hola, Bienvenidos al Programa de Representaciones Graficas!")
    saludo_text.setSize(15)           # Tamaño de fuente
    saludo_text.setStyle("bold")       # Estilo de fuente
    saludo_text.draw(win)
    
    autores_text = Text(Point(0, 3 * spacing), "Autores: \nVicente Santos\nCristobal Gallardo")
    saludo_text.setSize(15) 
    autores_text.setStyle("bold")       # Estilo de fuente
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
        rotacion_button = Button(win, Point(x_position, y_start + spacing), button_width, button_height, "Rotación")
        escalamiento_button = Button(win, Point(x_position, y_start + 2 * spacing), button_width, button_height, "Escalamiento")
        escalamiento_button_plus = Button(win, Point(x_position + 80, y_start + 2 * spacing), 30, 30, " + ")
        escalamiento_button_minus = Button(win, Point(x_position + 110, y_start + 2 * spacing), 30, 30, " - ")
        salir_button = Button(win, Point(x_position, y_start - spacing), button_width, button_height, "Salir")
        
        # Activar los botones
        crear_personaje_button.activate()
        salir_button.activate()
        botones_activos = 0
        # Esperar a que el usuario haga clic en uno de los botones
        while True:
            click_point = win.getMouse()
            
            if crear_personaje_button.is_clicked(click_point):
                personaje(win=win, xc=5, xy=5)
                print("El personaje fue dibujado")
                
                traslacion_button.activate()
                rotacion_button.activate()
                escalamiento_button.activate()
                escalamiento_button_plus.activate()
                escalamiento_button_minus.activate()    
                botones_activos = 1
                
            elif traslacion_button.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón Traslación clicado!")
                    Traslacion()

            elif rotacion_button.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón Rotación clicado!")
                    Rotacion(win)
                
            elif escalamiento_button_plus.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón Aumento de Escalamiento clicado!")
                    escalamiento_button_plus.activate()
                    escalamiento_button_minus.desactivate()
                    Escalamiento(win)

            elif escalamiento_button_minus.is_clicked(click_point):
                if botones_activos == 1:
                    print("Botón Disminución de Escalamiento clicado!")
                    escalamiento_button_minus.activate()
                    escalamiento_button_plus.desactivate()
                    Escalamiento(win)

            elif salir_button.is_clicked(click_point):
                win.close()
                break

# Comprobar si este script se está ejecutando directamente

main()