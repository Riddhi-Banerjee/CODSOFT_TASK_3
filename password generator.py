import string
import random
l=int(input("Enter length of the password that you want to generate : "))
print("Check the following list for the type of password you want to generate : ")
print("(1) Letter")
print("(2) Numeric")
print("(3) Special Characters")
print("(4) Exit")
ps=""
while True:
    ch=int(input("Enter your choice : (Enter 1/2/3/4(to exit)) : "))
    
    if (ch==1):
        ps=ps+string.ascii_letters
    elif(ch==2):
        ps=ps+string.digits
    elif(ch==3):
        ps=ps+string.punctuation
    elif(ch==4):
        break
    else:
        print("Invalid choice")
pw=[]
for i in range(l):
    randomch=random.choice(ps)
    pw.append(randomch)
print("Your generated password is : ")
for i in range(l):
    print(pw[i],end="")

