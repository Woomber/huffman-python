import tkinter.filedialog as filedialog
from tkinter import Label, Button, Message, Entry, Scrollbar
import tkinter as tk
import huffman.tools as tools
import huffman.algorithm as Huffman

charwidth = 600

class HuffmanUI(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        root = self.master
        root.title('Compresión Huffman - Yael Chavoya')
        self.master.geometry(f'{charwidth + 30}x400')
        root.grid()

        # =================================

        tk.Label(root, text='Texto a comprimir:').grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)

        self.original_entry = Entry(root, )
        self.original_entry.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn_1 = tk.Button(root, text="Comprimir", command=self.btn_compress)
        self.btn_1.grid(row=0, column=2, pady=10, padx=10)

        # =================================

        tk.Label(root, text="Texto original:").grid(row=1, column=0, padx=10, pady=0, sticky=tk.SW)

        self.strv_original = tk.StringVar()
        (tk.Message(root, width=charwidth, justify='left', textvariable=self.strv_original)
            .grid(row=2, pady=10, padx=10, column=0, columnspan=3, sticky='w'))

        # =================================

        tk.Label(root, text='Texto original en binario:').grid(row=3, column=0, padx=10, sticky='sw')

        self.strv_original_bin = tk.StringVar()
        (tk.Message(root, width=charwidth, justify='left', textvariable=self.strv_original_bin)
            .grid(row=4,pady=10,padx=10,column=0, columnspan=3, sticky=tk.N+tk.S+tk.E+tk.W))

        # =================================

        (tk.Label(root, text='Texto comprimido en binario:')
            .grid(row=5, column=0, padx=10, sticky='sw'))

        self.strv_compressed = tk.StringVar()
        (tk.Message(root, width=charwidth, justify='left', textvariable=self.strv_compressed)
            .grid(row=6,pady=10,padx=10,column=0, columnspan=3, sticky='w'))

        # =================================
        
        tk.Label(root, text='Código para descomprimir:').grid(row=7, column=0, padx=10, sticky='sw')

        self.strv_encoded = tk.StringVar()
        (tk.Message(root, width=charwidth, justify='left', textvariable=self.strv_encoded)
            .grid(row=8,pady=10,padx=10,column=0, columnspan=3, sticky='w'))

        # =================================

        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(6, weight=1)
        self.master.grid_rowconfigure(8, weight=1)

    def btn_compress(self):
        text = self.original_entry.get()
        if not text:
            return
        self.strv_original.set(text)
        self.strv_original_bin.set(tools.str_to_bin(text))

        compressed, code = Huffman.compress(text)
        encoded = Huffman.encode_key(code)

        self.strv_compressed.set(compressed)
        self.strv_encoded.set(encoded)

    def run(self):
        self.mainloop()