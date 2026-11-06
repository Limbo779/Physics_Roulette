import arxiv as A
import random as rnd 


def r_date():
    YY = str(rnd.randint(12,24))
    MM = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    rnd.shuffle(MM)
    rnd.shuffle(MM)

    return YY+MM[0]

def r_code():
    return str(rnd.randint(1000,99999))

def r_id():
    return r_date()+"."+r_code()

client = A.Client()

for i in range(10000):
    search = A.Search(
        id_list = [r_id()]
    )
    dump = client.results(search)
    try:
        for paper in dump:
            if paper.primary_category.startswith("math"):
                print(dump.title,end="\n\n")
    except:
        continue