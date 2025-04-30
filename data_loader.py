class DataLoader:
    def __init__(self):
        self.datasets = {}

    def load_multiple_datasets(self, datasets_info):
        self.datasets.update({
            f"{file_path}:{sheet_name}": self.safe_load(file_path, sheet_name)
            for file_path, sheet_names in datasets_info.items()
            for sheet_name in sheet_names
        })

    def safe_load(self, file_path, sheet_name):
        try:
            return self.load_excel(file_path, sheet_name)
        except Exception as e:
            print(f"Error loading {sheet_name} from {file_path}: {e}")
            return None

