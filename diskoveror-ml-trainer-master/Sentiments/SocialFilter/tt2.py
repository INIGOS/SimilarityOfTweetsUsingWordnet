import rake
import operator

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

rake_object = rake.Rake(stoppath)

for line in open('twittersearchconnector.dat','r'):
	item=line.rstrip()
	#print item
	new=item.split('|')
	ans=new[4]
	#print ans
	#print "-------------"
	text=ans
	sentenceList = rake.split_sentences(text)

	stopwordpattern = rake.build_stop_word_regex(stoppath)
	phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
	print "Phrases:", phraseList