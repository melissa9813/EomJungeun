#Create test set - Scikit Learn (train_test_split)
    # random testset
        # without random_state, you will get different test set when you run it.
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

housing["income_cat"].value_counts() / len(housing)


    # Stratified testset
from sklearn.model_selection import train_test_split

strat_train_set, strat_test_set = train_test_split(housing, test_size=0.2, random_state=42, stratifying=housing["income_cat"])

housing["income_cat"].value_counts() / len(housing)


