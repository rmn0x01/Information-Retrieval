from whoosh import fields, index
from whoosh.analysis import StemmingAnalyzer
import os.path
import csv

# This list associates a name with each position in a row
columns = ["idwiki", "title", "author","date","genre","synopsis"]

schema = fields.Schema(idwiki=fields.TEXT,
                        title=fields.TEXT(stored=True),
                        author=fields.TEXT(stored=True),
                        date=fields.TEXT(stored=True),
                        genre=fields.TEXT(stored=True),
                        synopsis=fields.TEXT(analyzer=StemmingAnalyzer(),stored=True))

# Create the Whoosh index
indexname = "index"
if not os.path.exists(indexname):
    os.mkdir(indexname)
ix = index.create_in(indexname, schema)

# Open a writer for the index
with ix.writer() as writer:
    # Open the CSV file
    with open("result.csv", "rt", encoding='utf-8') as csvfile:
     # Create a csv reader object for the file
        csvreader = csv.reader(csvfile)
        count=0
     # Read each row in the file
        for row in csvreader:

       # Create a dictionary to hold the document values for this row
            doc = {}
            count+=1
            print(count)
       # Read the values for the row enumerated like
       # (0, "name"), (1, "quantity"), etc.
            for colnum, value in enumerate(row):
                if(colnum<6):
         # Get the field name from the "columns" list

                    fieldname = columns[colnum]

         # Strip any whitespace and convert to unicode
         # NOTE: you need to pass the right encoding here!
                    value = str(value.strip())
                #    print(value)
         # Put the value in the dictionary
                    doc[fieldname] = value
       # Pass the dictionary to the add_document method
                writer.add_document(**doc) 
