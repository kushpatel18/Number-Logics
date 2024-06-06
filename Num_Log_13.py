import Num_Logics_Functions as nlf

def NL13():
    n=int(input("Enter a number: "))
    # print(type(n))
    # print(nlf.Check_Square(n))

    if nlf.Check_Square(n)==1:
        print(f"Number {n} is a Perfect Square")
    else:
        print(f"Number {n} is not a Perfect Square")

NL13()

