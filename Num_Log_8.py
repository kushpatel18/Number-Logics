import Num_Logics_Functions as nlf

def NL8():
    n=int(input("Enter first number: "))
    m=int(input("Enter second number: "))

    if n>0 and m>0:
        print(f"LCM of number {n} and {m} is: ",nlf.LCM(n,m))
    else:
        print("LCM is not possible")

NL8()