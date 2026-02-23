marks = [87,95,46,20,69]
print(marks[0:2])
print(marks[-3:-1])
print(len(marks))
marks.append(68)
print("Marks value of marks after appending the new marks 68")
print(marks,"\nHere is the new length of marks: -",len(marks))
# Using this function of the to reverse the list
marks.reverse()
print(marks)
# sort funtion is use for the sort the value of the list in asending order
marks.sort()
print(marks)
# sort funtion is use for the sort the value of the list in desending order
marks.sort(reverse=True)
print(marks)
marks.insert(2,24)
print(marks)
# Remove the elemet list by giveing the value of the element
marks.remove(24)
print("new list after removeing the element by using the remove function")
print(marks)
marks.pop(2)
print("new list after removeing the indexing by using the pop function")
print(marks)