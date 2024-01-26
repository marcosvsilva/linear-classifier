from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from src.helper import download_csv
import os
import pandas as pd

# features
# 1-long hair
# 2-small lag
# 3-auau sound

def animals():
    pig1 = [0, 1, 0]
    pig2 = [0, 1, 1]
    pig3 = [1, 1, 0]

    dog1 = [0, 1, 1]
    dog2 = [1, 0, 1]
    dog3 = [1, 1, 1]

    train_x = [pig1, pig2, pig3, dog1, dog2, dog3]
    train_y = [1, 1, 1, 0, 0, 0]

    model = LinearSVC()
    model.fit(train_x, train_y)

    test = [1, 1, 1]
    print(model.predict([test]))

def tracking():
    dataset_link = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
    data = pd.read_csv(dataset_link)

    map = {
        "home": "index",
        "how_it_works": "about",
        "contact": "contacts",
        "bought": "target"
    }

    data = data.rename(columns=map)
    columns = [col for col in data.columns if col != "target"]
    x = data[columns]
    y = data["target"]
    
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=.25, stratify=y)

    print("Train size %d, test size %d" % (train_x.shape[0], test_x.shape[0]))

    model = LinearSVC()
    model.fit(train_x, train_y)
    predict = model.predict(test_x)
    
    acc = accuracy_score(test_y, predict)

    print("Model accuracy: %.2f" % (acc*100))
