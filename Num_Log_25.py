import Num_Logics_Functions as nlf

def NL25():
    n=int(input("Enter a number: "))

    if nlf.Sunny(n)==1:
        print(f"Number {n} is a Sunny number")
    else:
        print(f"Number {n} is not a Sunny number")

NL25()