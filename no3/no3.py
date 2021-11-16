"""
calculate average word length of a text stored in a file
"""

import os
import re 

# find directory, open and read file 
os.chdir('C:\\Users\\Jessica\\Documents\\GitHub\\Week7_Hapax\\no3')
file = open("textfile.txt", "r")
contents = file.read()

# total number of letters in a text file
splitCon = contents.split() 
ttl_letters = sum (len(word) for word in splitCon)

# total number of words in a text file
word_count = len(splitCon)

av = ttl_letters / word_count
print("average word length is {:.3} to 2 decimal places ".format(av))
file.close()