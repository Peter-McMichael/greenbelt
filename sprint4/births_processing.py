
import csv

def load_data(filename):
    births_list = []

    with open(filename, mode = "r", newline = "") as file:
        reader = csv.DictReader(file)

        for row in reader:
            births_list.append(int(row["births"]))
    births_list = sorted(births_list)
    return births_list


# def makeList():
#     list = []
#     for i in range (40):
#         list.append(random.randint(1, 30))
#     births_list = sorted(list)
#     print(births_list)
#     return births_list


def mean(births_list):
    x=0
    for i in births_list:
        x = i+x
    mean = x/len(births_list)
    print(f"Mean: {mean}")


def median(births_list):
    right = len(births_list) 
    middle = right//2
    if len(births_list) % 2 == 0:
        median = (births_list[middle - 1] + births_list[middle])/2
    else:
        median = births_list[middle]
    print(f"Median: {median}")

def mode(births_list):
    dict = {}
    for i in births_list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
   
    max_values = max(dict.values())
    all_max_keys = [k for k, v in dict.items() if v == max_values]
    print(f"Modes: {all_max_keys}")
    return dict


births_data = load_data("/Users/homefolder/Desktop/Python/Green Belt/sprint4/births.csv")

# y = makeList()
mean(births_data)
median(births_data)
mode(births_data)
        
