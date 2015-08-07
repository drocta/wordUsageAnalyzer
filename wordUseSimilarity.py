import re
import operator
import math

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

def countWordsInList(wordsInList,wordCounts={}):
    #wordCounts={}
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



roseExampleIn="""Act 1
_
1. JE1: =001963
I understand you have recently come into possession of the beta release of "The Game of the Year", as featured in respectable periodicals such as GameBro Magazine.
I can't control myself.
I must have a weakness for insufferable pricks.
John.
You're wearing one of your disguises now, aren't you?
You are typing to me right now while wearing something ridiculous.
Ok.
Why don't you go get the game from your father?
I know, John.
_
2. JE2: =002035
It looks like you managed to retrieve the beta. Excellent.
I'm going to try to connect.
The rabbit?
I've heard tales of this wretched creature often. Its Homeric legend is practically ensconced in the fold of my personal mythology by now.
Why don't we focus on the matter at hand?
You are running the client application. I am running the server, so I am the host user. I have established a connection with you. This is sufficient for us to play the game.
Why don't we get started?
_
3. JE3: =002041
Sorry. I'm just getting a feel for the controls.
Yes.
I will try to be more careful next time.
_
4. JE4: =002044
I'll give it a shot."""

def processText(inText):
    aaaaa=getWordsOnly(inText).split(' ')
    aaaaa=countWordsInList(aaaaa)
    displayWordFrequencies(aaaaa)

asdf="bob"

def countWordsInFile(filepath):
    wordCounts={}
    i=0
    global asdf
    content_file = open(filepath, 'r')
    for line in content_file:
        wordsOnly=getWordsOnly(line)
        wordCounts=countWordsInList(getWordsOnly(line).split(' '),wordCounts)
        i+=1
    content_file.close()
        #content = content_file.read()
    #aaaaa=getWordsOnly(content).split(' ')
    return wordCounts

def wordCountsDotProduct(wordCounts_A,wordCounts_B):
    total=0
    for word in wordCounts_A:
        if(word in wordCounts_B):
            total+=wordCounts_A[word]*wordCounts_B[word]
    return total


charsFiles={
'john':r"C:\Users\madaco\Documents\homestuckLogs\humans\Beta kids\john egbert.rtf.txt",
'rose':r"C:\Users\madaco\Documents\homestuckLogs\humans\Beta kids\rose lalonde.rtf.txt",
'jade':r"C:\Users\madaco\Documents\homestuckLogs\humans\Beta kids\jade harley.rtf.txt",
'dave':r"C:\Users\madaco\Documents\homestuckLogs\humans\Beta kids\dave strider.rtf.txt"
    }

charsWordCounts={}
charsMagnitudes={}

def countWordsInEachFile():
    for char in charsFiles:
        charsWordCounts[char]=countWordsInFile(charsFiles[char])
        charsMagnitudes[char]=math.sqrt(wordCountsDotProduct(charsWordCounts[char],charsWordCounts[char]))

def similarity(char_A,char_B):
    return wordCountsDotProduct(charsWordCounts[char_A],charsWordCounts[char_B])/(
        charsMagnitudes[char_A]*charsMagnitudes[char_B])

