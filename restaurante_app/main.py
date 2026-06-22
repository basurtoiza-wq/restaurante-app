# Importar las clases
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto("Hamburguesa", 5.50)
producto2 = Producto("Pizza", 8.25)
producto3 = Producto("Jugo Natural", 2.50)

# Crear clientes
cliente1 = Cliente("Gabriela", "0987654321")
cliente2 = Cliente("Joel", "0998765432")
# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()