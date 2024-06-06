import Num_Logics_Functions as nlf

def NL66():
    n=int(input("Enter a number: "))
    rev=0

    rev=nlf.Reverse_Rec(n,rev)

    print(f"Reverse Number of {n} is: {rev}")

NL66()
