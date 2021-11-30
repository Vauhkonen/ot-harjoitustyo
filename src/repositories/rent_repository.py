from config import RENT_FILE_PATH
from pathlib import Path

class RentRepository:

    # Class constructor, parameter file path from config.py
    def __init__(self, file_path):
        self._file_path = file_path
        self._rentlist = []
        self._open()
        

    # To make sure that there is data-file or create one
    def _ensure_file_exist(self):
        Path(self._file_path).touch()

    def _save(self):
        self._ensure_file_exist()

        with open(self._file_path, "w") as file:
            for rent in self._rentlist:
                row = rent
                file.write(row)

    def _open(self):
        self._ensure_file_exist()

        with open(self._file_path) as file:
            for row in file:
                self._rentlist.append(row)
        
    def get_rentlist(self):
        return self._rentlist

    def save_new(self, borrow):
        self._rentlist.append(borrow)
        self._save()
        return True








repository = RentRepository(RENT_FILE_PATH)
    
