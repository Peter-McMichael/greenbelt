from bs4 import BeautifulSoup # html parser
from math import sqrt
import matplotlib.pyplot as plt # graphing
import requests # checks permission
import csv # dataset
from typing import Tuple

url = "data.html"

def genMean(items):
    sumValues = 0
    size =len(items)

    for i in range(size):
        sumValues+=items[i]
    mean = sumValues/size
    return mean

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

        

try: 

    # make genMean here.

    with open(url, 'r', encoding='utf-8') as file:
        html_source = file.read()

    # response = requests.get(html_source)
    soup = BeautifulSoup(html_source, "html.parser")

    #mortality rate for andes and corona: tr 11, mortality rate for hanta: 
    hantavirus_table = soup.find_all("table")[0]
    rows = hantavirus_table.find_all("tr")
    hanta_mortality_per_year = []
    hanta_avg_fatality = soup.find_all("td")[19] # compare this to andes and covid
    hanta_avg_fatality2 = float(hanta_avg_fatality.get_text().strip("%"))
    print(float(hanta_avg_fatality2))
    andes_avg_fatality = soup.find_all("td")[30]
    result_andes_fatal = float(andes_avg_fatality.get_text().split("% - ", 1)[1].strip("%"))
    print(float(result_andes_fatal))
    covid_avg_fatality = soup.find_all("td")[31]
    result_covid_fatal = covid_avg_fatality.get_text().split("% - ", 1)[1].strip("%")
    result_covid_fatal2 = float(result_covid_fatal.split(" ", 1)[0].strip("%"))
    print(float(result_covid_fatal2))


    fig, ax = plt.subplots()

    labels = ['Hanta', 'Andes Hanta', 'COVID']
    values = [hanta_avg_fatality2, result_andes_fatal, result_covid_fatal2]
    colors = ['blue', 'red', 'green']

    # ax.bar(x_positions, heights, ...)
    ax.bar(labels, values, color=colors)
    ax.set_title("Comparing Hanta, Andes Hanta and COVID-19 virus fatality rates.")
    ax.set_xlabel("Name of virus")
    ax.set_ylabel("Fatality %")
    plt.show()


    # for i in rows:
    #     hanta_mortality_per_year.append(rows[i])

except:
    print("An error occured!")

