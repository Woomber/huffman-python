"""
Interfaz gráfica
Yael Chavoya

La interfaz gráfica se divide en dos partes:
- La implementación del acomodo y formato de la interfaz se encuentra en este archivo
- La implementación de la funcionalidad de la interfaz se encuentra en gui.py
"""
from tkinter import font
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook
import tkinter as tk
from ui.scrollframe import VScrollFrame


# Longitud de los bloques que muestran texto, en caracteres (tk.Message)
char_width = 600


class MainWindow(tk.Frame):
    """
    Clase de la ventana principal. Implementa solamente el acomodo y formato de la interfaz
    """
    
    def __init__(self, title, compress_fn, decompress_fn):
        """
        Inicializa la ventana con el acomodo inicial

        :param title: El título de la ventana
        :param compress_fn: La función a llamar al presionar el botón de comprimir
        :param decompress_fn: La función a llamar al presionar el botón de descomprimir
        """
        tk.Frame.__init__(self)

        # Información básica de la ventana
        root = self.master
        root.title(title)
        root.geometry(f'{char_width + 150}x400')

        # Configurar la fuente a usar cuando se requiera hacer énfasis
        self.bold_font = font.Font(family='TkTextFont', size=10, weight='bold')

        # Configurar las pestañas como VScrollFrames

        tab_root = Notebook(root)

        tab_compress = VScrollFrame(tab_root)
        tab_decompress = VScrollFrame(tab_root)

        tab_root.add(tab_compress, text='Comprimir')
        tab_root.add(tab_decompress, text='Descomprimir')

        tab_root.pack(expand=1, fill=tk.BOTH)
        tab_cmp_root = tab_compress.interior
        tab_dcp_root = tab_decompress.interior

        # Asignar las acciones de los botones

        self.cmd_compress = compress_fn
        self.cmd_decompress = decompress_fn

        # Configurar el layout de cada pestaña

        self._setup_cmp(tab_cmp_root)
        self._setup_dcp(tab_dcp_root)

    @staticmethod
    def clipboard_copy(target: str):
        """
        Copia una cadena específica al portapapeles

        :param target: El texto a copiar
        """
        cb = tk.Tk()
        cb.withdraw()
        cb.clipboard_clear()
        cb.clipboard_append(target)
        cb.update()
        cb.destroy()

    def _setup_cmp(self, tab_cmp_root):
        """
        Configura la pestaña de comprimir

        :param tab_cmp_root: El Frame donde configurar los elementos
        """

        # =================================
        # Configurar la entrada del texto original

        row = 0

        (tk.Label(tab_cmp_root, text='Texto a comprimir:', font=self.bold_font)
            .grid(row=row, column=0, pady=10, padx=10, sticky=tk.W))

        row += 1

        self.original_entry = ScrolledText(tab_cmp_root, width=50, height=6, wrap=tk.WORD)
        self.original_entry.grid(row=row, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W+tk.E)

        self.btn_1 = tk.Button(tab_cmp_root, text="Comprimir", command=self.cmd_compress)
        self.btn_1.grid(row=row, column=2, pady=10, padx=10, sticky=tk.N)

        # =================================
        # Configurar la salida del texto comprimido

        row += 1

        (tk.Label(tab_cmp_root, text='Texto comprimido en binario:', font=self.bold_font)
            .grid(row=row, column=0, columnspan=2, padx=10, sticky='sw'))

        row += 1

        self.strv_compressed = tk.StringVar()
        (tk.Message(tab_cmp_root, width=char_width, justify='left', textvariable=self.strv_compressed, relief='groove')
            .grid(row=row, pady=10, padx=10, column=0, columnspan=2, sticky='w'))

        tk.Button(tab_cmp_root, text="Copiar", command=self.btn_cp_cmp).grid(row=row, padx=10, column=2, sticky=tk.N)

        # =================================
        # Configurar la salida del código para descomprimir

        row += 1
        
        (tk.Label(tab_cmp_root, text='Código para descomprimir:', font=self.bold_font)
            .grid(row=row, column=0, columnspan=2, padx=10, sticky=tk.S+tk.W))

        row += 1

        self.strv_encoded = tk.StringVar()
        (tk.Message(tab_cmp_root, width=char_width, justify='left', textvariable=self.strv_encoded, relief='groove')
            .grid(row=row, pady=10, padx=10, column=0, columnspan=2, sticky=tk.W))

        tk.Button(tab_cmp_root, text="Copiar", command=self.btn_cp_cod).grid(row=row, padx=10, column=2, sticky=tk.N)

        # =================================
        # Configurar la salida de la razón de compresión

        row += 1

        self.strv_rate = tk.StringVar()
        (tk.Label(tab_cmp_root, textvariable=self.strv_rate, font=self.bold_font)
            .grid(row=row, column=0, columnspan=3, padx=10, sticky=tk.S+tk.W))

        # =================================
        # Configurar cuáles filas y columnas se expanden al cambiar el tamaño de la ventana

        tab_cmp_root.grid_columnconfigure(1, weight=1)
        tab_cmp_root.grid_rowconfigure(1, weight=1)
        tab_cmp_root.grid_rowconfigure(3, weight=1)
        tab_cmp_root.grid_rowconfigure(5, weight=1)

    def _setup_dcp(self, tab_dcp_root):
        """
        Configura la pestaña de descomprimir

        :param tab_dcp_root: El Frame donde configurar los elementos
        """

        # =================================
        # Configurar la entrada del texto a descomprimir

        row = 0

        (tk.Label(tab_dcp_root, text='Texto a descomprimir:', font=self.bold_font)
            .grid(row=row, column=0, pady=10, padx=10, sticky=tk.W))
        
        self.btn_2 = tk.Button(tab_dcp_root, text="Descomprimir", command=self.cmd_decompress)
        self.btn_2.grid(row=1, column=2, pady=10, padx=10, rowspan=4, sticky=tk.S)

        row += 1

        self.decompress_entry = ScrolledText(tab_dcp_root, width=50, height=6, wrap=tk.CHAR)
        self.decompress_entry.grid(row=row, column=0, columnspan=2, sticky=tk.W+tk.E)

        # =================================
        # Configurar la entrada del código para descomprimir

        row += 1

        (tk.Label(tab_dcp_root, text='Código para descomprimir:', font=self.bold_font)
            .grid(row=row, column=0, pady=10, padx=10, sticky=tk.W))

        row += 1

        self.code_entry = ScrolledText(tab_dcp_root, width=50, height=6, wrap=tk.CHAR)
        self.code_entry.grid(row=row, column=0, columnspan=2, sticky=tk.W+tk.E)

        # =================================
        # Configurar la salida del texto descomprimido

        row += 1

        (tk.Label(tab_dcp_root, text="Texto original:", font=self.bold_font)
            .grid(row=row, column=0, columnspan=2, padx=10, pady=0, sticky=tk.SW))

        row += 1

        self.strv_original2 = tk.StringVar()
        (tk.Message(tab_dcp_root, width=char_width, justify='left', textvariable=self.strv_original2, relief='groove')
            .grid(row=row, pady=10, padx=10, column=0, columnspan=2, sticky='w'))

        tk.Button(tab_dcp_root, text="Copiar", command=self.btn_cp_ori).grid(row=row, padx=10, column=2, sticky=tk.N)

        # =================================
        # Configurar cuáles filas y columnas se expanden al cambiar el tamaño de la ventana

        tab_dcp_root.grid_columnconfigure(1, weight=1)
        tab_dcp_root.grid_rowconfigure(row, weight=1)

    def btn_cp_cmp(self):
        """
        Copiar el texto comprimido al portapapeles
        """
        self.clipboard_copy(self.strv_compressed.get())
    
    def btn_cp_cod(self):
        """
        Copiar el código al portapapeles
        """
        self.clipboard_copy(self.strv_encoded.get())
        
    def btn_cp_ori(self):
        """
        Copiar el texto descomprimido al portapapeles
        """
        self.clipboard_copy(self.strv_original2.get())
