import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def load_folder(name):

    path = f'{name}/'  # or unix / linux / mac path

    # Get the files from the path provided in the OP
    files = list(Path(path).glob('*.csv')) # .rglob to get subdirectories

    # Read the files into dataframes
    dfs = [pd.read_csv(f) for f in files]

    # Combine the list of dataframes
    df = pd.concat(dfs, ignore_index=True)

    # Add a new column
    df['Source'] = np.repeat([f'S{i}' for i in range(len(dfs))], [len(df) for df in dfs])
    return df

def seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"