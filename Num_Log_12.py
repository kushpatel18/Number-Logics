import Num_Logics_Functions as nlf

def NL12():
    n=int(input("Enter a number: "))

    if nlf.Prime(n)==1 :
        print(f"Number {n} is Prime")
    else:
        print(f"Number {n} is not Prime")

NL12()