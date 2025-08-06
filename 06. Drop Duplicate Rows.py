# https://leetcode.com/problems/drop-duplicate-rows/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')
