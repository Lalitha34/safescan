from datetime import datetime
from . import SafeScanService, LoadDBService as db
from models import SafeScanModel

def validateUPI(upiId):
    if not db.upiList : return SafeScanService.UNAUTH

    curr_id = next((item for item in db.upiList if item['UPI Id'].lower() == upiId.lower()), None)
    if not curr_id: return SafeScanService.UNKNOWN

    if curr_id['Trusted']:
        return SafeScanService.TRUSTED
    else:
        daysDiff = (datetime.today() - curr_id['Created Date']).days
        safeScanP3 = "Y" if daysDiff > 30 else "R"

        upiStatementPath = SafeScanService.DB_UPI_PATH(curr_id['EID'])
        safeScanResult = SafeScanModel.predict(upiStatementPath, safeScanP3)
        
        if safeScanResult == "R" : return SafeScanService.FRAUD
        elif safeScanResult == "Y" : return SafeScanService.WARNING
        elif safeScanResult == "G" : return SafeScanService.TRUSTED
        
        return SafeScanService.ERROR