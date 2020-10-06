from dataclasses import dataclass
import pandas as pd
import os
import xlrd
import googlemaps

@dataclass
class FileReader:
    
    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

    def new_file(self) -> str:
        return os.path.join(self.context, self.fname)

    def csv_to_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        return pd.read_excel(self.new_file(), header=header, usecols=usecols)

    def create_gmaps(self):
        return googlemaps.Client(key='AIzaSyCx06YfE-LfungduLv5prHvPLIPD0gtiZw')

