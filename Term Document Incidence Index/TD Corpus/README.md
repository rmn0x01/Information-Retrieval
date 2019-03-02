## Problem Description
Create a simple term-document incidence index from online articles with .txt format <br/>

## Details
*indexing.py*<br/>
Create *title.txt* to list articles file name. <br/>
[Scikit Library](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) is used for indexing from articles listed in *titles.txt*. <br/>
Returning *index.csv* file. <br/>

*query.py*<br/>
The script will take input word and return the search result. <br/>
If the given input is more than 1 word, script will return the search result using **AND** query. <br/>

## Usage
### Create Index
```
python indexing.py
```

### Using Search
```
python query.py
'''

