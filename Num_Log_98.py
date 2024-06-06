import Num_Logics_Functions as nlf

def NL98():
    n=int(input("Enter the number of pell no.'s you want: "))
    pell=[]

    for i in range(0,n):
        pell.append(nlf.Pell(i))


    print(f"First {n} Pell numbers are: ",pell)

NL98()