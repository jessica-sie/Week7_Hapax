import os 
import re

# find directory, open, read, close file 
os.chdir('C:\\Users\\Jessica\\Documents\\GitHub\\Week7_Hapax\\no4')
file = open("text.txt", "r")
contents = file.read()
file.close()

capitalLetters= "([A-Z])"
lowercase = "([a-z])"
digits = "([0-9])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
websites = "[.](com|net|org|io|gov)"
ie = "(i)[.](e)[.]"

# line -> space
edited = contents.replace("\n"," ") 
# for prefix no split
edited = re.sub(prefixes,"\\1<prd>",edited) 
# suffix no split
edited = re.sub(" "+suffixes+"[.]"," \\1<prd>",edited)
# for websites no split 
edited = re.sub(websites,"<prd>\\1",edited)
# decimals b4 no split
edited = re.sub("[.]" + digits,"<prd>\\1",edited) 
# decimals between no split 
edited = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",edited) 
# i.e. -> i<prd>e<prd>
edited = re.sub(ie, "i<prd>e<prd>", edited)  

edited = edited.replace("...","<prd><prd><prd><next>") 
edited = edited.replace(".",".<next>")
edited = edited.replace("?","?<next>")
edited = edited.replace("!","!<next>")
edited = edited.replace("<prd>",".") 
next= edited.split("<next>") 
next = [sent.strip() for sent in next]

print(*next, sep="\n")