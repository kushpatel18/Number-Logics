import Num_Logics_Functions as nlf

def NL83():
    n=int(input("Enter the number of catalan no.'s you want: "))
    catalan=[]

    for i in range(0,n):
        fact1=nlf.factorial(2*i)
        fact2=nlf.factorial(i+1)
        fact3=nlf.factorial(i)
        catln=int(fact1/(fact2*fact3))
        catalan.append(catln)


    print(f"First {n} Catalan numbers are: ",catalan)

NL83()