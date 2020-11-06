from tkinter import Frame, Canvas, Scrollbar
import tkinter as tk

class VScrollFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        scrollbar = Scrollbar(self, orient=tk.VERTICAL)
        scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

        canvas = Canvas(self, yscrollcommand=scrollbar.set)
        canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        
        scrollbar.config(command=canvas.yview)

        self.interior = Frame(canvas)
        interior = self.interior
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        def _conf_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion='0 0 %s %s' % size)
            if interior.winfo_reqwidth() != canvas.winfo_reqwidth():
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _conf_interior)

        def _conf_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            canvas.bind('<Configure>', _conf_canvas)
