# Programa: lab1.py implementación del algoritmo de Bresenham
# Autores : Vicente Santos 
#           Cristobal Gallardo         
# Fecha   : 22/10/2024

# Importar bibliotecas necesarias
import math
from Libgraphics import *

def personaje():
    print('\n Saliendo...')
    xc = 5
    xy = 5
    r = 3
    partidacuello = xy-r
    largo_cuerpo= -5


    width = 1000
    height = 1000
    pixel_size = 2

    # Inicializar la ventana
    win = GraphWin("Stickman with Pixel Grid", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)

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


    # Esperar a que el usuario haga clic antes de cerrar la ventana
    if not win.isClosed():
        win.getMouse()
    win.close()

def Rotacion():
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

    # Dibujar personaje rotado
    win = GraphWin("Rotación del personaje", 400, 400)
    win.setCoords(-200, -200, 200, 200)
    personaje(win=win, xc=0, xy=0)
    for x, y in puntos_rotados:
        draw_pixel(x * 2, y * 2, win, 2, "red")  # Dibujar cada punto en rojo

    # Esperar a que el usuario haga clic antes de cerrar la ventana
    if not win.isClosed():
        win.getMouse()
    win.close()
    
def Traslacion():
    print('\n Traslacion...')

def Escalamiento():
    print('\n Escalamiento...')

def Todo_al_personaje():
    print('\n Saliendo...')



def salir():
    print('\n Saliendo...')

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

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

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla


# Función principal
def main():
    # Inicialización de variables

    # LLamar al menu
    print("\n\tBienvenidos al Programa de Representaciones Graficas")
    print("\nAutores : \n  Vicente Santos\n  Cristobal Gallardo")
    print("\n\n")
    print("El punto (0,0) se mostrara en azul")
    input("\n\nPresiona Enter para continuar...")
    print("\n\nMenu:")
    opciones = {
        '1': ('Dibujar personaje de palo',personaje),
        '2': ('Realizar rotacion', Rotacion),
        '3': ('Realizar traslacion',Traslacion),
        '4': ('Realizar escalamiento', Escalamiento),
        '5': ('Realizar rotacion, traslacion y escalamiento al personaje', Todo_al_personaje),
        '6': ('Salir', salir)
    }
    generar_menu(opciones, '6')

# Comprobar si este script se está ejecutando directamente

main()