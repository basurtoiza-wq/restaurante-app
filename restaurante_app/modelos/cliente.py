class Cliente:
# Constructor que guarda la información del cliente
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
# Representación del cliente en forma de texto
    def __str__(self):
        return f"Cliente: {self.nombre} - Teléfono: {self.telefono}"