from tkinter import Tk
from ui.ui import UI



window = Tk()
window.title("LainaSinko")
window.geometry('500x300')


ui = UI(window)
ui.start()

window.mainloop()