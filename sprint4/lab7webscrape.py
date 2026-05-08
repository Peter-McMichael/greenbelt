
import requests
from bs4 import BeautifulSoup
import csv



url = "birds.html"
size = []
color = []
name = []


try: 

    with open(url, 'r', encoding='utf-8') as file:
        html_source = file.read()

    # response = requests.get(html_source)
    soup = BeautifulSoup(html_source, "html.parser")

    findTitle = soup.find('title')
    robin = soup.find('h2', class_= "bird-name").text.strip() #finding specific classes 
    # .text.strip() removes tag and makes it so that only name appears

    birdNames = soup.find_all('h2', class_="bird-name")
    names = []
    for i in birdNames:
        x = i.text.strip()
        names.append(x)
        #list of all birds on document.


    response = requests.get("https://google.com") # 200 means request is successful, 404 means reuqest is unsuccessful, 500 means there was a server error.

    birds = soup.find_all("article", class_="bird-card")
    print(birds)

    with open("collected_data.csv", 'w', newline = "") as file:
        fieldnames = ['Name', "Color", "Size"]
        writer = csv.DictWriter(file, fieldnames=fieldnames) #write rows
        # writer.writerow(["Name", "Color", "Size"])
        # writer.writerows(name)
        writer.writeheader()

        for i in birds:
            b_color = i.find('ul', class_="color1-list").find_all("li")
            b_name = i.find('h2', class_="bird-name").text
            b_size = i.find('ul', class_="size-list").find_all("li")

            b_color = [color.text.strip() for color in b_color]
            b_color = ", ".join(b_color)

            b_size = [size.text.strip() for size in b_size]
            b_size = ", ".join(b_size)


            writer.writerow({"Name": b_name, "Color": b_color, "Size": b_size })

      

        
    
    print(birds)
    # print(response)
    # print(names)    
    # print(findTitle)
    # print(birdNames)

except requests.exceptions.RequestException as e:
    print(f"An error occured! ({e})")



