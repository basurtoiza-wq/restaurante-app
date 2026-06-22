# Sistema de Gestión de Restaurante

## Nombre del estudiante
Gabriela Isabel Sanchez Basurto

## Descripción del sistema
Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos disponibles y clientes, además de mostrar la información almacenada mediante una estructura modular organizada en diferentes archivos.

## Estructura del proyecto

restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py


## Explicación de la estructura

- **modelos/producto.py:** contiene la clase Producto, que representa los productos del restaurante.
- **modelos/cliente.py:** contiene la clase Cliente, que representa a los clientes registrados.
- **servicios/restaurante.py:** contiene la clase Restaurante, encargada de gestionar los productos y clientes.
- **main.py:** es el archivo principal desde donde se crean los objetos y se ejecuta el programa.

## Conceptos de Programación Orientada a Objetos utilizados

- Clases y objetos.
- Constructores mediante __init__().
- Atributos y métodos.
- Método especial __str__().
- Importación de módulos.
- Organización modular del software.

## Reflexión

La modularización permite dividir el programa en diferentes archivos según sus responsabilidades. Esto facilita la organización, el mantenimiento y la reutilización del código. Además, la Programación Orientada a Objetos ayuda a representar entidades del mundo real de una manera más clara y estructurada.