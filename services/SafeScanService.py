# SafeScan Output Rules

FRAUD = {"state": True, "icon": "fraud-icon", "message": "Fraud"}
WARNING = {"state": True, "icon": "warning-icon", "message": "Suspicious"}
TRUSTED = {"state": True, "icon": "trusted-icon", "message": "Trusted"}

# SafeScan Internal Technical Issues

UNKNOWN = {"error": "SafeScan : UPI Unavailable", "icon": "unknown-icon", "message": "Sorry for the inconvenience — SafeScan is in beta with limited data, and the provided UPI ID isn't available. We're evolving quickly and will adapt to deliver results for this UPI ID soon. Thank you for your patience!"} 
UNAUTH = {"error": "SafeScan Error", "icon": "restricted-icon", "message": "Unauthorized User : Access Restricted"}
ERROR = {"error": "SafeScan Error", "icon": "error-icon", "message": "Sorry, We are currently experiencing technical difficulties."}

# SafeScan DataBase Rules

DB_BASE = "./database/"
DB_UPI_BASE = DB_BASE + "global/"
DB_BASE_EXTENSION = ".xlsx"
DB_CSV_EXTENSION = ".csv"

DB_URI_PATH = DB_BASE + "/UPIDetails" + DB_BASE_EXTENSION
DB_UPI_PATH = lambda eid : DB_UPI_BASE + str(eid) + DB_CSV_EXTENSION

# SafeScan Result Generator

def getRangeGrade(fraud_count, non_fraud_count):
    if fraud_count < 1 and non_fraud_count < 1 : return None

    total_count = 100 / (fraud_count + non_fraud_count)
    score = fraud_count * total_count 

    if score < 46 : return "G"
    elif score > 45 and score < 64 : return "Y"
    else : return "R"