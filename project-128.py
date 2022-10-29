from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
from selenium.webdriver.common.by import By
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("C:/hm/New folder/python/web-scraping/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scraping():
    headers = ["brown dwarf", "constellation", "right ascention", "declination", "apparent magnitude", "distance", "spectral type", "mass", "radius", "discovery year"]
    data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tbody in soup.find_all("tbody"):
        tr = tbody[7].find_all("tr")
        for i,tr_tag in enumerate(tr):
            templist = []   
            if i == 0:
                templist.append(tr_tag.find_all("td")[0].contents[0])
            else:
                try:
                    templist.append(tr_tag.find_all("td").contents[0])
                except:
                    templist.append("")

        data.append(templist)
        print(data)
        with open("proj-128-scraping.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(data)
            print("file created!") 
                
                

