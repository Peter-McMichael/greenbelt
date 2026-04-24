import random
from math import sqrt
from typing import Tuple

# Random Data
def makeList(size, scope: Tuple[int, int]):
    items = []
    for i in range(size):
        items.append(random.randint(scope[0], scope[1]))
    print(items)
    return items

#range
def getRange(items):
    items.sort()
    range = max(items) - min(items)
    print(f"Range: {range}")
    return range

#domain
def getDomain(items):
    items.sort()
    domain = [min(items), max(items)]
    print(f"Domain: {domain}")
    return domain

#variance
def getVariance(items):
    x=0
    squaredDiffSum = 0
    for i in items:
        x = i+x
    mean = x/len(items)
    squaredDiff = []
    for i in items:
        squaredDiff.append((i - mean)**2)
    for i in squaredDiff:
        squaredDiffSum = i + squaredDiffSum
    global variance
    variance = squaredDiffSum/len(items)
    print(f"Variance: {variance}")
    return variance

#standard deviation
def getStandardDeviation(items):
    standardDeviation = sqrt(variance)
    print(f"Standard deviation: {standardDeviation}")
    return standardDeviation

#covariance
def getCovariance(items1, items2):
    #if lists are equal length
    totalSum = 0
    if len(items1) == len(items2):
        x = 0
        for i in items1:
            x = i+x
        mean1 = x/len(items1)
       

        y=0
        for i in items2:
            y = i+y
        mean2 = y/len(items2)

        for i in range(len(items1)):
            totalSum += (items1[i] - mean1) * (items2[i] - mean2)
        global covariance
        covariance = totalSum/len(items1)
        print(f"Covariance: {covariance}")
        return covariance
    else:
        print("Your lists are different sizes!")
        return None
    
# correlation
def getCorrelation(items1, items2):
    if len(items1) == len(items2):
        cov = getCovariance(items1, items2)
        
        stdDeviation1 = getStandardDeviation(getVariance(items1))
        stdDeviation2 = getStandardDeviation(getVariance(items2))

        correlation = cov/(stdDeviation1*stdDeviation2)
        
        print(f"Correlation: {correlation}")
    else:
        print("Your lists are different sizes!")
        return None



   

myList1 = makeList(10, [1, 10])
myList2 = makeList(10, [1, 10])

getRange(myList1)
getDomain(myList1)
getVariance(myList1)
getStandardDeviation(getVariance(myList1))
getCovariance(myList1, myList2)
getCorrelation(myList1, myList2)