from dataclasses import dataclass
import pandas as pd
import os
import xlrd
import googlemaps
import json
'''
pandas ver.1.x 이상 encoding='UTF-8' 불필요
'''

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
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        return pd.read_excel(self.new_file(), header=header, usecols=usecols)

    def create_gmaps(self):
        return googlemaps.Client(key='')

    def json_load(self): # 기능을 쓸 때는 dframe, 속성 기능 -객체 / 아닐땐 dframe 이라고 쓰지않는다
        return json.load(open(self.new_file()), encoding='UTF-8')

