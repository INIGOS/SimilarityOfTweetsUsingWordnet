# -*- coding: utf-8 -*-
__author__ = "Inigo Solomon"
import pickle
import re, collections
import rake
import operator
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
list1=['skin','skincare','care','business','intelligence']
list2=[0.0]

class TweetsExtract(object):
    def __init__(self):

        self.spellCheck = spellCheck()

    #Optional Stop Words Removal
    #Amazon nlp stop word list
        self.stop  = ['a', 'across', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'been', 'being', 'but', 'by', 'can', 'could', 'did', 'do', 'does', 'each', 'for', 'from', 'had', 'has', 'have', 'in', 'into', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'of', 'on', 'or', 'that', "that's", 'thats', 'the', 'there', "there's", 'theres', 'these', 'this', 'those', 'to', 'under', 'until', 'up', 'were', 'will', 'with', 'would']
        self.stop+=[")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]

    def process(self,stopwordsF = 0, stemmerF = 0, encode = 1):


        f=open('twitter.csv','r')
        for line in iter(f):
            item=line.rstrip()
            #new=item.split('|')
            #tweet=new[4]
            #print tweet
            #print "_____"
    # remove URL
            line = re.sub(twokenize.Url_RE," ", item)

    # to strip of extra white spaces
            temp = line.replace("#" , " ").lower().split()
            temp = " ".join(temp)
            print "TWEET:"
            print temp
            out=[i for i in temp.split() if i not in stop]
            

            for word1 in list1:
                for word2 in out:
                    wordFromList1=wordnet.synsets(word1)
                    wordFromList2=wordnet.synsets(word2)
                    if wordFromList1 and wordFromList2:
                        s=wordFromList1[0].wup_similarity(wordFromList2[0])
                        list2.append(s)
                    #print list2
                print word1
                #print list2
                if list2:
                    print(max(list2))
                else:
                    print '0.0'
                del list2[:]

        #getkeys(out,list1)
        
    #print tweet

        #tempTweet = ""



        #for word in twokenize.tokenize(temp):
            """
                except:
                    tempTweet = " ".join([tempTweet,word.strip().decode("iso-8859-1")])
                    """
        

        

    #print(tempTweet.encode("utf-8"))
        #if encode == 0:
            #return(tempTweet)
    #return(tempTweet.encode("utf-8"))
        return(max(list2))


extract=TweetsExtract()
ans=extract.process()