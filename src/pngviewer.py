import tkinter as tk
from typing import Any, Optional

class PngViewer(tk.Frame):
    '''Display a PNG image'''

    def __init__(self, master: Optional[Any] = None) -> None:
        super().__init__(master)
        self.master: Optional[Any] = master
        self.pack()

