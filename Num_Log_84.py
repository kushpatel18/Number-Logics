import Num_Logics_Functions as nlf

def NL84():
    n=int(input("Enter the number of happy no.'s you want: "))
    happy=[]
    i=0
    num=n

    while num>0:
        if(nlf.Happy(i)==1):
            happy.append(i)
            num-=1
        i+=1


    print(f"First {n} Happy numbers are: ",happy)

NL84()