import math
# Funcion que permite calcular el area del cuadrago ingresando un Lado
def area_cuadrado(lado):
    # Validacion numeros positivos
    if(lado<=0):
        return print('Solo numeros positivos Error')
    else :
        # Calculo del area
        area=lado**2
        return  print('El area del cuadrado es: ', area)
# Funcion que permite calcular el area del trinagulo ingresando base y altura
def area_triangulo(base,altura):
    # Validacion numeros positivos
    if(base<=0 or altura <=0):
        return print('Solo numeros positivos Error')
    else :
        # Calculo del area
        area=base*altura/2
        return print('El area del triángulo es: ', area)

# Llamada de las funciones   
salir = False
# Menu con opciones
while not salir:
    print("Calcular Áreas de figuras Geométricas.\n")
    print("1.Cuadrado.\n2.Triángulo\n3.Salir\n")

    opciones=int(input("Escoja la figura: "))
    #  opcion 1 Cuadrado
    if opciones==1:
        lado=int(input('Ingrese el lado: '))
        area_cuadrado(lado)
        print("\n")

     #  opcion 2 Triangulo
    if opciones==2:
        base=int(input('Ingrese la base: '))
        altura=int(input('Ingrese la altura: '))
        area_triangulo(base,altura)
        print("\n")
     #  opcion 3 Salir   
    if opciones==3:
        salir = True
        print ("Fin\n")
    

