import arxiv as A
import random as rnd 
import time

def r_date():
    YY = str(rnd.randint(12,24))
    MM = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    rnd.shuffle(MM)
    rnd.shuffle(MM)

    return YY+MM[0]

def r_code():
    return f"{rnd.randint(1, 3000):05d}"

def r_id():
    return r_date()+"."+r_code()

client = A.Client()

domain = ["cs.CC","cs.AI","cs.DS","cs.GR","math.HO","gr-qc","quant-ph","physics.class-ph","q-fin.CP","q-fin.TR"]

for i in range(16000):
    if (i%100 == 0):
        print("\n\n\nTime to sleep zzzzz\n\n\n")
        time.sleep(10)
    id = r_id()
    search = A.Search(
        id_list = [id]
    )
    dump = list(client.results(search))
    if not (not dump):
        for paper in dump:
            dumainu = []
            for i in domain:
                if paper.primary_category.startswith(i):
                    dumainu.append(i)
            if not (not dumainu):
                print(f"Checking id : {id}  ||  Paper found !!",end="\n\n")
                print(paper.title,end="\n\n")
                with open("absolute_garbage_candidates.txt", "a", encoding="utf-8") as f:
                    f.write(f"ID: {id}\nTitle: {paper.title}\n\nCatagories:\n")
                    for i in dumainu:
                        f.write(f"{i}\n")
                    f.write(f"\nAbstract:\n{paper.summary}\n")
                    f.write("="*60 + "\n\n\n")
            
            else:
                print(f"Checking id : {id}  ||  Paper found BUT NOT OUR INTEREST  ")
    else:
        print(f"Checking id : {id}  ||  NO PAPER FOUND :(  ")
        continue