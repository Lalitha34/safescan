import pandas as pd
from services import SafeScanService

def processModel(path):
    data = pd.read_csv(path)
    counts = data['Report'].value_counts().to_dict()
    count_true = counts[True] if True in counts else 0
    count_false = counts[False] if False in counts else 0
    return SafeScanService.getRangeGrade(count_false, count_true)