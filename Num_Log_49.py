import Num_Logics_Functions as nlf

def NL49():
    n=int(input("Enter a number: "))
    i=0
    temp=n+1
    lst=[]

    while temp>0:
        if(nlf.Prime(i)==1):
            lst.append(i)
            temp-=1
        i+=1
    # print(lst)

    print(f"The {n}th term of Prime numbers is: {lst[n-1]}")


NL49()