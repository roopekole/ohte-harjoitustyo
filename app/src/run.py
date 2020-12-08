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
window.geometry("600x500")

# Initialize style
s = ttk.Style()
s.theme_use("clam")
# Create style used by default for all Frames
s.configure("TFrame", background="white")
s.configure("TLabel", background="white")
s.configure("TButton", background="#3AAFA9")
# Create style for footer progress bar used for download and upload animation
s.configure(
    "custom.Horizontal.TProgressbar",
    troughcolor='#FEFFFF',
    background='#2B7a78',
    darkcolor="#3AAFA9",
    lightcolor="#DEF2F1",
    bordercolor="#FEFFFF",
    )

ui = UI(window)
ui.start()

window.mainloop()
