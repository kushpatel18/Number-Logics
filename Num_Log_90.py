import Num_Logics_Functions as nlf

def NL90():
    n=int(input("Enter a number: "))
    m=int(input("Enter a number: "))

    if nlf.AmicablePair(n,m)==1:
        print(f"Numbers {n} and {m} are an Amicable pair")
    else:
        print(f"Numbers {n} and {m} are not an Amicable pair")

NL90()