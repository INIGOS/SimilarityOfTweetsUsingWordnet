import rake
import operator

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = open("data/docs/fao_test/w2167e.txt", 'r')
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print "Keywords:", keywords
