from bitarray import bitarray
#ambil dokumen 
docs = open('title2.txt').readlines()
#ambil indeks
indx = open('index2.csv').readlines()
for i in range(len(indx)-1):
    print i #debug
    indx[i+1] = indx[i+1][2:].rstrip().split(',')
#wordlist
words = indx[0].rstrip().split(',')[1:]
#index value
value = []
for i in range(len(indx[1])-1):
    tmp=''
    for j in range(len(indx)-1):
        tmp = tmp+indx[j+1][i]
    value.append(tmp)

def process_query(keyword):
    proc = keyword.split()
    try:
        tmp = bitarray(value[words.index(proc[0])])
    except:
        tmp = bitarray('0'*len(value[0]))
    for i in range(len(proc)-1):
        try:
            a = bitarray(value[words.index(proc[i+1])])
        except:
            a = bitarray('0'*len(value[0]))
        res = (tmp & a)
        tmp = res
    result = []
    for i in range(len(tmp)):
        if tmp[i] == 1:
            result.append(i)
    return find_docs(result)

def find_docs(search):
    print search
    result = []
    for i in search:
        tmp = open('dataset/'+docs[i].rstrip(),'r').read()
        result.append(tmp.rstrip())
    return print_result(result)

def print_result(result):
    if (len(result) > 0):
        print ('\nYour search result(s): \n')
        for i in result :
            print '-> ' + i
    else:
        print "Your keyword does not match any documents"
    print 
        
while(True):
    print('Search :'),
    process_query(raw_input())
