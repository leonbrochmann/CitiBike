# Data Analysis Project

This repository contains code and data for analyzing bike trip and collision data. The project includes functions for loading, cleaning, and visualizing the data.  
Main Recipient is the AXA Innovation Lab

## Table of Contents

- [Installation](#installation)
- [General Information](#general-information)
- [Functions](#functions)
- [Usage](#usage)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/leonbrochmann/CitiBike.git
    ```

2. Navigate to the project directory:
    ```sh
    cd your folder name
    ```

3. Create a virtual environment and activate it:
    Unfortunatly i had no time to set up poetry, so no lock file is included

4. Install the required packages(As soon as the poetry toml is added):
    ```sh
    poetry install
    ```
## General Information before anything is executed  
1. All of this code was done locally on a pc with limited resources.  
Therefore all parts of the analysis where split into each year and sometimes even into months of the year.  
If possible, with available ressources, build a datamart for the whole database and another for all nypd data or comparable company data to make data access more efficient.  
2. For data before 2020, use the 2015.ipynb file, otherwise the 2020-2024.ipynb .
## Usage

1. Load and clean data:
   There are 2 distinct methods to load the data currently:  
   For data before 2020 use the method **load_and_rename_csv_files**  
   For data starting 2020 use the method **load_and_rename_csv_files_2020**  
   Both are found in the helper.py, and need all the column names they use so that you avoid data issued, especially the datetimes.

2. Timedata format:  
Almost all of the datafiles have timedata issues, so after converting them into a pandas datetime you can used the function **seconds_to_hhmmss** to convert seconds to hhmmss for better readability.


## Next Steps  
1. Demand Forecast at Stations:  
    One possible next step would be to create a forecast service to see how many people need bikes at certain stations and current traffic in NYC to predict whether or not a insurance would be important.  
2. Compare the data with simliar scooter services to see their rates of accidents, demand and even times of lending.  

## License
The data used in this repo completely belongs to citibike. They hold all rights to the data.