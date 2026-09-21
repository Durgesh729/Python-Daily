s="I am in coma".replace(" ","")
print(set(max(s,key=s.count)))# max(data,rule) here s.count , count every character return occurences of every character in key , s is string 
#set is used for get only unique element