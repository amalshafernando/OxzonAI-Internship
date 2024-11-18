'''
User Story - 0009 - File Handling
● Topics Covered
    * Reading from and writing to files.
    * File modes (read, write, append) and handling file paths.
● Exercises
    * Write a program to read a text file and count the number of words.
    

'''
count = 0;

file = open("file.txt", "r") # open file in read mode


for line in file:
    words = line.split(" ") #splits lines into words
    count = count + len(words) #count words
   
print("number of words in the file = ", str(count))
file.close()

