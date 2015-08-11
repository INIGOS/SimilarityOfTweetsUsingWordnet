# -*- coding: utf-8 -*-
import rake
import operator


stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

# 2. run on RAKE on a given text
#sample_file = open("tweet.txt", 'r')
#text = sample_file.read()

keywords = rake_object.run("antiaging face cream: excellent remedy for anti agin skin care")

# 3. print results
print "Keywords:", keywords
