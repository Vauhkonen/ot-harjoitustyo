from tkinter import Tk, constants, ttk
from main_view import MainView
from rent_view import RentView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_main_view()
    
    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_rent
        )

        self._current_view.pack()
    
    def _show_rent_view(self):
        self._hide_current_view()
        
        self._current_view = RentView(
            self._root,
            self._handle_main
        )

        self._current_view.pack()


    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None
        
    
    def _handle_main(self):
        self._show_main_view()

    def _handle_rent(self):
        self._show_rent_view()
    




window = Tk()
window.title("LainaSinko")
window.geometry('500x300')


ui = UI(window)
ui.start()

window.mainloop()