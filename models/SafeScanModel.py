import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from . import SafeScanP1Model, SafeScanP2Model

def predict(path, safeScanP3):
    safeScanP1 = SafeScanP1Model.processModel(path)
    safeScanP2 = SafeScanP2Model.processModel(path)
    if safeScanP1 == None or safeScanP2 == None : return None

    mainModel = joblib.load("./models/libs/SafeScanMainModel.pkl")
    encoder = LabelEncoder()
    encoder.fit(["R", "Y", "G"])

    enc1 = encoder.transform([safeScanP1.upper()])[0]
    enc2 = encoder.transform([safeScanP2.upper()])[0]
    enc3 = encoder.transform([safeScanP3.upper()])[0]
    X_input = np.array([[enc1, enc2, enc3]])

    result = mainModel.predict(X_input)
    label_map = {0: "R", 1: "Y", 2: "G"}

    return label_map[result[0]]