from sklearn.svm import LinearSVC

# features
# 1-long hair
# 2-small lag
# 3-auau sound

pig1 = [0, 1, 0]
pig2 = [0, 1, 1]
pig3 = [1, 1, 0]

dog1 = [0, 1, 1]
dog2 = [1, 0, 1]
dog3 = [1, 1, 1]

data = [pig1, pig2, pig3, dog1, dog2, dog3]
labels = [1, 1, 1, 0, 0, 0]

model = LinearSVC()
model.fit(data, labels)

test = [1, 1, 1]
print(model.predict([test]))
