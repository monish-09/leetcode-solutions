import pandas as pd

def valid_emails(Users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    return Users[Users['mail'].str.match(pattern)]
    