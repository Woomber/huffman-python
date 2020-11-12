"""
Interfaz gráfica
Yael Chavoya

La interfaz gráfica se divide en dos partes:
- La implementación del acomodo y formato de la interfaz se encuentra en _windowsetup.py
- La implementación de la funcionalidad de la interfaz se encuentra en este archivo
"""
import huffman.tools as tools
import huffman.algorithm as huffman
from tkinter.messagebox import showerror
import tkinter as tk
from ui._windowsetup import MainWindow


class HuffmanUI(MainWindow):
    """
    Clase de la ventana principal

    Hereda de la clase que implementa el acomodo y formato de la interfaz
    """

    def __init__(self):
        MainWindow.__init__(self, 'Compresión Huffman - Yael Chavoya', self.btn_compress, self.btn_decompress)

    def btn_compress(self):
        """
        Método accionado al presionar el botón de comprimir
        """
        text = self.original_entry.get('1.0', tk.END)

        # Validar los datos

        if text[-1] == chr(10):
            text = text[:-1]

        if not text:
            return

        # Comprimir el texto mediante el algoritmo de Huffman y mostrarlo junto con el código

        original_bin = tools.str_to_bin(text)
        compressed, code = huffman.compress(text)
        encoded = huffman.encode_key(code)

        self.strv_compressed.set(compressed)
        self.strv_encoded.set(encoded)

        # Calcular el tamaño del texto comprimido en proporción con el tamaño del texto original

        rate = len(compressed) * 100 / len(original_bin)
        self.strv_rate.set('Razón de compresión: {:0.2f}%'.format(rate))

    def btn_decompress(self):
        """
        Método accionado al presionar el botón de descomprimir
        """

        binary = self.decompress_entry.get('1.0', tk.END).strip()
        code = self.code_entry.get('1.0', tk.END).strip()

        # Validación de datos

        if not binary or not code:
            return

        try:
            # Descomprimir la representación binaria usando el código proporcionado y mostrarlo
            code_list = huffman.decode_key(code)
            text = huffman.decompress(binary, code_list)
            self.strv_original2.set(text)
        except ValueError as error:
            showerror(message=error)

    def run(self):
        """
        Método que inicia la ejecución de la ventana
        """
        self.mainloop()
