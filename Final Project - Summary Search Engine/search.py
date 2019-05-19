from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys

ix = open_dir("index")

print("==========SUMMARY SEARCH ENGINE==========")
query_str = input("Search: ")
print("\nResults: ")

with ix.searcher(weighting=scoring.Frequency) as searcher:
    query = QueryParser("synopsis",schema=ix.schema).parse(query_str)
    results = searcher.search(query,limit=1000)
    
    last = len(results)
    lastPage = last/2/10.0
    if(lastPage%10!=0):
        lastPage = int(lastPage) + 1
    else:
        lastPage = int(lastPage)
    pageNum=1
    
    def openRes(results,choose,pageNum):
        print("Title:",results[choose*2-2]['title'])
        print("Author:",results[choose*2-2]['author'])
        print("Date:",results[choose*2-2]['date'])
        print("Genre:",results[choose*2-2]['genre'])
        print("Summary:\n",results[choose*2-2]['synopsis'])
        action=input("Return to search? (y/n):")
        if(action=='y' or action=='Y'):
            paginate(results,pageNum)
        else:
            print("Closing...")

        

    def paginate(results,pageNum):
        print("\nPage",pageNum,"of",lastPage)
        for i in range(20*(pageNum-1),20*(pageNum)):
            if(i<last):
                if(i%2==0):
                    print(int(i/2)+1," ",results[i]['title'],"\n", results[i]['synopsis'][:200],'...',sep="")
        if(pageNum<lastPage):
            print("\n[N]ext page")
        if(pageNum>1):
            print("[P]revious page")
        print("[G]o to page")
        print("[O]pen result")
        print("[Q]uit")
        action=input("Command: ")
        if(action=='N' or action=='n'):
            paginate(results,pageNum+1)
        elif(action=='P' or action=='p'):
            paginate(results,pageNum-1)
        elif(action=='G' or action=='g'):
            pageNum=int(input("Page: "))
            paginate(results,pageNum)
        elif(action=="O" or action=='o'):
            choose = int(input("Result no.: "))
            if((choose<pageNum*10-10) or (choose>pageNum*10)):
                print('invalid')
                paginate(results,pageNum)         
            else:
                openRes(results,choose,pageNum)
        elif(action=="Q" or action=='q'):
            print("Closing...")
        else:
            print("Wrong command")
            paginate(results,pageNum)
    paginate(results,pageNum)


