import Num_Logics_Functions as nlf

def NL81():
    n=int(input("Enter the number of narcissist decimal no.'s you want: "))
    narcissist=[]
    i=0
    num=n

    while num>0:
        if(nlf.Armstrong(i)==1):
            narcissist.append(i)
            num-=1
        i+=1

    print(f"First {n} Narcissistic decimal numbers are: ",narcissist)

NL81()