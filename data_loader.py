def handle_exception(action_description, exception):
    print(f"Error during {action_description}: {exception}")

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
      return exception_catcher(self.load_excel, file_path, sheet_name)


