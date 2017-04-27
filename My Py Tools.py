#### prepare dataset 
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels


############### My Python Tools ##################


# Where by col# < dig 3.1
def wherecol(dataSet, nthCol, value):
    retDataSet = []
    nthCol = nthCol - 1
    for featVec in dataSet:
        if featVec[nthCol] == value:
            reducedFeatVec = featVec[:nthCol]     
            reducedFeatVec.extend(featVec[nthCol+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
	
# Where by row# 
print dataSet[:nrow]

# count distinct group by all other columns
def count_distinct_group_by_all(dataSet, nthCol_for_Cnt):
	classlist  = [col[nthCol_for_Cnt-1] for col in dataSet]
	classCount = {}
	for vote in classlist:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount

print count_distinct_group_by_all(dataSet, 3) [:10]  #print top 10
print count_distinct_group_by_all(dataSet, 3) [0][0] #print the top element

# count distinct group by multiple columns
import pandas as pd
df = pd.DataFrame(dataSet)
df.columns = ['col1','col2','col3']
print df
print '---------'
print df.groupby(['col2','col3']).size()
print '---------'
print df.groupby(['col2','col3']).size().max()
print '---------'
print df.groupby(['col2','col3']).size().groupby(level=1).max()
print '---------'
print df.groupby(['col3']).size()

# majority element in a list
from collections import Counter
c = Counter([1,2,3,4,3,3,2,4,5,6,1,2,3,4,5,1,2,3,4,6,5])
c.most_common() # [(3, 5), (2, 4), (4, 4), (1, 3), (5, 3), (6, 2)]
value, count = c.most_common()[0]
print value

def find_majority(k):
    myMap = {}
    maximum = ( '', 0 ) # (occurring element, occurrences)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1

        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n,myMap[n])

    return maximum