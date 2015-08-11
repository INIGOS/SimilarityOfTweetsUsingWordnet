import rake
import operator

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

rake_object = rake.Rake(stoppath)

text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms new york " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of new york " \
       "systems and systems of mixed types new york."



# 1. Split text into sentences
sentenceList = rake.split_sentences(text)



stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)


wordscores = rake.calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print "Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate)

