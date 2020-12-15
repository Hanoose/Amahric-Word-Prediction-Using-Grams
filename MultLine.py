import nltk
import re
import string 
from nltk.collocations import *
import textwrap

fo = open('amhpre.txt','r', encoding="utf8")
fw = open("amhmul.txt","w+", encoding="utf8")
raw = fo.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
bgs = nltk.bigrams(tokens)

"""
words = raw.split()
# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])

"""
word = raw.split()
#\d|\n|\?|\.|\!|\/|\;|\:|\::|\.|\ ::|\)|\(|\፣

#input_str = ’Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.’
#words = re.sub(r'\d+', '', raw)
#print(result)
#result1 = raw.translate(string.maketrans(','), string.punctuation)
#words = re.sub(r'\d|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.|\ +',' ',raw)
#words= re.sub(r'\d|\n|\t|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.','',raw)
#words = re.sub(' +|\n|\d|\n|\t|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.| +', ' ',raw)

for l in textwrap.wrap("\n".join(word),45):
    print (l)
    fw.write(l+"\n")
fw.close()

#print('\n'.join(words))
#words = re.sub(r'\d|\n|\t|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.',' +', ' ',raw)
print("----------------------------------------")


