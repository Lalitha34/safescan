import pandas as pd
from . import SafeScanService

upiList = {}

def load():
    data = pd.read_excel(SafeScanService.DB_URI_PATH)

    global upiList
    upiList = data.to_dict(orient='records')