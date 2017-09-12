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
arr = [0 for i in range(slen+1)]
arst = [0 for i in range(slen+1)]

for i in range(slen):
    print sentoke[i]