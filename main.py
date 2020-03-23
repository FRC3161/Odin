import tkinter as tk
from Scan import Scan

class Odin(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.scan = Scan("data.csv")
        self.scan_button = tk.Button(text = "Scan Code", width = 50, height = 2, command=self.scan.scan)
        self.scan_button.pack()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        self.scan.cleanup()
        self.destroy()

odin = Odin()
odin.mainloop()
