import Num_Logics_Functions as nlf

def NL19():
    n=int(input("Enter a number: "))

    if nlf.Automorphic(n)==1:
        print(f"Number {n} is an Automorphic number")
    else:
        print(f"Number {n} is not an Automorphic number")

NL19()