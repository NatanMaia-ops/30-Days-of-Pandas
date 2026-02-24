import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    condition = ~customers['id'].isin(orders['customerId'])
    return pd.DataFrame(customers.loc[condition, ['name']]).rename(columns={"name":"Customers"})

    