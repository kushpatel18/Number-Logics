import Num_Logics_Functions as nlf

def NL72():
    n=int(input("Enter a number: "))
    m=int(input("Enter a number: "))

    if nlf.AmicablePair(n,m)==1:
        print(f"Numbers {n} and {m} are an amicable pair")
    else:
        print(f"Numbers {n} and {m} are not an amicable pair")

NL72()