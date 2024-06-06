import Num_Logics_Functions as nlf

def NL79():
    lower=int(input("Enter lower range: "))
    upper=int(input("Enter upper range: "))
    kaprekar=[]

    for i in range(lower,upper):
        if nlf.Kaprekar(i)==1:
            kaprekar.append(i)

    print(f"Kaprekar Numbers from {lower} to {upper} are: {kaprekar}")

NL79()