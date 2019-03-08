# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
titles = open('titles.txt').readlines()
f = []
x = 1	#debug
for i in titles:
    print x	#debug
    x+=1	#debug
    g = open('dataset/'+i.rstrip(),'r').read()
    f.append(g)
vec = CountVectorizer(binary = True)
X = vec.fit_transform(f)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
df.to_csv('index.csv')
