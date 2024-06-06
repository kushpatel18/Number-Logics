import Num_Logics_Functions as nlf

def NL73():
    n=int(input("Enter a number:"))
    max_digit=0
    sec_max=0

    sec_max=nlf.Sec_Max_Digit(n,max_digit,sec_max)
    print(f"Second largest digit of number {n} is: {sec_max}")

NL73()