import pandas as pd
import datetime as dt
from models.DiabetesModel import Diabete
from models.ItemModel import Item
"""
This function serves to clean the incoming new data in production when it is JSON format
"""


def fix_missing_cols(training_cols, new_data):
    missing_cols = set(training_cols) - set(new_data.columns)
    # Add a missing column in test set with default value equal to 0
    for c in missing_cols:
        new_data[c] = 0
    # Ensure the order of column in the test set is in the same order than in train set
    new_data = new_data[training_cols]
    return new_data


def clean_data_json(df):
    data=pd.DataFrame([toDiabetSet(df).dict()])
    data.rename(
        columns = {'Heart_Rate':'Heart Rate',
                   'Blood_Pressure':'Blood Pressure',
                   'Blood_Type':'Blood Type'}, inplace = True)
    dataCardio=pd.DataFrame([toCardioSet(df).dict()])
    return data,dataCardio
def toDiabetSet(data:Item):
    df = Diabete()
    df.Age =dt.date.today().year - data.DateNais.year
    print(dt.date.today().year - data.DateNais.year)
    gender={'Male':1,'Female':0}
    df.Gender=gender[data.Gender]
    df.Height=data.Height
    df.Weight=data.Weight
    blood={'A':0,'B':1,'O':2,'AB':3}
    df.Blood_Type=blood[data.Blood_Type]
    df.BMI = (data.Weight / pow(data.Height, 2)) * 10000
    df.Temperature=data.Temperature
    df.Heart_Rate=data.Heart_Rate
    df.Blood_Pressure=data.Blood_Pressure
    df.Cholesterol=data.Cholesterol
    isSmoking={'No':1,'Yes':0}
    df.Smoking=isSmoking[data.Smoking]
    return df
def toCardioSet(data:Item):
    df = Diabete()
    df.age =dt.date.today().year - data.DateNais.year
    print(dt.date.today().year - data.DateNais.year)
    gender={'Male':1,'Female':0}
    df.gender=gender[data.Gender]
    df.height=data.Height
    df.weight=data.Weight
    df.ap_hi=data.ap_hi
    df.ap_lo = data.ap_lo
    df.active=data.active
    df.alco=data.alco
    df.gluc=data.gluc
    df.cholesterol=data.Cholesterol
    isSmoking={'No':1,'Yes':0}
    df.smoke=isSmoking[data.Smoking]
    return df
