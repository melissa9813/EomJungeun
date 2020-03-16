    # SimpleImputer (Null values들을 특정 값으로 채움)

from sklearn.impute import SimpleImputer
#median으로 Null value채우기
imputer = SimpleImputer(strategy = "median")

#text data type인 column을 drop하고 복사본 생성
housing_num = housing.drop("ocean_proximity", axis=1)
#fit() = compute the stats
imputer.fit(housing_num)

imputer.statistics_
housing_num.median().values

#X = numpy array that computed stats replace Null values
X=imputer.transform(housing_num)

#Using pandas dataframe, it can be simply returned
housing_tr = pd.Dataframe(X, columns=housing_num.columns, index=list(housing.index.values))




    # dropna(), drop(), fillna()
housing.dropna(subset=["total_bedrooms"]) # null values 제거
housing,drop("total_bedrooms", axis=1) # null values가 있는 column 자체 제거
median = housing["total_bdrooms"].median #median 계산
housing["total_bedrooms"].fillna(median, inplace=True) #median으로 null values 채우기