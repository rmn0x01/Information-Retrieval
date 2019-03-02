# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
f = open('document.txt').readlines()
vec = CountVectorizer(binary = True)
X = vec.fit_transform(f)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
df.to_csv('index.csv')