from tkinter import Tk, ttk
from ui.ui import UI

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
