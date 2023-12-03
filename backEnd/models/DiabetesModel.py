from pydantic import BaseModel
from datetime import date
from typing import Union

class Diabete(BaseModel):
    Age: float=None
    Gender: str =None
    Height: float =None
    Weight: float =None
    Blood_Type: str =None
    BMI: float =None
    Temperature: float =None
    Heart_Rate: float =None
    Blood_Pressure: float =None
    Cholesterol: float =None
    Smoking: str =None