from typing import List
import pandas as pd


def read_prdnames(path: str) -> List:
    return pd.read_csv(path).iloc[:, 0].to_list()


