# https://leetcode.com/problems/get-the-size-of-a-dataframe/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    size = list(players.shape)
    return size
