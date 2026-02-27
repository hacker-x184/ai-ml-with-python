set1= {54,68,65,64,12,148,21,6,53,24,45,"Hello","Wolrd","What's up","new"}
print(set1)
set1.add(57)#To add the elemnt in the set 
print(set1)
set1.remove(54)#To remove the  element fromm teh set
print(set1)
set1.pop()#To remove the randome value fro the set
print(set1)
set1.clear()#From makeing the set completely empty
set1.add(57)
print(set1)
set1.add(88)
print(set1)
set1.add("Hello")
print(set1)
set1.add("I'm Inzamam")
print(set1)
set1.add("Hey What's up")
print(set1)
set1.add(3534.5j)
set4 =set1
set2={"Inzamam","CSE-(AI/ML)",74.61,54,"World","Hello"}
set1.union(set2)#this funtion helps us to Connect the two set but commmon value will not repate
print(set1)
set3 = {"Inzamam","CSE-(AI/ML)",74.61,54,"World","Hello"}
set3.intersection(set4)#This function help us to get the only comman valuse in both of the sets
print(set3)

