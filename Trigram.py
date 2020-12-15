import nltk
from nltk.collocations import *
from nltk import word_tokenize
from nltk.util import ngrams


fo = open('amhpre.txt','r', encoding="utf8")
fw = open("amhtri.txt","w+", encoding="utf8")
raw = fo.read()

tokens = nltk.word_tokenize(raw)
trigrams=ngrams(tokens,2)


#Create your bigrams
bgs = nltk.trigrams(tokens)

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
