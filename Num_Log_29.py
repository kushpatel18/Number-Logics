import Num_Logics_Functions as nlf

def NL29():
    n=int(input("Enter a number: "))
    # print(nlf.Dec_Bin(n))

    if nlf.Evil(n)==1:
        print(f"Number {n} is an Evil number")
    else:
        print(f"Number {n} is not an Evil number")

NL29()