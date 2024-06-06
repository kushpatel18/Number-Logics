import Num_Logics_Functions as nlf

def NL97():
    m=int(input("Enter lower range: "))
    n=int(input("Enter upper range: "))
    narcissist=[]

    for i in range(m,n+1):
        if(nlf.Armstrong(i)==1):
            narcissist.append(i)

    print(f" Narcissistic numbers between {m} and {n} are: ",narcissist)

NL97()