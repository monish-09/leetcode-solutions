import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = distinct_salaries.sort_values(ascending=False).reset_index(drop=True)
    if N <= 0 or N > len(sorted_salaries):
        result = None
    else:
        result = sorted_salaries.iloc[N - 1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})