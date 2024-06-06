import Num_Logics_Functions as nlf

def NL74():
    n=int(input("Enter a number:"))
    min_digit=9
    sec_min=9

    sec_min=nlf.Sec_Min_Digit(n,min_digit,sec_min)
    print(f"Second Smallest digit of number {n} is: {sec_min}")

NL74()