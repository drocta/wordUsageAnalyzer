import re
import operator
import math
import itertools

removeApostr=re.compile(r"'")#to remove apostrophes.
removeDigits=re.compile(r"[0-9]")#to remove digits
removeNonAlpha=re.compile(r"[^\w]")#to remove digits
removeNull=re.compile(r"\x00")


def getWordsOnly(inStr):
    inProgress=inStr
    inProgress=removeApostr.sub('',inProgress)
    inProgress=removeNull.sub('',inProgress)
    inProgress=removeDigits.sub('',inProgress)
    inProgress=removeNonAlpha.sub(' ',inProgress)
    inProgress=re.sub('\s{2,}', ' ', inProgress)
    inProgress=inProgress.lower()
    return inProgress

def countWordsInList(wordsInList,wordCounts=None):
    if(wordCounts == None):
    	wordCounts = {}
    for a in wordsInList:
        if a not in wordCounts:
            wordCounts[a]=1
        else:
            wordCounts[a]+=1
    return wordCounts

def displayWordFrequencies(wordCounts):
    sorted_wordCounts = sorted(wordCounts.items(), key=operator.itemgetter(1), reverse=True)
    for wordEntry in sorted_wordCounts[3:100]:
        if(wordEntry[1]>1):
            print(wordEntry)

			
def processText(inText):
    wordList = getWordsOnly(inText).split(' ')
    wordCount = countWordsInList(wordList)
    displayWordFrequencies(wordCount)


def countWordsInFile(filepath):
    wordCounts={}
    content_file = open(filepath, 'r')
    for line in content_file:
        wordsOnly=getWordsOnly(line)
        wordCounts=countWordsInList(getWordsOnly(line).split(' '),wordCounts)
    content_file.close()
    return wordCounts

def wordCountsDotProduct(wordCounts_A,wordCounts_B):
    total=0
    for word in wordCounts_A:
        if(word in wordCounts_B):
            total+=wordCounts_A[word]*wordCounts_B[word]
    return total


charsFiles={
'john':r"./words/Humans/Beta kids/john egbert.txt",
'rose':r"./words/Humans/Beta kids/rose lalonde.txt",
'jade':r"./words/Humans/Beta kids/jade harley.txt",
'dave':r"./words/Humans/Beta kids/dave strider.txt",
'jane':r"./words/Humans/alpha kids/jane crocker.txt",
'jake':r"./words/Humans/alpha kids/jake english.txt",
'roxy':r"./words/Humans/alpha kids/roxy lalonde.txt",
'dirk':r"./words/Humans/alpha kids/dirk strider.txt",
'karkat':r"./words/trolls/Alternia trolls/karkat vantas.txt",
'kanaya':r"./words/trolls/Alternia trolls/kanaya maryam.txt",
'gamzee':r"./words/trolls/Alternia trolls/gamzee makara.txt"
    }

charsWordCounts={}
charsMagnitudes={}

commonWords = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some', 'could','them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', '', '_']

def countWordsInEachFile(usageTreshold):
    for char in charsFiles:
        charsWordCounts[char] = (#filter for only words that happen more than once
			{k:v for (k,v) in countWordsInFile(charsFiles[char]).items() if v > usageTreshold and k not in commonWords})
        charsMagnitudes[char]=math.sqrt(wordCountsDotProduct(charsWordCounts[char],charsWordCounts[char]))

def similarity(char_A,char_B):
    return wordCountsDotProduct(charsWordCounts[char_A],charsWordCounts[char_B])/(
        charsMagnitudes[char_A]*charsMagnitudes[char_B])


def allValuesOf(names):
	for a,b in itertools.combinations(names,2):
		yield a,b,similarity(a,b)
