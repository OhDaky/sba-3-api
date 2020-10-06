import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
from model.crime import CrimeModel
import pandas as pd
import numpy as np 
from sklearn import preprocessing
from model.cctv import CctvModel
'''
Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
       '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '구별'],
      dtype='object')
'''

class Police:
    def __init__(self):
        self.reader = FileReader()

    def hook_process(self):
        print('----------- POLICE -------------')
        self.create_crime_rate()
    
    def create_crime_rate(self):
        crime = CrimeModel()
        crime_police = crime.get_crime_police()
        police = pd.pivot_table(crime_police, index='구별', aggfunc=np.sum)
        print(f'{police.head()}')
        police['살인검거율'] = (police['살인 검거'] / police['살인 발생']) * 100
        police['강간검거율'] = (police['강간 검거'] / police['강간 발생']) * 100
        police['강도검거율'] = (police['강도 검거'] / police['강도 발생']) * 100
        police['절도검거율'] = (police['절도 검거'] / police['절도 발생']) * 100
        police['폭력검거율'] = (police['폭력 검거'] / police['폭력 발생']) * 100

        police.drop(columns= {'살인 검거','강간 검거','강도 검거','절도 검거','폭력 검거'}, axis=1)
        crime_rate_columns = ['살인검거율','강간검거율','강도검거율','절도검거율','폭력검거율']

        for i in crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100

        police.rename(columns = {
            '살인 발생': '살인',
            '강간 발생': '강간',
            '강도 발생': '강도',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        crime_columns=['살인', '강간', '강도', '절도', '폭력']

        x = police[crime_columns].values

        min_max_scaler = preprocessing.MinMaxScaler()

        x_scaled = min_max_scaler.fit_transform(x.astype(float))
        
        police_norm = pd.DataFrame(x_scaled, columns=crime_columns, index=police.index)
        police_norm[crime_rate_columns] = police[crime_rate_columns]

        cctv = CctvModel()
        cctv_pop = cctv.get_cctv_pop()

        print(f'cctv_pop :: {cctv_pop.head()}')
        police_norm['범죄'] = np.sum(police_norm[crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[crime_columns], axis=1)
        print(f'police_norm_columns :: {police_norm.columns}')
        reader = self.reader
        reader.context = os.path.join(baseurl, 'saved_data')
        reader.fname = 'police_norm.csv'

        police_norm.to_csv(reader.new_file(), sep=',', encoding='UTF-8')


if __name__ == '__main__':
    police = Police()
    police.hook_process()
    