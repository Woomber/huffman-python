"""
Implementación del Algoritmo de Compresión de Huffman
Con interfaz gráfica de usuario

Yael Chavoya
"""
from ui.gui import HuffmanUI


def main():
    """
    Crear y ejecutar una instancia de la ventana gráfica
    """
    ui = HuffmanUI()
    ui.run()


if __name__ == '__main__':
    main()
