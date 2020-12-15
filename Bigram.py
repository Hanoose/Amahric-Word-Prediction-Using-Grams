import nltk
from nltk.collocations import *

fo = open('amhpre.txt','r', encoding="utf8")
fw = open("amhbig.txt","w+", encoding="utf8")
raw = fo.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
bgs = nltk.bigrams(tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    print (v,(" ").join(k))
    #w= v,(" ").join(k)
    g = str(v)
    fw.write(str("\n"))
    fw.write(str(g))
    fw.write(str(" "))
    fw.write(" ".join(" ").join(k))
    #fw.write("kiki")
fw.close()
