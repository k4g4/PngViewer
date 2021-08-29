from pngreader import PngReader
import tkinter as tk
import sys


BG_COLOR: str = "#1C1B22"


class PngViewer(tk.Frame):
    """Display a PNG image"""

    def __init__(self, png_file: str) -> None:
        self.master: tk.Tk = tk.Tk()
        super().__init__(self.master)

        self.reader: PngReader = PngReader(png_file)

        self.canvas: tk.Canvas = tk.Canvas(self.master, width=self.reader.width, height=self.reader.height, bg=BG_COLOR)
        self.canvas.pack()

        self.pack()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        PngViewer(sys.argv[1]).mainloop()
    else:
        print("Provide a PNG image.")