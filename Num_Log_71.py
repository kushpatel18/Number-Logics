import Num_Logics_Functions as nlf

def NL71():
    n=int(input("Enter a number:"))
    min_digit=9

    min_digit=nlf.Min_Digit(n,min_digit)
    print(f"Max digit of number {n} is: {min_digit}")

NL71()