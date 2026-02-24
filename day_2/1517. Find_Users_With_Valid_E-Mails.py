import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    condition = users['mail'].str.match(r"^[a-zA-Z][a-zA-Z0-9_.\-]*@leetcode\.com$")
    return users.loc[condition, ['user_id','name','mail']]
    