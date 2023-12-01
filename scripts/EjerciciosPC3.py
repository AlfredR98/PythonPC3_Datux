'''
Ejercicio 2
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
Ejercicio 3
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
