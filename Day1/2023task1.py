#---------------------------------------------PART 1----------------------------------------------------
file=open("task1.txt","r")
i=0
sum=0
list_of_numbers=[]
for line in file:
  for char in line:
    if char.isdigit():
      list_of_numbers.append(int(char))
      #checks if integer, if so adds to the list
      i+=1
  if i>0:
    sum+=int((str(list_of_numbers[0])+str(list_of_numbers[i-1])))
    #concatenates first in list to end of list, then adds the integer produced to the sum
  list_of_numbers.clear()
  i=0
print(sum)
file.close()
#---------------------------------------------PART 2----------------------------------------------------
file=open("task1.txt","r")
numbers= {'one':'o1e',
          'two':'2',
          'three':'th3ee',
          'four':'4',
          'five':'fi5e',
          'six':'6',
          'seven':'sev7n',
          'eight':'eig8t',
          'nine':'ni9e'}
#this avoids us from replacing numbers wrongly, as strings such as 'threeight' are not replaced appropiately otherwise.
sum=0
for line in file:
  for number in numbers:
    if number in line:
      line=line.replace(number,numbers.get(number))
  for char in line:
    if char.isdigit():
      list_of_numbers.append(int(char))
      i+=1

  if i>0:
    sum+=int((str(list_of_numbers[0])+str(list_of_numbers[i-1])))
  list_of_numbers.clear()
  i=0
print(sum)
file.close()
#same logic as first part of problem used to solve problem, after issue involving combined numbers is dealt with.
