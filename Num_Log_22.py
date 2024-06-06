import Num_Logics_Functions as nlf

def NL22():
    n=int(input("Enter a number: "))

    if nlf.Neon(n)==1:
        print(f"Number {n} is a Neon number")
    else:
        print(f"Number {n} is not a Neon number")

NL22()