import Num_Logics_Functions as nlf

def NL95():
    n=int(input("Enter upper range: "))
    ramanujan=[]

    for i in range(1,n+1):
        if nlf.Ramanujan(i)==1:
            ramanujan.append(i)

    print(f"Ramanujan Numbers between 1 and {n} are: {ramanujan}")

    # print(nlf.Ramanujan(n))


NL95()