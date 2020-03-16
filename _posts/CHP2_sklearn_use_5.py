# Pipeline class (정확한 순서대로 변환단계를 진행 시켜줌)

## Pipeline -- Standardization
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

    # Order is important
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

housing_num_tr = num_pipeline.fit_transform(housing_num)


## DataFrameSelector (pandas Dataframe을 처리)
    #필요한 특성을 선ㅌ낵하여 넘파이 배열로 바꿔줌
from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


## Pipeline for numeric and categorical dataframe
num_attribs = list(housing_num) #앞에서 미리 numeric columns들만 모아놓음 = housing_num
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline({
    ('selector', DataFrameSelector(num_attribs)),
    ('imputer', SimpleImputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
})

cat_pipeline = Pipeline([
    ('selector', DataFrameSelector(cat_attribs)),
    ('cat_encoder', OneHotEncoder(sparse=False)),
])


## 위 두개의 pipelines을 하나로 합치기
from sklearn.pipeline import FeatureUnion

full_pipeline = FeatureUnion(transformer_list = [
    ("num_pipeline", num_pipeline),
    ("cat_pipeline", cat_pipeline),
])

    #pipeline 실행
housing_prepared = full_pipeline.fit_transform(housing)
housing_prepared

housing_prepared.shape