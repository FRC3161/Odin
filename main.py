import tkinter as tk
from tkinter import ttk
from Scan import Scan
from PIL import ImageTk, Image
from TBA import TBA

class Odin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x400")
        self.title("Odin")
        self.scan = Scan("data.csv")

        self.columnconfigure(0, weight=1)

        self.img = ImageTk.PhotoImage(Image.open("logo_image.png"))
        self.panel = tk.Label(self, image=self.img)
        self.panel.grid(row=0, column=0)

        self.scan_button = ttk.Button(text="Scan Code", command=self.scan.scan)
        self.scan_button.grid(row=1, column=0)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        self.scan.cleanup()
        self.destroy()

odin = Odin()
tba = TBA()
tba.getstatus()
odin.mainloop()
