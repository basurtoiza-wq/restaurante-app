# Clase que representa un producto del restaurante

class Producto:
# Constructor que inicializa los datos del producto
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
 # Permite mostrar el objeto como texto
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"