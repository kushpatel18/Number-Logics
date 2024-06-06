import Num_Logics_Functions as nlf

def NL44():
    m=int(input("Enter lower range: "))
    n=int(input("Enter upper range: "))
    lst=[]

    for i in range(m,n+1):
        if(nlf.Disarium(i)==1):
            lst.append(i)

    print(f"Disarium Numbers within the range of {m} to {n} are: {lst}")

NL44()