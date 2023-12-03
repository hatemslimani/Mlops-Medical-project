import pandas as pd
import datetime as dt
from models.DiabetesModel import Diabete

def fix_missing_cols(training_cols, new_data):
    missing_cols = set(training_cols) - set(new_data.columns)
     # Add a missing column in test set with default value equal to 0
    for c in missing_cols:
        new_data[c] = 0
    # Ensure the order of column in the test set is in the same order than in train set
    new_data = new_data[training_cols]
    return new_data

def clean_data(data):
    df = pd.DataFrame()
    data.DateNais = pd.to_datetime(data.DateNais)
    
    # Calculate age and assign to the 'Age' column
    df['Age'] = dt.date.today().year - data.DateNais.dt.year
    
    # Map gender values and assign to the 'Gender' column using map
    gender_mapping = {'Male': 1, 'Female': 0}
    df['Gender'] = data.Gender.map(gender_mapping)
    
    df['Height'] = data.Height
    df['Weight'] = data.Weight
    
    # Map blood type values and assign to the 'Blood_Type' column
    blood_mapping = {'A': 0, 'B': 1, 'O': 2, 'AB': 3}
    df['Blood Type'] = data.Blood_Type.map(blood_mapping)
    
    # Calculate BMI and assign to the 'BMI' column
    df['BMI'] = (data.Weight / (data.Height ** 2)) * 10000
    
    df['Temperature'] = data.Temperature
    df['Heart Rate'] = data.Heart_Rate
    df['Blood Pressure'] = data.Blood_Pressure
    df['Cholesterol'] = data.Cholesterol
    
    # Map smoking values and assign to the 'Smoking' column
    smoking_mapping = {'No': 1, 'Yes': 0}
    df['Smoking'] = data.Smoking.map(smoking_mapping)
    
    return df