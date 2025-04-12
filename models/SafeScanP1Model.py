import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer  
from services import SafeScanService

loaded_model = joblib.load("./models/libs/SafeScanP1_Model.pkl")

def processModel(path):
    data = pd.read_csv(path)
    features = ["type", "amount", "oldbalanceOrg", "newbalanceOrig"] 

    if not all(col in data.columns for col in features):
        return None
    
    data["type"] = data["type"].map({"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5})

    imputer = SimpleImputer(strategy='mean')
    predict = imputer.fit_transform(data[features].values)
    predictions = loaded_model.predict(predict)

    fraud_count = np.sum(predictions == "Fraud")
    non_fraud_count = np.sum(predictions == "No Fraud")

    return SafeScanService.getRangeGrade(fraud_count, non_fraud_count)