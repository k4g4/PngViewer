import sys
from tkinter import Tk
from src.pngviewer import PngViewer


if len(sys.argv) > 1:
    PngViewer(sys.argv[1]).mainloop()
else:
    print("Provide a PNG image.")