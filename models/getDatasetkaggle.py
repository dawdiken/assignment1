# Program Name: getDatasetKaggle
# Purpose: Use Kaggle API to get dataset

import kaggle
import requests

site = 'https://www.kaggle.com/'


def request_csv_file():
    """
    Check connection to site where dataset is present

    """
    try:
        # GET request to Kaggle API
        requests.get(site)
    except requests.ConnectionError as conn_error:
        print("connection error")
    else:
        kaggle.api.authenticate()
        # Downloading dataset from Kaggle
        kaggle.api.dataset_download_files('heesoo37/120-years-of-olympic-history-athletes-and-results', path=None, unzip=True)
