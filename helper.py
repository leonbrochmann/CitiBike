import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os


def load_and_clean_csv(file_path):
    """
    Load a single CSV file and clean its data.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A cleaned DataFrame.
    """
    df = pd.read_csv(file_path)
    
    first_column_name = df.columns[0]
    
    # Rename all columns to the first column name

    # Rename columns if necessary
    column_mapping = {
        'start_time': 'starttime',
        'stop_time': 'stoptime',
        'trip_duration': 'tripduration',
        'start_station_id': 'start_station_id',
        'end_station_id': 'end_station_id',
        'bike_id': 'bikeid',
        'user_type': 'usertype',
        'birth_year': 'birth_year',
        'gender': 'gender'
    }
    df.rename(columns=column_mapping, inplace=True)

    # Convert columns to appropriate types
    if 'starttime' in df.columns:
        df['starttime'] = pd.to_datetime(df['starttime'], errors='coerce')
    if 'stoptime' in df.columns:
        df['stoptime'] = pd.to_datetime(df['stoptime'], errors='coerce')
    if 'tripduration' in df.columns:
        df['tripduration'] = pd.to_numeric(df['tripduration'], errors='coerce')
    if 'start_station_id' in df.columns:
        df['start_station_id'] = pd.to_numeric(df['start_station_id'], errors='coerce')
    if 'end_station_id' in df.columns:
        df['end_station_id'] = pd.to_numeric(df['end_station_id'], errors='coerce')
    if 'bikeid' in df.columns:
        df['bikeid'] = pd.to_numeric(df['bikeid'], errors='coerce')
    if 'usertype' in df.columns:
        df['usertype'] = df['usertype'].astype('category')
    if 'birth_year' in df.columns:
        df['birth_year'] = pd.to_numeric(df['birth_year'], errors='coerce')
    if 'gender' in df.columns:
        df['gender'] = pd.to_numeric(df['gender'], errors='coerce')
    
    return df

def load_and_clean_2016_csv(file_path):
    """
    Load a single CSV file from 2016 and clean its data.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A cleaned DataFrame.
    """
    df = pd.read_csv(file_path)
    
    # Ensure all column names are in lowercase
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '', regex=True)
    
    column_mapping = {
        'Trip Duration': 'tripduration',
        'Start Time': 'starttime',
        'Stop Time': 'stoptime',
        'Bike ID': 'bikeid',
        'User Type': 'usertype'
    }
    df.rename(columns=column_mapping, inplace=True)

    # Convert columns to appropriate types
    if 'starttime' in df.columns:
        df['starttime'] = pd.to_datetime(df['starttime'], errors='coerce')
    if 'stoptime' in df.columns:
        df['stoptime'] = pd.to_datetime(df['stoptime'], errors='coerce')
    if 'tripduration' in df.columns:
        df['tripduration'] = pd.to_numeric(df['tripduration'], errors='coerce')
    if 'start_station_id' in df.columns:
        df['start_station_id'] = pd.to_numeric(df['start_station_id'], errors='coerce')
    if 'end_station_id' in df.columns:
        df['end_station_id'] = pd.to_numeric(df['end_station_id'], errors='coerce')
    if 'bikeid' in df.columns:
        df['bikeid'] = pd.to_numeric(df['bikeid'], errors='coerce')
    if 'usertype' in df.columns:
        df['usertype'] = df['usertype'].astype('category')
    if 'birth_year' in df.columns:
        df['birth_year'] = pd.to_numeric(df['birth_year'], errors='coerce')
    if 'gender' in df.columns:
        df['gender'] = pd.to_numeric(df['gender'], errors='coerce')
    
    return df

def load_folder(folder_path, year = None):
    """
    Load all CSV files in the specified folder into a single pandas DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all CSV files.
    """
    # Get the list of all CSV files in the folder
    files = list(Path(folder_path).glob('*.csv'))

    # Read each CSV file into a DataFrame and store them in a list
    # Read and clean each CSV file into a DataFrame and store them in a list
    if year == 2016:
        dfs = [load_and_clean_2016_csv(file) for file in files]
    else:
        dfs = [load_and_clean_csv(file) for file in files]

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df

def seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"



def load_and_rename_csv_files(folder_path, column_names):
    """
    Load all CSV files in the specified folder into a single pandas DataFrame,
    rename columns for each DataFrame to the specified list of column names,
    and concatenate them into a single DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    column_names (list): The list of column names to rename each DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all CSV files with renamed columns.
    """
    # Initialize a list to store DataFrames
    dfs = []

    # Get the list of all CSV files in the folder
    files = list(Path(folder_path).glob('*.csv'))

    # Read and clean each CSV file into a DataFrame and append to the list
    for file in files:
        df = pd.read_csv(file)
        
        # Rename columns to the specified list of column names
        df.columns = column_names

        df['starttime'] = pd.to_datetime(df['starttime'], errors='coerce')
        df['stoptime'] = pd.to_datetime(df['stoptime'], errors='coerce')

        # Append the cleaned DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df



def load_and_rename_csv_files_2020(folder_path, column_names):
    """
    Load all CSV files in the specified folder into a single pandas DataFrame,
    rename columns for each DataFrame to the specified list of column names,
    and concatenate them into a single DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    column_names (list): The list of column names to rename each DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all CSV files with renamed columns.
    """
    # Initialize a list to store DataFrames
    dfs = []

    # Get the list of all CSV files in the folder
    files = list(Path(folder_path).glob('*.csv'))

    # Read and clean each CSV file into a DataFrame and append to the list
    for file in files:
        df = pd.read_csv(file)
        
        # Rename columns to the specified list of column names
        df.columns = column_names

        df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce')
        df['ended_at'] = pd.to_datetime(df['ended_at'], errors='coerce')

        # Append the cleaned DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df

import pandas as pd
from pathlib import Path

def load_and_rename_2024_07(folder_path, column_names):
    """
    Load all CSV files in the specified folder into a single pandas DataFrame,
    drop the first column for each DataFrame, rename columns to the specified list of column names,
    and concatenate them into a single DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    column_names (list): The list of column names to rename each DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all CSV files with renamed columns.
    """
    # Initialize a list to store DataFrames
    dfs = []

    # Get the list of all CSV files in the folder
    files = list(Path(folder_path).glob('*.csv'))

    # Read and clean each CSV file into a DataFrame and append to the list
    for file in files:
        df = pd.read_csv(file)
        
        # Drop the first column
        df.drop(df.columns[0], axis=1, inplace=True)
        
        # Rename columns to the specified list of column names
        df.columns = column_names

        # Convert started_at and ended_at columns to datetime
        df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce')
        df['ended_at'] = pd.to_datetime(df['ended_at'], errors='coerce')

        # Append the cleaned DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df


def create_folder(path, folder_name):
    """
    Create a folder in the specified path with the given name.

    Parameters:
    path (str): The path where the folder should be created.
    folder_name (str): The name of the folder to be created.

    Returns:
    str: The full path of the created folder.
    """
    # Combine the path and folder name to get the full path
    full_path = os.path.join(path, folder_name)

    # Create the folder if it does not exist
    os.makedirs(full_path, exist_ok=True)

    return full_path

# Example usage
