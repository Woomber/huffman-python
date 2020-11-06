import tkinter.filedialog as filedialog
from tkinter import Label, Button, Message, Entry, Scrollbar
from tkinter.ttk import Notebook, Frame
import tkinter as tk
import huffman.tools as tools
import huffman.algorithm as Huffman
from ui.scrollframe import VScrollFrame

charwidth = 600


class HuffmanUI(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        root = self.master
        root.title('Compresión Huffman - Yael Chavoya')
        self.master.geometry(f'{charwidth + 30}x400')
        self.pack()

        # =================================

        tab_root = Notebook(root)

        tab_compress = VScrollFrame(tab_root)
        tab_decompress = Frame(tab_root)

        tab_root.add(tab_compress, text='Comprimir')
        tab_root.add(tab_decompress, text='Descomprimir')

        tab_root.pack(expand=1, fill=tk.BOTH)
        tab_cmp_root = tab_compress.interior


        # =================================

        tk.Label(tab_cmp_root, text='Texto a comprimir:').grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        self.original_entry = Entry(tab_cmp_root)
        self.original_entry.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn_1 = tk.Button(tab_cmp_root, text="Comprimir", command=self.btn_compress)
        self.btn_1.grid(row=0, column=2, pady=10, padx=10)

        # =================================

        tk.Label(tab_cmp_root, text="Texto original:").grid(row=1, column=0, padx=10, pady=0, sticky=tk.SW)

        self.strv_original = tk.StringVar()
        (tk.Message(tab_cmp_root, width=charwidth, justify='left', textvariable=self.strv_original)
            .grid(row=2, pady=10, padx=10, column=0, columnspan=3, sticky='w'))
        # =================================

        (tk.Label(tab_cmp_root, text='Texto comprimido en binario:')
            .grid(row=3, column=0, padx=10, sticky='sw'))

        self.strv_compressed = tk.StringVar()
        (tk.Message(tab_cmp_root, width=charwidth, justify='left', textvariable=self.strv_compressed)
            .grid(row=4,pady=10,padx=10,column=0, columnspan=3, sticky='w'))

        # =================================
        
        tk.Label(tab_cmp_root, text='Código para descomprimir:').grid(row=5, column=0, padx=10, sticky='sw')

        self.strv_encoded = tk.StringVar()
        (tk.Message(tab_cmp_root, width=charwidth, justify='left', textvariable=self.strv_encoded)
            .grid(row=6,pady=10,padx=10,column=0, columnspan=3, sticky='w'))

        # =================================

        self.strv_rate = tk.StringVar()
        tk.Label(tab_cmp_root, textvariable=self.strv_rate).grid(row=7, column=0, padx=10, sticky='sw')

        # =================================

        tab_cmp_root.grid_columnconfigure(1, weight=1)
        tab_cmp_root.grid_rowconfigure(2, weight=1)
        tab_cmp_root.grid_rowconfigure(4, weight=1)
        tab_cmp_root.grid_rowconfigure(6, weight=1)

    def btn_compress(self):
        text = self.original_entry.get()
        if not text:
            return
        self.strv_original.set(text)

        original_bin = tools.str_to_bin(text)
        compressed, code = Huffman.compress(text)
        encoded = Huffman.encode_key(code)

        self.strv_compressed.set(compressed)
        self.strv_encoded.set(encoded)

        rate = len(compressed) * 100 / len(original_bin)
        self.strv_rate.set(f'Razón de compresión: {rate}%')

    def run(self):
        self.mainloop()