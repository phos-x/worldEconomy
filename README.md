# World Trade Data Analysis

This repository contains a Python-based project for analyzing world trade data. It includes modules for loading, cleaning, and visualizing datasets related to trade, inflation, and other economic indicators.

## This Code Has Not Been Tested. Currently Fascinated with Other Projects.

## Features

- **Data Loading**: Load multiple datasets from Excel files, including support for multiple sheets.
- **Data Cleaning**: Remove duplicates, handle missing values, and clean datasets for analysis.
- **Data Visualization**: Generate visualizations for country-specific analysis and comparisons.
- **Data Merging**: Combine datasets for deeper insights into economic trends.

## Project Structure

worldTrade/ │ 
├── main.py # Main script to run the project 
├── data_loader.py # Module for loading datasets 
├── data_cleaner.py # Module for cleaning datasets 
├── data_visualizer.py # Module for visualizing data 
├── exception.py # Module for handling exceptions 


## Requirements

- Python 3.8 or higher
- Libraries:
  - `pandas`
  - `openpyxl`
  - `matplotlib`
  - `seaborn`

Install the required libraries using:
```bash
pip install pandas openpyxl matplotlib seaborn

Example Workflow
1. Load Datasets
The DataLoader class loads datasets from Excel files. You can specify file paths and sheet names in the datasets_info dictionary.

2. Clean Data
The DataCleaner class removes duplicates, handles missing values, and prepares the data for analysis.

3. Visualize Data
The DataVisualizer class generates visualizations for:

Country-specific analysis
Country comparisons
4. Merge and Save Data
The datasets are merged on common columns (e.g., year) and saved to an Excel file (economy.xlsx).
