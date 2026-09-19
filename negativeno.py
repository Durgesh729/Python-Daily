# Keep taking numbers from the user and print them until a negative number appears, then stop the loop. 
n=list(map(int,input("Enter number: ").split()))
for i in n:
    if i>0:
        print(i,end=" ")
    elif i<0:
        break
     