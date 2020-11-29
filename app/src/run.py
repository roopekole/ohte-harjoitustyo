from tkinter import Tk, ttk
import os.path
from whoosh import index
from ui.ui import UI
from config.whoosh_config import Config as whoosh

if not os.path.exists("indexfiles"):
    os.mkdir("indexfiles")
    ix = index.create_in("indexfiles", whoosh.schema)

window = Tk()
window.title('Reference data manager')
window.configure(bg="#FFFFFF")
window.geometry("500x500")

# Initialize style
s = ttk.Style()
# Create style used by default for all Frames
s.configure("TFrame", background="white")
s.configure("TLabel", background="white")

ui = UI(window)
ui.start()

window.mainloop()
