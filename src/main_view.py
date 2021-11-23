from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_rent):
        self._root = root
        self._frame = None
        self._handle_rent = handle_rent

        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Valitse toiminto")
        lainaa_button = ttk.Button(master=self._frame, text="Lainaa", command=self._handle_rent)
        tarkistalainat_button = ttk.Button(master=self._frame, text="Tarkista lainat")

        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        lainaa_button.grid(row=1, column=0, padx=5, pady=5)
        tarkistalainat_button.grid(row=1, column=1, padx=5, pady=5)

        #self._root.grid_columnconfigure(1, weight=1, minsize=200)

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    
