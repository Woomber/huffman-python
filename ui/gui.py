import huffman.tools as tools
import huffman.algorithm as Huffman
from tkinter.messagebox import showerror
import tkinter as tk
from ui._windowsetup import MainWindow

class HuffmanUI(MainWindow):

    def __init__(self):
        MainWindow.__init__(self, 'Compresión Huffman - Yael Chavoya', self.btn_compress, self.btn_decompress)

    def btn_compress(self):
        text = self.original_entry.get('1.0', tk.END)

        if text[-1] == chr(10):
            text = text[:-1]

        if not text:
            return

        original_bin = tools.str_to_bin(text)
        compressed, code = Huffman.compress(text)
        encoded = Huffman.encode_key(code)

        self.strv_compressed.set(compressed)
        self.strv_encoded.set(encoded)

        rate = len(compressed) * 100 / len(original_bin)
        self.strv_rate.set('Razón de compresión: {:0.2f}%'.format(rate))

    def btn_decompress(self):
        binary = self.decompress_entry.get('1.0', tk.END).strip()
        code = self.code_entry.get('1.0', tk.END).strip()
        if not binary or not code:
            return
        
        try:
            codelist = Huffman.decode_key(code)
            text = Huffman.decompress(binary, codelist)
            self.strv_original2.set(text)
        except ValueError as error:
            showerror(message=error)



    def run(self):
        self.mainloop()