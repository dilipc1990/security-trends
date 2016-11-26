from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus.reader import PlaintextCorpusReader,CategorizedPlaintextCorpusReader
from nltk.corpus import movie_reviews
import nltk
import random
from BeautifulSoup import BeautifulSoup

p = nltk.data.find('corpora/SecurityThreat-MaxEnt')
reader = CategorizedPlaintextCorpusReader(p,r'.*\.txt', cat_pattern=r'(\w+)/*')
from nltk import WordNetLemmatizer


#Using Wordnet Lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
all_words = nltk.FreqDist(word for word in reader.words())
top_words = list(all_words)[:100]
print(top_words)
def word_feats(words):
    return {word:True for word in words if word in top_words}


#def word_feats(words):
    #return dict([(wordnet_lemmatizer.lemmatize(word), True) for word in words])

# Generate all the files based on ThreatType.
IdentityThreat = reader.fileids('IdentityThreat')
InsiderThreat = reader.fileids('InsiderThreat')
Malware=reader.fileids('Malware')

# Identify the words in the datasets as based on ThreatType.
IdentityThreatfeats = [(word_feats(reader.words(fileids=[f])), 'IdentityThreat') for f in IdentityThreat]
InsiderThreatfeats = [(word_feats(reader.words(fileids=[f])), 'InsiderThreat')  for f in InsiderThreat]
Malwarefeats = [(word_feats(reader.words(fileids=[f])), 'Malware')  for f in Malware]
#print (IdentityThreatfeats)
IDcutoff = len(IdentityThreatfeats)
ITcutoff = len(InsiderThreatfeats)
Malcutoff=len(Malwarefeats)
print(IDcutoff,ITcutoff,Malcutoff)
# Based on the cut off, fill the training data and testing data with its respective  ThreatType.
trainfeats = IdentityThreatfeats[:4] + InsiderThreatfeats[:2] + Malwarefeats[:1]
testfeats = IdentityThreatfeats[4:] + InsiderThreatfeats[2:] + Malwarefeats[1:]
print( 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))

# Executing Maximum Entropy Classifier to classify the training data.
classifier = nltk.classify.MaxentClassifier.train(trainfeats)
print(classifier.classify(word_feats('Malware is been detected')))

inputpath = nltk.data.find('corpora/abc/threatdescp.txt')
f = open(inputpath, encoding='latin2')
outputpath=nltk.data.find('corpora/abc/ResultMaxEnt.txt')
ResultFile = open(outputpath, 'w',encoding='latin2')
for  line  in f:
 line=BeautifulSoup(line.strip()).text
 Threattype=classifier.classify(word_feats(line))
 finalText=line +'|'+Threattype
 #print(finalText)
 #Writing to output file
 ResultFile.writelines(finalText)
 ResultFile.writelines("\n")
