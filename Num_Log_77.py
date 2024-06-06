import Num_Logics_Functions as nlf

def NL77():

    lower_range=int(input("Enter lower range: "))
    upper_range=int(input("Enter upper range: "))
    abundant=[]
    deficient=[]
    perfect=[]

    for i in range(lower_range,upper_range+1):
        if(nlf.Abundant(i)==1):
            abundant.append(i)
        if(nlf.Deficient(i)==1):
            deficient.append(i)
        if(nlf.Perfect(i)==1):
            perfect.append(i)

    print()

NL77()