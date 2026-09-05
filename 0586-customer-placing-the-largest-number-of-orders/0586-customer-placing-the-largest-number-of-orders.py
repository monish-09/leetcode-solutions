import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    count = orders.groupby('customer_number')['order_number'].count()
    
    customer = count.idxmax()
    
    return pd.DataFrame({'customer_number': [customer]})
    