from ui.main_view import MainView
from ui.rent_view import RentView
from ui.check_view import CheckView

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
            self._handle_rent,
            self._handle_check            
        )

        self._current_view.pack()
    
    def _show_rent_view(self):
        self._hide_current_view()
        
        self._current_view = RentView(
            self._root,
            self._handle_main
        )

        self._current_view.pack()

    def _show_check_view(self):
        self._hide_current_view()
        
        self._current_view = CheckView(
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
    
    def _handle_check(self):
        self._show_check_view()