from whoosh import fields, index
from whoosh.analysis import StemmingAnalyzer
import os.path
import csv

# Nama Fields
columns = ["idwiki", "title", "author","date","genre","synopsis"]

schema = fields.Schema(idwiki=fields.TEXT,
                        title=fields.TEXT(stored=True),
                        author=fields.TEXT(stored=True),
                        date=fields.TEXT(stored=True),
                        genre=fields.TEXT(stored=True),
                        synopsis=fields.TEXT(analyzer=StemmingAnalyzer(),stored=True))

# Whoosh Index
indexname = "index"
if not os.path.exists(indexname):
    os.mkdir(indexname)
ix = index.create_in(indexname, schema)

with ix.writer() as writer:
    with open("result.csv", "rt", encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        count=0         #Debug Counter
        for row in csvreader:
       # Temporary dict to save values
            doc = {}
            count+=1    #Debug Counter
            print(count)
       # Baca value, enumerated
       # (0, "idwiki"), (1, "title"), etc.
            for colnum, value in enumerate(row):
                if(colnum<6):
                    fieldname = columns[colnum]
         # hilangkan whitespace
                    value = str(value.strip())
         # Value -> Dictionary
                    doc[fieldname] = value
       # Dictionary -> Writer
                writer.add_document(**doc) 
