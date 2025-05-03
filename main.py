import os
import requests
from concurrent.futures import ThreadPoolExecutor
from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_visualizer import DataVisualizer
from exception import exception_catcher
import pandas as pd


def main():

    # Load datasets

    datasets_info = {
        './Query1.xlsx': ['new'],  # File path and sheet names
        './inflationData_extracted.xlsx': ['inflationData'],
        './anotherDataset.xlsx': ['Sheet1', 'Sheet2']  # Example for multiple sheets
    }

    data_loader = DataLoader()
    data = data_loader.load_data()
    data_loader.load_multiple_datasets(datasets_info)
    df_port = data_loader.datasets.get('./Query1.xlsx:new')
    df_inflation = data_loader.datasets.get('./inflationData_extracted.xlsx:inflationData')


    #clean data 
    data_cleaner = DataCleaner()
    cleaned_data = data_cleaner.clean_data(data)

    data_visualizer = DataVisualizer()
    data_visualizer.visualize_country_analysis(cleaned_data)
    data_visualizer.visualize_country_comparison(cleaned_data)

if __name__ == "__main__":
    main()






# ---------------------------------------------


# load ImportExportData workbook

# display columns in workbook 
print(df_port.head(5))

# # Remove unwanted columns from the workbook
# df_port.drop(columns=['year-1'], inplace=True)
# # df_gdp.drop(columns=[''], inplace=True)
# # df_inflation.drop(columns=[''], inplace=True)


data = pd.merge(df_port, df_inflation, on='year', how='inner')

data.drop_duplicates(inplace=True)
data.dropna(inplace=True)


print(data.head(50))

# # Save the cleaned output to a new Excel file
output_file = 'economy.xlsx'
data.to_excel(output_file, index=False)

# print(f"Cleaned data saved to {output_file}")