import Num_Logics_Functions as nlf

def NL99():
    n=int(input("Enter a number: "))

    if nlf.Keith(n)==1:
        print(f"Number {n} is a Keith number")
    else:
        print(f"Number {n} is not a Keith number")

NL99()