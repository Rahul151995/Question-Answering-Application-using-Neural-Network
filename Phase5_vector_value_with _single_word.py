import nltk as nl
import numpy as np
import gensim as ge
def locationfunc(empl):
    if(empl=='UP'):
        return "true"
    elif(empl=='UttarPradesh'):
        return "true"
    elif(empl=='Noida'):
        return "true"
    elif(empl=='Australia'):
        return "true"
    elif(empl=='India'):
        return "true"
    else:
        return "false"
#INPUT KNOWLEDGE ####################################################################
sentence = "Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language."
sentoke=nl.sent_tokenize(sentence)
slen= len(sentoke)
arr = [0 for i in range(slen+1)]     #initialization of whole array
arst = [0 for i in range(slen+1)]    #initialization of whole array

for p in range(0,(slen)):
    tokens = nl.word_tokenize(sentoke[p])
#print all the tokens
    arst[p]=tokens
    toke=nl.pos_tag(tokens)
    fur=np.array(toke)
    arr[p]=fur    



#printing the different category of sentence such as it is noun,adjective and adverb.
"""
for i in range(0,len(arr)-1):
    for u in range(0,len(arr)-1):
          print arr[i][u]
"""

#print "arst contain all the tokenized data"
#print arst
#print fur[0][0][1]
for i in range(0,len(arr)-1):
    for u in range(0,len(arr[i])-1):
        if arr[i][u][1] =="NN" or arr[i][u][1] =="NNP":
            arr[i][u][1]="Agent"
            blv=locationfunc(fur[i][0])
            if blv=="true":
               arr[i][u][1]="Location"
        elif arr[i][u][1]=="VBZ":
               arr[i][u][1] = "Modifiee"
        elif arr[i][u][1] == "VBZ":
               arr[i][u][1] = "Modifiee"
        elif arr[i][u][1]=="VBD":
              arr[i][u][1] = "Patient"
        
#print len(arr)
 
mrpp=[0 for h in range(len(arst))]
arst = arst[0:len(arst)-1]
mpo=iter(arst)

#printing the vector values of the word with windows size 10 with respect to Python
model=ge.models.Word2Vec(mpo,min_count=1,size=10)
sim=model.most_similar("Python",topn=8)
print sim