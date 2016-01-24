# -*- coding: utf-8 -*-

# Python script for analyzing word frequency and density in a text

# Copyright (C) 2016 Kris P. Shaffer

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import codecs
import csv


def stripPunc(sourceFile):
    punctuation = [ u".", u",", u":", u";", u"?", u"!", u"'", u"’", u'"', u"-", u"–", u"—" ]
    content = [line.rstrip('\n') for line in codecs.open(sourceFile, encoding='utf-8')]
    strippedText = []
    for line in content:
        strippedLine = ''
        for letter in line:
            if letter not in punctuation:
                strippedLine += letter
        strippedText.append(strippedLine)
    
    return strippedText


def wordify(textAsList):
    wordifiedText = []
    for line in textAsList:
        wordList = line.split()
        for word in wordList:
            wordifiedText.append(word.lower())
    return wordifiedText


def analyzeWord(word, wordPosition):
    wordInfo = []

    wordInfo.append(wordPosition)

    wordInfo.append(word)
    
    if word in wordCount.keys():
        wordCount[word] += 1
    else:
        wordCount[word] = 1
    wordInfo.append(wordCount[word])

    wordInfo.append(float(wordCount[word])/float(wordPosition))
    
    if word in previousOccurrence.keys():
        wordInfo.append(previousOccurrence[word])
        wordInfo.append(wordPosition-previousOccurrence[word])
    else:
        wordInfo.append(None)
        wordInfo.append(None)
    previousOccurrence[word] = wordPosition

    return wordInfo

def analyzeWholeText(wordifiedText):
    textAnalysis = []
    wordPosition = 1
    for word in wordifiedText:
        textAnalysis.append(analyzeWord(word, wordPosition))
        wordPosition += 1
    return textAnalysis


def writeWordifyToFile(wordifiedText, filename):
    f = codecs.open(filename, mode='w', encoding='utf-8')
    for line in wordifiedText:
        f.write(line + '\n')
    f.close()
    print filename, 'successfully created.'


def writeToCSV(dataToWrite, outputFileName):
    with open(outputFileName, 'wb') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['position','word','tallySoFar','probSoFar','previousOccurrence','distanceSincePrevious','\n'])
        for row in dataToWrite:
            w.writerow(row)
    print outputFileName, 'successfully created.'

    
# run


wordCount = {}
previousOccurrence = {}

sourceFile = 'peterRabbit.txt'
outputWordifiedFile = 'peterRabbitWordified.txt'
outputAnalysisFile = 'peterRabbitAnalysis.csv'
writeWordifyToFile(wordify(stripPunc(sourceFile)), outputWordifiedFile)
writeToCSV(analyzeWholeText(wordify(stripPunc(sourceFile))), outputAnalysisFile)
