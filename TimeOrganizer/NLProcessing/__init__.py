from NLProcessing.NLPClassDefault import testing
from NLProcessing.WordsFinder import testing2
from NLProcessing.SearchEngine import testing3
from Database.Initialization import createDatabase

if __name__ == "__main__":
    createDatabase(True)
    testing3()


#import nltk
#from nltk.corpus import wordnet 
#from nltk.stem.wordnet import WordNetLemmatizer #To download corpora: python -m nltk.downloader all

#####################################################
#ws1 = wordnet.synsets('run') # v here denotes the tag verb
#ws2 = wordnet.synsets('sprint')

#sim_list = []
#for w1 in ws1:
#    for w2 in ws2:
#        sim_list.append({"Accuracy":w1.wup_similarity(w2),"Words": w1.name() + " - " + w2.name()})


#sim_list = [x for x in sim_list if x["Accuracy"] is not None]
#print("\n\n")

#sim_list.sort(reverse=True, key=lambda x: x["Accuracy"])
#for x in range(10):
#    print(sim_list[x]["Words"] + ": " + str(sim_list[x]["Accuracy"]))
#print("\n\n")
##print(sim_list)
#w1 = wordnet.synset('run.v.01') # v here denotes the tag verb
#w2 = wordnet.synset('sprint.v.01')
#sim_list = [] 
#sim_list.append({"Accuracy":w1.wup_similarity(w2),"Words": w1.name() + " - " + w2.name()})

#print(w1.name() + " - " + w2.name() + ": " + str(w1.wup_similarity(w2)))
#print("\n\n")


## if it can be a verb
##def possible_verb(surface):
##    return 'v' in set(s.pos() for s in wn.synsets(surface))



## https://stackoverflow.com/questions/35462747/how-to-check-a-word-if-it-is-adjective-or-verb-using-python-nltk

##words = ['amazing', 'interesting', 'love', 'great', 'nice']
##for w in words:
##    tmp = wn.synsets(w)[0].pos()
##    print w, ":", tmp


##    Output:
##amazing : v
##interesting : v
##love : n
##great : n
##nice : n

## Pomysł
#words = ["run","important","very","meeting","exam","knowledge", "examination"]

#def sort_lamb(item):
#    if(item[1] == None):
#        return 0
#    else:
#        return item[1]

#for word in words:
#    synonyms = [] 
#    syns = wordnet.synsets(word)
#    syn_list = [] 
#    syn_list2 = [] 
#    main_word = syns[0]
#    for syn in syns:
#        for l in syn.lemmas():
#            syn_list.append(l)
#            syn_list2.append(l.name())
#    for synonim in set(syn_list):
#        synsetOfSyn = synonim.synset()
#        synonyms.append([synonim.name()+"." + synsetOfSyn.pos(),main_word.wup_similarity(synsetOfSyn)])
#    synonyms.sort(reverse = True, key = sort_lamb)
#    print("Main word: " + main_word.name())
#    for synonym in synonyms:
#        print(synonym[0] + ": " + str(synonym[1]))
#    print()
#    print(set(syn_list))
#    print()
#    print(set(syn_list2))
#    print("\n------------------------------------------------------------------------\n")
#    #for syn in syns:
#    #    if(word in syn.name()):
#    #        main_word = syn
#    #        break
#    #for syn in syns:
#    #    add = True
#    #    if (len(synonyms) == 0):
#    #        synonyms.append([syn.lemmas()[0].name(),main_word.wup_similarity(syn)])
#    #    for s in synonyms:
#    #        tocheck = syn.name().split(".")[0]
#    #        if(tocheck == s[0].split(".")[0]):
#    #             add = False
#    #    if(add):
#    #        synonyms.append([syn.lemmas()[0].name(),main_word.wup_similarity(syn)])

## Opis: Doctor appointment. Very importnant , don't miss it!
## Opis1: Bartek birthday. Important, get a gift!
## Opis2: Final exam, get some crucial knowledge!

## search query: crucial
## Kolejność:
## Opis2
## Opis
## Opis1

## search query: crucial gift
## Kolejność:
## Opis1