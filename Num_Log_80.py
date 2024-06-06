import Num_Logics_Functions as nlf

def NL80():
    lower=int(input("Enter lower range: "))
    upper=int(input("Enter upper range: "))
    lychrel=[]
    iterations=0

    for i in range(lower,upper+1):
        if nlf.Lychrel(i,iterations)==1:
            lychrel.append(i)

    print(f"Lychrel Numbers from {lower} to {upper} are: {lychrel}")

    lychrel_seeds=[]

NL80()