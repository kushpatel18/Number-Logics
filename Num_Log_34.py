import Num_Logics_Functions as nlf

def NL34():
    m=int(input("Enter lower range: "))
    n=int(input("Enter upper range: "))
    lst=[]

    for i in range(m,n+1):
        if(nlf.Strong(i)==1):
            lst.append(i)

    print(f"Strong Numbers within the range of {m} to {n} are: {lst}")

NL34()