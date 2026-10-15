#Write a Python program to reverse each word in a sentence
s = "I am a complain boy"
print(" ".join(word[::-1] for word in s.split())) # 'I' -> 'ma' -> 'a' -> 'nialpmoc' -> 'yob' 