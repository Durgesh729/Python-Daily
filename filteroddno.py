#filter required 2 arguments filter(function(condition),list) need to declare inside list 
#because it will return memory address of that .
l=[1,2,3,4,5]
print(list(filter(lambda x:x%2!=0,l)))