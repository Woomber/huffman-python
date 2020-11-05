import tkinter.filedialog as filedialog
import tkinter as tk
import huffman

class HuffmanUI(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        root = self.master
        root.title('Compresión Huffman - Yael Chavoya')
        # self.master.geometry('350x200')
        root.grid()

        charwidth = 600

        (tk.Label(root, text='Selecciona un archivo a comprimir:')
            .grid(row=0, column=0, pady=10, padx=10))

        self.btn_1 = (tk.Button(root, text="Abrir archivo...", command=self.openfile)
            .grid(row=0,column=1,pady=10, padx=10))

        (tk.Label(root, text="Texto original:")
            .grid(row=1, column=0, padx=10, pady=0, sticky='sw'))

        self.original_text = tk.StringVar()
        (tk.Message(root, justify='left', textvariable=self.original_text)
            .grid(row=2, pady=10, padx=10, column=0, columnspan=2, sticky='w'))

        (tk.Label(root, text='Texto original en binario:')
            .grid(row=3, column=0, padx=10, sticky='sw'))

        self.bin_text = tk.StringVar()
        (tk.Message(root, textvariable=self.bin_text, anchor='nw')
            .grid(row=4,pady=10,padx=10,column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W))


        (tk.Label(root, text='Texto comprimido en binario:')
            .grid(row=5, column=0, padx=10, sticky='sw'))

        self.mod_text = tk.StringVar()
        (tk.Message(root,width=charwidth, justify='left', textvariable=self.mod_text)
            .grid(row=6,pady=10,padx=10,column=0, columnspan=2, sticky='w'))

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(6, weight=1)

    def openfile(self):
        filename = filedialog.askopenfilename(parent=self)
        try:
            f = open(filename)
            self.original_text.set(f.read())
            self.bin_text.set(huffman.regular_binary(self.original_text.get()))
            self.compress()
        except FileNotFoundError:
            pass

    def compress(self):
        compressed = huffman.compress(self.original_text.get())
        self.mod_text.set(compressed)

    def run(self):
        self.mainloop()