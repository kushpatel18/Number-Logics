import Num_Logics_Functions as nlf

def NL87():
    n=int(input("Enter a number: "))

    if nlf.Harshad(n)==1:
        print(f"Number {n} is a Harshad number")
    else:
        print(f"Number {n} is not a Harshad number")

NL87()