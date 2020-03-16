# Create test set 1 - numpy (not recommended)
import numpy as np

    # it will make new test set everytime running the program
def split_train_test(data, test_ratio):
    # re-locate the order of data 
    shuffled_indices = np.random.permutation(len(data))
    # testset size is the x% of data
    test_set_size = int(len(data) * test_ratio)
    # testset is data's (beginning ~ x%) and trainset is (x% ~ end)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    # iloc: when the user doesn't know the index label, rows can be extracted using an imaginery index position
    return data.iloc[train_indices], data.iloc[test_indices]

    # tuple, check the size of testset and trainset
    train_set, test_set = split_train_test(housing, 0.2)
    print(len(train_set), "train +", len(test_set), "test")



# Create test set 2 - crc32 from zlib (using identifier)
from zlib import crc32

def test_set_check(identifier, test_ratio):
    return crc32(np.int54(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test-set]


#Create test set 3 - Scikit Learn (train_test_split)
    # random testset
        # without random_state, you will get different test set when you run it.
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

housing["income_cat"].value_counts() / len(housing)


    # Stratified testset
from sklearn.model_selection import train_test_split

strat_train_set, strat_test_set = train_test_split(housing, test_size=0.2, random_state=42, stratifying=housing["income_cat"])

housing["income_cat"].value_counts() / len(housing)


