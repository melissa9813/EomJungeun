# read / analyze the data using pandas
# refer all the pandas dataframe objects
import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    # get the file path of csv file saved in the housing_path
    csv_path = os.path.join(housing_path, "housing.csv")
    # read the csv file in the housing_path
    return pd.read_csv(csv_path)


housing = load_housing_data
# head() = show the first five rows including header of columns
housing.head() 

# info() = show the brief description (# of rows, datatype, # of non-null...)
housing.info()

# value_contents() = show the categories, # of each categories
housing["ocean_proximity"].value_contents()

# describe() = shows the summary of numeric info (std, min, max, count, 25%, 50%, 75%...)
housing().describ()

# factorize() = text-type categories를 integer로 매핑
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = housing_cat.factorize()
housing_cat_encoded[:10]
    # 첫 10개를 integer 타입으로 변형해줌 (ex) 1H OCEAN=0, NEAR OCEAN=1, INLAND=2, NEAR BAY=3, ISLAND=4