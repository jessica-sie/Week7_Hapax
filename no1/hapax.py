import os

import re
def hapax():

    fileN = input("enter file name: ")
    os.chdir('C:\\Users\\Jessica\\Documents\\GitHub\\Week7_Hapax\\no1')
    # _cwd = os.getcwd() #test
    # print(_cwd) # test
    file = open(fileN, "r")
    contents = file.read()
    # print(contents)#test

    # initialize dictionary to store the words 
    wordDict={}

    # make lower case
    contents = contents.lower()
    # print(contents)#test

    # replacing punctuation with space 
    contents = re.sub(r'(?u)[^\w\s]', '', contents)
    
   

    splitCon = contents.split() # [list,list2]
    for word in splitCon:
        wordDict[word] = wordDict.get(word,0)+1

    liHapax=[]
    #append single keys into list 
    for key, value in wordDict.items():
        if value == 1:
            liHapax.append(key)

    print(liHapax)
            

    file.close


hapax()

