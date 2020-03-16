# Extracting Data w/ os, tarfile, urllib

import os # for file handling
import tarfile # for zipped file handling
from six.moves import urllib # for getting url sources

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
# create a folder named 'datasets' and a folder named 'housing' insdie the 'datasets' folder
HOUSING_PATH = os.path.join("datasets", "housing")
# file path of the downloaded files 
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    # make the path if not existed
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    # set the path for target data (save tgv file in 'housing' folder)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    # downloaded files from url would be saved in tgv file path
    urllib.request.urlretreive(housing_url, tgz_path)
    # open, extract, and close the data file
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()