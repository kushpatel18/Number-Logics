import Num_Logics_Functions as nlf

def NL21():
    n=int(input("Enter first number: "))
    m=int(input("Enter second number: "))

    if nlf.Friendly_Pair(n,m)==1:
        print(f"Numbers {n} and {m} are a Friendly Pair")
    else:
        print(f"Numbers {n} and {m} are not a Friendly Pair")

NL21()