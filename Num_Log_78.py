import Num_Logics_Functions as nlf

def NL78():
    lower=int(input("Enter lower range: "))
    upper =int(input("Enter upper range: "))
    random_int=[]
    length=int(input("Enter the no. of integers you want: "))

    random_int=nlf.Random_Integers(random_int,lower,upper,length)
    print(f"Random integers between {lower} and {upper} are: {random_int}")

NL78()


