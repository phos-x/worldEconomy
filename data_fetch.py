import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from exception import exception_catcher

class DatasetDownloader:
    def __init__(self, download_dir, max_workers=None):
        self.download_dir = download_dir
        self.max_workers = max_workers or os.cpu_count() or 4  # Dynamically set workers
        os.makedirs(download_dir, exist_ok=True)

    def download_files(self, files_info):
        if isinstance(files_info, tuple):
            files_info = [files_info]

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.download_file, url, filename): (url, filename)
                for url, filename in files_info
            }

            for future in as_completed(futures):
                url, filename = futures[future]
                exception_catcher(lambda: future.result(), context=f"downloading {filename} from {url}")

    def download_file(self, url, filename):
        raise NotImplementedError("Implement the `download_file` method to define download logic.")
    

from concurrent.futures import ThreadPoolExecutor, as_completed

class DatasetDownloader:
    def __init__(self, download_dir, max_workers=None):
        self.download_dir = download_dir
        self.max_workers = max_workers or os.cpu_count() or 4 
        os.makedirs(download_dir, exist_ok=True)

    def download_files(self, files_info):
        if isinstance(files_info, tuple):
            files_info = [files_info]

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.download_file, url, filename): (url, filename)
                for url, filename in files_info
            }

            # Process futures as they complete
            for future in as_completed(futures):
                url, filename = futures[future]
                exception_catcher(
                    target_function=lambda: future.result(),
                    context=f"downloading {filename} from {url}"
                )

    def download_file(self, url, filename):
        import requests
        filepath = os.path.join(self.download_dir, filename)
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            return filepath
        else:
            raise Exception(f"Failed to download {url}, HTTP Status Code: {response.status_code}")