from bs4 import BeautifulSoup # html parser
from math import sqrt
import matplotlib.pyplot as plt # graphing
import requests # checks permission
import csv # dataset
from typing import Tuple

url = "data.html"

def genMean(items):
    sumValues = 0
    for item in items:
        sumValues += item
    return sumValues / len(items)




def getRange(items):
    itemRange = max(items) - min(items)
    print(f"Range: {itemRange}")
    return itemRange




def getDomain(items):
    domain = [min(items), max(items)]
    print(f"Domain: {domain}")
    return domain




def getVariance(items):
    mean = genMean(items)
    squaredDiffSum = 0


    for item in items:
        squaredDiffSum += (item - mean) ** 2


    variance = squaredDiffSum / len(items)
    print(f"Variance: {variance:.2f}")
    return variance




def getStandardDeviation(items):
    standardDeviation = sqrt(getVariance(items))
    print(f"Standard deviation: {standardDeviation:.2f}")
    return standardDeviation




def getCovariance(items1, items2):
    totalSum = 0


    if len(items1) == len(items2):
        mean1 = genMean(items1)
        mean2 = genMean(items2)


        for i in range(len(items1)):
            totalSum += (items1[i] - mean1) * (items2[i] - mean2)


        covariance = totalSum / len(items1)
        print(f"Covariance: {covariance:.2f}")
        return covariance


    print("Your lists are different sizes!")
    return None




def getCorrelation(items1, items2):
    if len(items1) == len(items2):
        covariance = getCovariance(items1, items2)
        standardDeviation1 = sqrt(getVariance(items1))
        standardDeviation2 = sqrt(getVariance(items2))
        correlation = covariance / (standardDeviation1 * standardDeviation2)


        print(f"Correlation: {correlation:.2f}")
        return correlation


    print("Your lists are different sizes!")
    return None


def cleanNumber(text): # for third tablew only
    return int(text.replace("~", "").replace(",", "").strip())

def cleanPercent(text):
    return float(text.replace("%", "").strip())

def getPercent(text):
    highPercent = text.split("-")[-1]
    highPercent = highPercent.split("%")[0]
    return float(highPercent.strip())

def getCells(row):
    return [cell.get_text(strip=True) for cell in row.find_all("td")] #regex




# make genMean here.

with open(url, 'r', encoding='utf-8') as file:
    html_source = file.read()




# response = requests.get(html_source)
soup = BeautifulSoup(html_source, "html.parser")

hantaTable = soup.find("table", id="table-hanta-yearly")
hantaYears = []
hantaCases = []
hantaDeaths = []
hantaFatalityRate = []
hanta_avg_fatality2 = 0


for row in hantaTable.find("tbody").find_all("tr"):
    cells = getCells(row)

    if "Total" in cells[0]: # find cell with keywrod "total"
        hanta_avg_fatality2 = cleanPercent(cells[3])
    else:
        hantaYears.append(int(cells[0])) # get all years
        hantaCases.append(cleanNumber(cells[1]))
        hantaDeaths.append(cleanNumber(cells[2]))
        hantaFatalityRate.append(cleanPercent(cells[3]))
hantaYears.reverse()
hantaCases.reverse()
hantaDeaths.reverse()
hantaFatalityRate.reverse()


comparisonTable = soup.find("table", id="table-comparative")
andesFatalityRates = 0
covidFatalityRates = 0

for row in comparisonTable.find("tbody").find_all("tr"):
    cells = getCells(row)

    if cells[0] == "Mortality Rate (CFR)":
        andesFatalityRates = getPercent(cells[1])
        covidFatalityRates = getPercent(cells[2])

covidTable = soup.find("table", id="table-covid-yearly")
covidYears = []
covidDeaths = []
covidHospital = []

for row in covidTable.find("tbody").find_all("tr"):
    cells = getCells(row)
    covidYears.append(int(cells[0]))
    covidDeaths.append(cleanNumber(cells[1]))
    covidHospital.append(cleanNumber(cells[2]))

covidYears.reverse()
covidDeaths.reverse()
covidHospital.reverse() # reverse to put in descending order of years.

def EDASummary():
    print("\nEDA Summary")
    print("﹌﹌﹌﹌﹌﹌﹌﹌")
    print(f"Years analyzed: {len(hantaYears+covidYears)}")
    print("Viruses compared: 3")
    print(f"Average Hanta deaths per year: {genMean(hantaDeaths):.2f}") #hantaDeaths is list, gen mean of list
    print(f"Average Hanta fatality rate: {genMean(hantaFatalityRate):.2f}%")
    print(f"Average Andes Hanta fatality rate: {andesFatalityRates}%")
    print(f"Average COVID fatality rate: {covidFatalityRates}%")
    print(f"Average COVID deaths per year: {genMean(covidDeaths):.2f}")
    print(f"Average COVID hospitaliations per year: {genMean(covidHospital):.2f}")

    print("\n Hanta Death Statistics")
    print("﹌﹌﹌﹌﹌﹌﹌﹌")
    getDomain(hantaDeaths)
    getRange(hantaDeaths)
    getStandardDeviation(hantaDeaths)

    print("\nCOVID Death and Hospitalization Relationship")
    print("﹌﹌﹌﹌﹌﹌﹌﹌")
    getCorrelation(covidDeaths, covidHospital)

    print("\n COVID Deaths Compared to Hanta Deaths")
    print("﹌﹌﹌﹌﹌﹌﹌﹌")
    for i in range(len(hantaYears)):
        ratio = covidDeaths[i] / hantaDeaths[i]
        print(f"{hantaYears[i]} COVID deaths were {ratio:.0f} times higher than Hanta deaths. ")

    
EDASummary()









fig, ax = plt.subplots()

labels = ['Hanta', 'Andes Hanta', 'COVID']
values = [hanta_avg_fatality2, andesFatalityRates, covidFatalityRates]
colors = ['blue', 'red', 'green']

# ax.bar(x_positions, heights, ...)
ax.bar(labels, values, color=colors)
ax.set_title("Comparing Hanta, Andes Hanta and COVID-19 virus fatality rates.")
ax.set_xlabel("Name of virus")
ax.set_ylabel("Fatality %")


fig, ax = plt.subplots(figsize = (8, 5))
ax.bar(hantaYears, hantaDeaths, color="firebrick")
ax.set_title("Hanta Deaths Per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Deaths")
ax.set_xticks(hantaYears)


fig, ax = plt.subplots(figsize= (8,5))
barWidth = 0.35
xPositions = list(range(len(covidYears)))
deathPositions = [position - barWidth / 2 for position in xPositions]
hospitalizationsPositions = [position + barWidth / 2 for position in xPositions]

ax.bar(deathPositions, covidDeaths, width = barWidth, label = "Deaths", color = "seagreen")
ax.bar(
    hospitalizationsPositions,
    covidHospital,
    width = barWidth,
    label = "Hospitalizations",
    color = "darkorange",
)
ax.set_title("COVID Deaths and Hospitalizations per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of people")
ax.set_xticks(xPositions)
ax.set_xticklabels(covidYears)
ax.legend()


fig, ax = plt.subplots(figsize= (8,5))
ax.bar(
    deathPositions, hantaDeaths, width = barWidth, label = "Hanta Deaths", color = "firebrick"
)

ax.bar(
    hospitalizationsPositions,
    covidDeaths,
    width=barWidth,
    label = "COVID Deaths",
    color = "seagreen",
    alpha = 0.75,
)

ax.set_title("COVID Deaths Compared to Hanta Deaths")
ax.set_xlabel("Year")
ax.set_ylabel("Deaths")
ax.set_xticks(xPositions)
ax.set_yticks(hantaYears)
ax.legend()




plt.show()