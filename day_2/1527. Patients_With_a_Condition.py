import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
     pd.DataFrame(person.iloc[1:].sort_values(by='id',inplace=True)).drop_duplicates(subset='email',inplace=True,keep='first')
    