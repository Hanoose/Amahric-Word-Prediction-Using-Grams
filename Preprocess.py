import nltk
import re
import string 
from nltk.collocations import *

fo = open('amhcol.txt','r', encoding="utf8")
fw = open("amhpre.txt","w+", encoding="utf8")
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
#\d|\n|\?|\.|\!|\/|\;|\:|\::|\.|\ ::|\)|\(|\፣

#input_str = ’Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.’
#result = re.sub(r'\d+', '', raw)
#print(result)
#result1 = raw.translate(string.maketrans(','), string.punctuation)
#words = re.sub(r'\d|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.|\ +',' ',raw)
#words= re.sub(r'\d|\n|\t|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.','',raw)
words = re.sub(' +|\[A-Z]|\[a-z]+|\n|\r|\d|\n|\t|\[|\]|\።|\”|\‼|\፦|\፣|\፤|\"‼|\,|\…|\(|\‹|\›|\“|\"|\#|\||\!!|\!|\?|\•|\)|\/|\-|\፡፡|\.| +', ' ',raw)

"""
for i in words:
 fw.write(i)

fw.close()
print(words)
"""

for i in range(0, len(words), 80):
    print(words[i:i + 80])
    fw.write(words[i:i + 80]+"\n")


fw.close()
#print('\n'.join(words))
#words = re.sub(r'\d|\n|\t|\።|\፣|\,|\(|\)|\/|\-|\፡፡|\.',' +', ' ',raw)
print("----------------------------------------")
#print(string.punctuation)
#print(words[:100])
#
#print(result1)

#for word in words:
 #   print (word)



"""
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
"""
