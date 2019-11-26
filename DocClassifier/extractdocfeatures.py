# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:28:24 2019

@author: halterman
"""
def getcontext(wordlist,position):
    if (position < 4) and (position <(len(wordlist)-6)):
       context = wordlist[:position] + wordlist[position:position+6]
       #context = 'first'
    elif position>4 and position>(len(wordlist)-6):
        context = wordlist[position-4:position]+wordlist[position:len(wordlist)-1]
        #context = 'second'
    elif position>=4 and position<=(len(wordlist)-5):
        context = wordlist[position-4:position]+wordlist[position:position+6]
    else:
        context = wordlist[:]
        #context = 'third'
    return context


def extractwordcontext(wordlist):
    length = len(wordlist)
    wordfeatures={'word':'',
                 'previous_word':'',
                 'context':[]}
    for word in range(length):
        wordfeatures['context'] = getcontext(wordlist,word)
        wordfeatures['word'] = wordlist[word]
        wordfeatures['previousword'] =wordlist[word-1]
    return wordfeatures




    