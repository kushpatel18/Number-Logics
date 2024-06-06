import Num_Logics_Functions as nlf

def NL91():
    n=int(input("Enter a number: "))

    if nlf.Circular_Prime(n)==1:
        print(f"Number {n} is a Circular Prime number")
    else:
        print(f"Number {n} is not a Circular Prime number")

NL91()