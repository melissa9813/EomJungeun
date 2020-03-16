# 나만의 transformer 만들기

# 조합 특성을 추가하는 변환기 - TransformMixin
from sklearn.base import BaseEstimator, TransformerMixin

# 3, 4, 5, 6은 각각 total_rooms, total_bedrooms 등등의 index number
rooms_ix, bedrooms_ix, population_ix, household_ix = 3,4,5,6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    #estimator - fit()
    def fit(self, X, y=None):
        return self

    #transformer - transform()
    def transform(self, X, y=None):

        # [:, rooms_ix] = 전체중에서 rooms_ix 즉 total_rooms column만 select
        # total number of rooms / total number of household 와 같은 표현
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]

        #np.c_ 는 두개의 1차원 배열을 세로로 나열하여 2차원 배열로 만드는 것
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)