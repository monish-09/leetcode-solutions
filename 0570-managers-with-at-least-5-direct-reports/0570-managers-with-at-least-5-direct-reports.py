import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee['managerId'].value_counts()
    manager_ids = counts[counts >= 5].index
    result = employee[employee['id'].isin(manager_ids)][['name']]
    return result