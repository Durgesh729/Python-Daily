#7.	Write a program to check whether a character is a vowel or a consonant. 
n = input("Enter character: ")

if len(n) != 1 or not n.isalpha():
    print("Please enter only one alphabet character.")
elif n.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
