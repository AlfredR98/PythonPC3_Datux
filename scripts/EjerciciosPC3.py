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
'''
Ejercicio 4
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
Ejercicio 5
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
Ejercicio 6
'''
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
'''
Ejercicio 7
'''
class Phone:

    def __init__(self,nombreContacto,apellidoContacto,celContacto):
        self.nombreContacto = nombreContacto
        self.apellidoContacto = apellidoContacto
        self.celContacto = celContacto
        self.contacto = []
      
    def agregarContacto(self):
        self.contacto.append(self.nombreContacto)
        self.contacto.append(self.apellidoContacto)
        self.contacto.append(self.celContacto)
    
    
    def llamar(self):
        try:
            ingresarC = input('\nIngrese el nombre y apellido del contacto que desea llamar: ').lower()
            primerN, apellido = ingresarC.split(' ')
            contactoLlamar = primerN+''+apellido
        
            if contactoLlamar == self.nombreContacto+''+self.apellidoContacto:
                return print(f'Llamando a ... {self.nombreContacto} {self.apellidoContacto}')
            else:
                return print('No existe dentro de sus contactos')
        except Exception as e:
            print(e)
        
    def bloquearContacto(self):
        bloquearC = input('\n¿Cual es el nombre del contacto que quiere bloquear?: ')

        if bloquearC in self.contacto:
            self.bloquearContacto = True
            print(f'Su contacto {self.nombreContacto} con el número {self.celContacto} ha sido bloqueado')
        else: 
            print('No existe dentro de sus contactos')
                
nomC = input('Ingrese el Nombre del contacto: ').lower()
apeC = input('Ingrese el Apellido paterno del contacto: ').lower()
celC = input('Ingrese el Número celular del contacto: ')  

p = Phone(nomC,apeC,celC)
p.agregarContacto()
p.llamar()
p.bloquearContacto()
'''
Ejercicio 8
'''
class Persona:

    def __init__(self):
        try: 
            self.nombres = input('Ingrese su nombre completo: ').upper()
            self.edad = int(input('Ingrese su edad: '))
            self.sexo = input('Ingrese su sexo: ').upper()
            self.dni = input('Ingrese su dni: ')
            self.fecha_nacimiento = input('Ingrese su fecha de nacimiento: ')
        except Exception as e:
            print(e)
        
    def mostrar(self):
        print(self)
    
    def __str__(self):
        return 'Su nombre es: {}, su edad es: ({}), su sexo es: "{}", su DNI es: "{}" y su fecha de nacimiento es: "{}"'.format(self.nombres,self.edad,self.sexo,self.dni,self.fecha_nacimiento)

p = Persona()
p.mostrar()