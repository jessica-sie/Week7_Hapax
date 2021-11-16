import os
fName = input("name of program (sample text: textfile.txt) (must have file extension of .txt): ")

#change directory to file 'no2' where textfile.txt is located 
os.chdir('C:\\Users\\Jessica\\Documents\\GitHub\\Week7_Hapax\\no2')
# _cwd = os.getcwd() #test
# print(_cwd) # test


file = open(fName,  "r")
#readlines reads all the lines
conts_b4 = file.readlines() 
file.close()

newFile = open("newFile.txt","w")
num = 1 # line number starts at 1 instead of 0
for line in conts_b4:
    newFile.write(f"{num} " + line)
    num +=1

newFile.close()







