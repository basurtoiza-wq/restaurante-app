# Importar las clases necesarias
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self):
        
        self.productos = []
        self.clientes = []

   # Agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agregar clientes 
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Mostrar productos
    def mostrar_productos(self):
        print("\nPRODUCTOS DISPONIBLES")
        for producto in self.productos:
            print(producto)

    # Mostrar clientes
    def mostrar_clientes(self):
        print("\nCLIENTES REGISTRADOS")
        for cliente in self.clientes:
            print(cliente)