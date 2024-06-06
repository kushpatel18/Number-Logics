import Num_Logics_Functions as nlf

def NL43():
    m=int(input("Enter lower range: "))
    n=int(input("Enter upper range: "))
    lst=[]

    for i in range(m,n+1):
        if(nlf.Sunny(i)==1):
            lst.append(i)

    print(f"Sunny Numbers within the range of {m} to {n} are: {lst}")

NL43()