import nltk
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
import random
from BeautifulSoup import BeautifulSoup


#Reading from  custom created categorized corpora
#categorized corpora will be categorized for topic, genre, polarity, etc.
#In addition to the standard corpus interface, these corpora provide access to the list of categories
#and the mapping between the documents and their categories (in both directions)
# Access the categories using the categories() method

d = nltk.data.find('corpora/SecurityThreat')
reader = CategorizedPlaintextCorpusReader(d,r'.*\.txt', cat_pattern=r'(\w+)/*')
from textblob.classifiers import NaiveBayesClassifier
random.seed(1)
train = [
    ('Identity', 'IdentityThreat'),
    ('identity', 'IdentityThreat'),
    ('identities', 'IdentityThreat'),
    ('identity loss', 'IdentityThreat'),
    ('insider', 'InsiderThreat'),
    ('Malware', 'Malware'),
       
]

# Categorized corpora Reader collect the respective words based on ThreatType
ThreatTypes = [(list(reader.words(fileid)), category)
              for category in reader.categories()
              for fileid in reader.fileids(category)]
random.shuffle(ThreatTypes)
print(reader.categories())
new_train = ThreatTypes
print(new_train)
#Naive Bayes classifiers assume that the value of a particular feature is independent of the value of
#any other feature, given the class variable.
cl = NaiveBayesClassifier(train)
#update the classifier with training keywords from Categorized corpora
cl.update(new_train)
inputpath = nltk.data.find('corpora/abc/threatdescp.txt')
f = open(inputpath, encoding='latin2')
outputpath=nltk.data.find('corpora/abc/ResultNB.txt')
ResultFile = open(outputpath, 'w',encoding='latin2')
for  line  in f:
 line=BeautifulSoup(line.strip()).text
 Threattype=cl.classify(line)
 finalText=line +'|'+Threattype
 print(finalText) 
 ResultFile.writelines(finalText)
 ResultFile.writelines("\n")



     
