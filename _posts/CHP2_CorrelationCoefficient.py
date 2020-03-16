## Research correlation coefficient between the features
        # using pandas

    # Standard correlation coefficient (corr() method)
    corr_matrix = housing.corr()
    corr_matrix["median_house_value"].sort_values(ascending=False)

    # Scatter_matrix
    from pandas.plotting import scatter_matrix

    attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]

    scatter_matrix(housing[attributes], figsize=(12,8))


## Check the combinatinos of features
    # 한 가구당 방 개수
    housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
    
    # 한 방 당 침실 개수
    housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]

    # 한 가구당 사람 수
    housing["population_per_household"] = housing["population"]/housing["households"]

    # 위 세개의 특성조합을 포함하여 다시 standard correlation coefficient 비교해보기
    corr_matrix = housing.corr()
    corr_matrix["median_house_value"].sort_values(ascending=False)