import Num_Logics_Functions as nlf

def NL6():
    n=int(input("Enter a number: "))

    if(n>=0):
        print(f"Reverse of number {n} is: ",nlf.Reverse_Num(n))
    else:
        print(f"Reverse of number {n} is: ",nlf.Reverse_Num(-n)*-1)

NL6()