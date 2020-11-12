"""
Implementación de una clase para hacer scroll vertical en un tkinter.Frame
Yael Chavoya
"""
from tkinter import Frame, Canvas, Scrollbar
import tkinter as tk


class VScrollFrame(Frame):
    """
    Clase que permite crear un Frame que puede hacer overflow vertical y mostrarlo mediante una barra de scroll

    Para agregar elementos al Frame, usar la propiedad 'interior'
    """

    def __init__(self, parent, *args, **kw):
        """
        Inicializa el Frame
        """
        Frame.__init__(self, parent, *args, **kw)

        scrollbar = Scrollbar(self, orient=tk.VERTICAL)
        scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

        # Uso de un canvas debido a que permite el desplazamiento
        canvas = Canvas(self, yscrollcommand=scrollbar.set)
        canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        
        scrollbar.config(command=canvas.yview)

        # Creación del Frame que contendrá a los elementos que se deseen agregar
        self.interior = Frame(canvas)
        interior = self.interior
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # Configurar la barra y el canvas para que estén sincronizados
        def _conf_interior(_):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion='0 0 %s %s' % size)
            if interior.winfo_reqwidth() != canvas.winfo_reqwidth():
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _conf_interior)

        def _conf_canvas(_):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _conf_canvas)
