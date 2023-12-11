import pandas as pd
import pickle
from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
import mlflow
from clean_data_json import clean_data_json
from clean_data_csv import clean_data
from models.DiabetesModel import Diabete
from models.ItemModel import Item


os.environ['MLFLOW_TRACKING_USERNAME'] = "hatemslimani2035"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "f497730cfadcd6d476b9089d797bda3a8abcaa02"


mlflow.set_tracking_uri('https://dagshub.com/hatemslimani2035/ML_OPS.mlflow')
def getBestModel(filename,modelname,id):
    modelId=0
    with open(filename, 'r') as file:
        modelId = file.readline() 
        print(modelId)
        file.close
    print(modelId)
    df_mlflow = mlflow.search_runs(
        experiment_ids=[id], filter_string="metrics.Precision_test <1")
    run_id = df_mlflow.loc[df_mlflow['metrics.Precision_test'].idxmax()]['run_id']
    if modelId!=0 and run_id==modelId:
        modelDiabet = pickle.load(open(modelname, 'rb'))
    else:
        with open(filename, 'w') as file:
            file.write(run_id)
        logged_model = f'runs:/{run_id}/ML_models'
        modelDiabet = mlflow.pyfunc.load_model(logged_model)
        pickle.dump(modelDiabet, open(modelname, 'wb'))
    return modelDiabet

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
modelDiabet= getBestModel("id.txt","model.h5",1)
modelCardio= getBestModel("id2.txt","modelCardio.h5",0)


def read_file(file: UploadFile):
    content_type = file.content_type
    if "json" in content_type:
        return pd.read_json(file.file)
    elif "csv" in content_type:
        return pd.read_csv(file.file)
    else:
        raise ValueError("Unsupported file format")


@app.get("/")
def read_root():
    return {"Hello": "to medical Classifaction"}
@app.post("/predict")
def predict(data:Item):
    preprocessed_data,dfCardio = clean_data_json(data)
    predictions = modelDiabet.predict(preprocessed_data)
    predictionsCardio = modelCardio.predict(dfCardio)
    return {'diab':data.dict() , 'prediction':predictions.tolist(), 'cardio':data.dict() , 'predictionCardio':predictionsCardio.tolist()}
@app.post("/predict/csv")
def return_predictions(file: UploadFile = File(...)):
    data = read_file(file)
    preprocessed_data = clean_data(data)
    predictions = modelDiabet.predict(preprocessed_data)
    data['prediction']=predictions
    json_list = data.to_dict(orient='records')
    return {"diab":json_list}
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
