import pandas as pd
import os

from config import ROOT_DIR


def load_data(split: str = 'train'):
    data_path = os.path.join(ROOT_DIR, split)
    return pd.read_csv(data_path)
