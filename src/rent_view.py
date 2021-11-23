from tkinter import Entry, ttk, constants, Text, Button, Label, Frame
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


class RentView:
    def __init__(self, root, handle_main):
        self._root = root
        self._handle_main = handle_main
        self._frame = None

        self._initialize()
    
    def _initialize(self):
        self._frame = Frame(master=self._root)

    # Labels
        Label(
            self._frame,
            text="Lisää uusi laina",
            font=("Times", "20", "bold")
            ).grid(row=1,column=1,padx=5, pady=5)

        Label(
            self._frame,
            text="Lainattava tuote",
            ).grid(row=2, column=0, padx=5, pady=5, sticky="E")
        
        Label(
            self._frame,
            text="Lainaaja",
            ).grid(row=3, column=0, padx=5, pady=5, sticky="E")
        
        Label(
            self._frame,
            text="Lainaus pvm",
            ).grid(row=4, column=0, padx=5, pady=5, sticky="E")

        Label(
            self._frame,
            text="Palautus pvm",
            ).grid(row=5, column=0, padx=5, pady=5, sticky="E")

        Label(
            self._frame,
            text="Selite",
            ).grid(row=6, column=0, padx=5, pady=5, sticky="NE")
        
        #Entry
        self.product = Entry(self._frame, width=30)
        self.product.grid(row=2, column=1)
        self.borrower = Entry(self._frame, width=30)
        self.borrower.grid(row=3, column=1)
        self.borrowdate = Entry(self._frame, width=30)
        self.borrowdate.grid(row=4, column=1)
        self.returndate = Entry(self._frame, width=30)
        self.returndate.grid(row=5, column=1)

        #Text
        self.description = Text(self._frame, width=30, height=5)
        self.description.grid(row=6, column=1)


        #Button
        btn_back = Button(self._frame, text="Takaisin", command=self._handle_main)
        btn_back.grid(row=10, column=0, pady=5)
        btn_reset = Button(self._frame, text="Tyhjennä")
        btn_reset.grid(row=10, column=1)
        btn_save = Button(self._frame, text="Tallenna", command=self._tallenna)
        btn_save.grid(row=10, column=2)
        

        
    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _tallenna(self):
        a = self.product.get()
        b = self.borrower.get()
        c = self.borrowdate.get()
        d = self.returndate.get()
        e = self.description.get(1.0, constants.END)
        record = [a,b,c,d,e]
        print(record)
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = ';'.join(record)
            print(text)
            output_file.write(text)
