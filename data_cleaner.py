# Handles cleaning of data.

class DataCleaner:
    def clean_data(self, data):
        if data is None:
            print("No data to clean.")
            return None
        data = data.dropna()
        print("Data cleaned successfully.")
        return data



