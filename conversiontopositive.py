#Write a Python program to convert all negative numbers in a list to positive.
l=[-1,-2,-7,8,91,11,-7]
print([-i for i in l if i<0]+[i for i in l if i>0])