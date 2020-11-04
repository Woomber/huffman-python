import tkinter.filedialog as filedialog
import tkinter as tk


class HuffmanUI(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('Compresión Huffman - Yael Chavoya')
        # self.master.geometry('350x200')

        tk.Label(self, text='Selecciona un archivo a comprimir:').grid(row=0, column=0, pady=10, padx=10)

        self.btn_1 = tk.Button(self, text="Abrir archivo...", command=self.openfile).grid(row=0,column=1,pady=10, padx=10)

        tk.Label(self, text="Texto original:").grid(row=1, column=0, padx=10, pady=0, sticky='sw')

        self.textvar = tk.StringVar()
        self.original_text = tk.Entry(self, width=50, state='disabled', textvariable=self.textvar).grid(row=2, pady=10, padx=10, column=0, columnspan=2)

    def openfile(self):
        filename = filedialog.askopenfilename(parent=self)
        try:
            f = open(filename)
            self.textvar.set(f.read())
        except FileNotFoundError:
            pass


    def run(self):
        self.mainloop()