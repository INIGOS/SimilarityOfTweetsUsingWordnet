# -*- coding: utf-8 -*-

__author__ = "Inigo Solomon"


import pickle
import re, collections
import rake
import operator
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

### Insert Current Path
import os, sys, inspect, traceback
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from Twokenize import twokenize


from nltk.corpus import stopwords
from nltk.corpus import wordnet

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
from SpellCheck.Corrector import spellCheck

path = cmd_folder+"/models/"
stoppath = "SmartStoplist.txt"
rake_object = rake.Rake(stoppath,4,2,1)
stop = stopwords.words('english')
list1=['skin','skincare','care']
list2=[]


for line in open('new.txt','r'):
    item=line.rstrip()
    #print item
    new=item.split('|')
    tweet=new[4]
    #print tweet

class TweetsExtract(object):
    def __init__(self):


        

        self.spellCheck = spellCheck()

    #Optional Stop Words Removal
    #Amazon nlp stop word list
        self.stop  = ['a', 'across', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'been', 'being', 'but', 'by', 'can', 'could', 'did', 'do', 'does', 'each', 'for', 'from', 'had', 'has', 'have', 'in', 'into', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'of', 'on', 'or', 'that', "that's", 'thats', 'the', 'there', "there's", 'theres', 'these', 'this', 'those', 'to', 'under', 'until', 'up', 'were', 'will', 'with', 'would']
        self.stop+=[")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]

    

    def getkeys(self,tweet,list1):
        for word1 in list1:
            for word2 in tweet:
                wordFromList1=wordnet.synsets(word1)
                wordFromList2=wordnet.synsets(word2)
                if wordFromList1 and wordFromList2:
                    s=wordFromList1[0].wup_similarity(wordFromList2[0])
                    list2.append(s)

            print(max(list2))
        
        return max(list2)


        

    def process(self,text,stopwordsF = 0, stemmerF = 0, encode = 1):

    # remove URL
        line = re.sub(twokenize.Url_RE," ", text)

    # to strip of extra white spaces
        temp = line.replace("#" , " ").lower().split()
        temp = " ".join(temp)
        
    #print temp

        tempTweet = ""


        for word in twokenize.tokenize(temp):
            """
                except:
                    tempTweet = " ".join([tempTweet,word.strip().decode("iso-8859-1")])
                    """
        


    #print(tempTweet.encode("utf-8"))
        if encode == 0:
            return(tempTweet)
    #return(tempTweet.encode("utf-8"))
        return temp
extract=TweetsExtract()

ans=extract.process(tweet)
#print ans
out=[i for i in ans.split() if i not in stop]
#print out
fout=extract.getkeys(out,list1)