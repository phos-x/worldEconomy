from exception import exception_catcher
import pandas as pd

class DataCleaner:
    def __init__(self):
        pass

    def clean_data(self, data):
        try:
            if data is None:
                raise ValueError("No data provided for cleaning.")
            cleaned_data = data.dropna()
            print("Data cleaned successfully.")
            return cleaned_data
        except Exception as e:
            exception_catcher(e)
            return None

    def clean_and_join(self, datasets, join_columns):
        try:
            if not datasets or len(datasets) < 2:
                raise ValueError("At least two datasets are required for joining.")
            if not join_columns:
                raise ValueError("Join columns must be specified.")

            cleaned_datasets = []
            for i, data in enumerate(datasets):
                print(f"Cleaning dataset {i + 1}...")
                cleaned_data = self.clean_data(data)
                if cleaned_data is None:
                    raise ValueError(f"Failed to clean dataset {i + 1}.")
                cleaned_datasets.append(cleaned_data)

            joined_data = cleaned_datasets[0]
            for i in range(1, len(cleaned_datasets)):
                joined_data = joined_data.merge(cleaned_datasets[i], on=join_columns, how='inner')

            print("Datasets joined successfully.")
            return joined_data
        except Exception as e:
            exception_catcher(e)
            return None

    def load_input(self, input_source):
        try:
            if isinstance(input_source, str):  # Assume it's a file path
                print(f"Loading datasets from file: {input_source}")
                with open(input_source, 'r') as file:
                    dataset_paths = file.read().splitlines()
                datasets = [pd.read_csv(path) for path in dataset_paths]
            elif isinstance(input_source, list):  # Assume it's a list of datasets
                print("Loading datasets from variable.")
                datasets = input_source
            else:
                raise ValueError("Invalid input source. Must be a file path or a list of datasets.")
            
            print("Datasets loaded successfully.")
            return datasets
        except Exception as e:
            exception_catcher(e)
            return None
