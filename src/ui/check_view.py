from tkinter import Entry, ttk, constants, Text, Button, Label, Frame

class CheckView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._frame = None

        self._initialize()
    
    def _initialize(self):
        self._frame = Frame(master=self._root)
    

        #Button
        btn_back = Button(self._frame, text="Takaisin", command=self._handle_main)
        btn_back.grid(row=10, column=0, pady=5)

    
    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)