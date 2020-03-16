# OneHotEncoder
    # 숫자로 된 범주형 값을 원-핫 벡터로 바꿔줌 (pandas factorize로 text>integer, sklearn으로 one hot encoding)
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(categories = 'auto')
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
housing_cat_1hot.toarray()
    #toarray() = 넘파이 배열로 바꿔서 호출하기 (Scipy sparse matrix 이기 때문에, numpy의 dense array로 바꿔 출력)
    #reshape에서 -1은 차원을 지정하지 않는 다는 뜻, 1은 1행씩 출력 (1행씩 수천개의 열 출력)