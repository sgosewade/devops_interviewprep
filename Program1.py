# 1) Python Program to print duplicates from a list of integers?


list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
dupNum = []
sameNum = []

for x in list1:
	if x not in sameNum:
		sameNum[x] = 1
	else:
		if sameNum[x] == 1
			dupNum.append(x)
		sameNum[x] += 1

print(dupNum)

#2) Reverse words in a given String in Python ( i/p : Hyderabad is the capital of Telangana o/p : Telangana of capital the is Hyderabad)

str = "Hyderabad is the capital of Telangana"
temp = str.split()
temp = list(reversed(temp))

print(" ".join(temp))

#3) Write a Python program to get only ".txt" files in directory? ( ex: Create one folder and create .txt files for input)

import global
import os

os.chdir(r'C:\Users\HP\Documents\Python')
txtFiles = glob.glob('*.txt')
print(txtFiles)


#4) Write a Program to print the number of lines,words and characters present in the given file?

file = open("temp.txt","r")

no_of_lines = 0
no_of_words = 0
no_of_chars = 0

for line in file:
	line = line.strip("\n")
	words = line.split()
	no_of_lines += 1
	no_of_words += len(words)
	no_of_chars += len(lines)
	
file.close()

print("lines:",no_of_lines,"words:",no_of_words,"characters:",no_of_chars)

#5) Given an array arr[] of n elements, write a function to search a given element x in arr[]. (Input : arr[] = {​​​​​10, 20, 40, 60, 50, 110, 100, 130, 170}​​​​​x = 50;


arr[] = {​​​​​10, 20, 40, 60, 50, 110, 100, 130, 170}

x=50

for i in range(len(arr)):
	if arr[i] == x
		print ("X=",x "is found at position:",i)
		return 1
return -1

'''6) Write a python program to replace delimeter as ':' with space and display output on console.
 Example : Input = 'Moschip:Technologies:is:hiring'
Output = 'Moschip Technologies is hiring'
'''

str = "Moschip:Technologies:is:hiring"
tempList = list(str)
delim = ':'

repStr = []

for ele in tempList:
	repStr.append(ele.replace((" "), delim))

print ("Updated list: "+ str(repStr))













	

	
	