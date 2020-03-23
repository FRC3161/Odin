import tkinter as tk
from tkinter import ttk
from Scan import Scan

class Odin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x400")
        self.scan = Scan("data.csv")

        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.entry = ttk.Entry(self.frame)

        self.scan_button = ttk.Button(self.frame, text="Scan Code", command=self.scan.scan)
        self.scan_button.pack()

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        self.scan.cleanup()
        self.destroy()

odin = Odin()
odin.mainloop()
