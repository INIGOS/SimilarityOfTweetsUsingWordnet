# -*- coding: utf-8 -*-
import rake
import operator


stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

# 2. run on RAKE on a given text
#sample_file = open("ans.txt", 'r')
#text = sample_file.read()
ans=antiaging face cream: excellent remedy for anti agin skin care
f = open('ans','w')
f.write(ans) # python will convert \n to os.linesep
f.close()

#keywords = rake_object.run(text)

# 3. print results
#print "Keywords:", keywords