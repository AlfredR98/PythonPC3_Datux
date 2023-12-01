'''
Ejercicio 2
'''
'''
import math

class Circulo:
    
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        area = math.pi * (self.radio**2)
        return area


circulo = Circulo(8)
areaC = circulo.calcular_area()
print(f'El area de {circulo.radio} es: {areaC:.2f}')
'''
'''
Ejercicio 3
'''
'''
#crear la clase Catálogo y producto
class Producto:
    def __init__(self,nombre, precio:float):
        self.nombre = nombre   
        self.precio = precio

    def __str__(self):
        return '\nProducto: {} - Precio: S/. {}'.format(self.nombre, self.precio)

class Catalago:
    
    def __init__(self,productos=[]):
        self.productos = productos

    def agregar_productos(self,pro):
        self.productos.append(pro)

    def mostrar_productos(self):
        for p in self.productos:
            print(p)

cantidad = int(input('¿Cuantos productos desea catalogar?: '))
i = 1
pN = Producto('TELEVISION',500)
c = Catalago([pN])

while i <= cantidad:
    nomP = input(f'Ingrese nombre del producto {i}:  ').upper()
    precioP = float(input(f'Ingrese el precio del producto {i}:  '))
    c.agregar_productos(Producto(nomP,precioP))
    i+=1

c.mostrar_productos()
'''
'''
Ejercicio 4
'''
'''
from main import *

try:
    menu()
    opcion = int(input('Ingrese el número de la opción: '))

    if opcion == 1:

        n1 = float(input('Ingrese el número 1: '))
        n2 = float(input('Ingrese el número 2: '))
        resultado = fdividir(n1,n2)
        print('La división de los números {} y {} es: {}'.format(n1,n2,resultado))

    elif opcion == 2:
         print('Acaba de salir del Menú, Nos vemos!')

except Exception as e:
    print(e)
'''   
'''
Ejercicio 5
'''
'''
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self) -> str:
        return '\nEl Producto "{}" se le asignó el código "{}"'.format(self.nombre, self.codigo) 

  
nom = input('Ingrese el nombre del producto: ').capitalize()

pais = input('Ingrese País: ').upper()
        
while True:
    lote = input('Ingrese el Lote: ')
    if len(lote) !=4:
        print('! El lote debe contener 4 caracteres !')
        continue
    else:
        anio = input('Ingrese el Año: ')
        cod = pais+'-'+lote+'-'+anio
        p = Producto(nom,cod)
        print(p)
        break
'''
'''
Ejercicio 6
'''
#para la pregunta 4 al importar la funciones usar el manejo de errores (try,except) 
# y en las sentencias de “ else “ imprimir la ruta del directorio de trabajo os.getcwd() 
# (previamente importar el modulo os < import os> y en la sentencia finally imprimir “proceso terminado”
from main import *
import os

try:
    menu()
    opcion = int(input('Ingrese el número de la opción: '))

    if opcion == 1:

        n1 = float(input('Ingrese el número 1: '))
        n2 = float(input('Ingrese el número 2: '))
        resultado = fdividir(n1,n2)
        print('\nLa división de los números {} y {} es: {}'.format(n1,n2,resultado))

    elif opcion == 2:
         print('Acaba de salir del Menú, Nos vemos!')

except Exception as e:
    print(e)
else:
    print('El punto del directorio es: ',os.getcwd())
finally:
    print('“Proceso terminado"')