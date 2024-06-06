import Num_Logics_Functions as nlf

def NL82():
    n=int(input("Enter the number of lucas no.'s you want: "))
    lucas=[]

    for i in range(0,n):
        lucas.append(nlf.Lucas(i))


    print(f"First {n} Lucas numbers are: ",lucas)

NL82()