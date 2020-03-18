#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
import re

banner_text = '''

 ██████╗ ██████╗ ██╗   ██╗██╗██████╗        ██╗ █████╗     ██╗     ██╗██╗   ██╗███████╗    ███████╗████████╗ █████╗ ████████╗██╗ ██████╗███████╗
██╔════╝██╔═══██╗██║   ██║██║██╔══██╗      ███║██╔══██╗    ██║     ██║██║   ██║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝
██║     ██║   ██║██║   ██║██║██║  ██║█████╗╚██║╚██████║    ██║     ██║██║   ██║█████╗      ███████╗   ██║   ███████║   ██║   ██║██║     ███████╗
██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║╚════╝ ██║ ╚═══██║    ██║     ██║╚██╗ ██╔╝██╔══╝      ╚════██║   ██║   ██╔══██║   ██║   ██║██║     ╚════██║
╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       ██║ █████╔╝    ███████╗██║ ╚████╔╝ ███████╗    ███████║   ██║   ██║  ██║   ██║   ██║╚██████╗███████║
 ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        ╚═╝ ╚════╝     ╚══════╝╚═╝  ╚═══╝  ╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝                                                                                                                                                

 Script Written By r00tk1ll3r

 DISCLAIMER:

    ALL OF THESE STATICS FROM https://www.corona.help 
    AND THANKS TO Alex Dumitru WHO BUILT ABOVE MENTIONED WEB SITE

 To See Useage just execute ./COVID19.py

'''
print(banner_text)
coronaPage = requests.get("https://corona.help")
pageContent = BeautifulSoup(coronaPage.content,'html.parser')
if(len(sys.argv) == 2):
    j = 0
    statics = pageContent.find_all(class_="col-xl-2 col-md-4 col-sm-6")
    if("totalInfected" in str(sys.argv)):
        for i in statics:
            totalInfected = i.find(class_="mb-0 line-ellipsis").get_text()
            if(totalInfected == "Total people infected"):
                value = statics[j].find(class_="text-bold-700").get_text()
                print(totalInfected + " " +value)
            j=j+1
    elif("totalDeath" in str(sys.argv)):
        for i in statics:
            totalDeath = i.find(class_="mb-0 line-ellipsis").get_text()
            if(totalDeath == "Total deaths"):
                value = statics[j].find(class_="text-bold-700").get_text()
                print(totalDeath + " " + value)
            j=j+1
    elif("totalRecovered" in str(sys.argv)):
        for i in statics:
            totalRecovered = i.find(class_="mb-0 line-ellipsis").get_text()
            if(totalRecovered == "Total people recovered"):
                value = statics[j].find(class_="text-bold-700").get_text()
                print(totalRecovered + " " + value)
            j=j+1
    elif("todayInfected" in str(sys.argv)):
        for i in statics:
            todayInfected = i.find(class_="mb-0 line-ellipsis").get_text()
            if(todayInfected == "People infected today"):
                value = statics[j].find(class_="text-bold-700").get_text()
                print(todayInfected+ " " + value)
            j=j+1
    elif("todayDeath" in str(sys.argv)):
        for i in statics:
            todayDeath = i.find(class_="mb-0 line-ellipsis").get_text()
            if(todayDeath== "Deaths today"):
                value = statics[j].find(class_="text-bold-700").get_text()
                print(todayDeath + " " + value)
            j=j+1
    elif("todayRecovered" in str(sys.argv)):
        for i in statics:
            todayRecovered = i.find(class_="mb-0 line-ellipsis").get_text()
            if(todayRecovered == "People recovered today"):
                value = statics[j].find(class_="text-bold-700").get_text()
                print(todayRecovered + " " + value)
            j=j+1
elif(len(sys.argv) == 3):
    k=0
    if("COUNTRY" in str(sys.argv)):
        countryStatics = pageContent.find(class_="table table-hover-animation mb-0")
        tr = countryStatics.find_all("tr")
        for j in tr:
            div = j.find("div")
            if div is not None:
                if(re.sub('W+',' ', div.get_text() ).lower()==str(sys.argv[2])):
                    country = "| " +div.get_text() + " | "
                    infected = tr[k].find(class_="text-warning").get_text() + " | "
                    deaths = tr[k].find(class_="text-danger").get_text() + " | "
                    recovered = tr[k].find(class_="text-success").get_text() + " | "
                    active = tr[k].find_all("td")
                    active = active[4].get_text() + " | "
                    static = pd.DataFrame({
                        "| Country | ":[country],
                        "Infected | ":[infected],
                        "Deaths | ":[deaths],
                        "Recovered | ":[recovered],
                        "Active | ":[active]
                    })
                    print(static)
            k=k+1
else:
    useage = '''
USEAGE
------

TO GET TOTAL NUMBER OF PEOPLE WHO INFECTED BY COVID-19 : ./COVID19.py totalInfected

TO GET TOTAL NUMBER DEATH BY COVID-19 : ./COVID19.py totalDeath

TO GET TOTAL NUMBER OF PEOPLE WHO RECOVERED FROM COVID-19 : ./COVID19.py totalRecovered

TO GET TOTAL NUMBER OF PEOPLE WHO INFECTED TODAY : ./COVID19.py todayInfected

TO GET TOTAL NUMBER OF DEATH TODAY : ./COVID19.py todayDeath

TO GET TOTAL NUMBER OF RECOVERED PEOPLE IN TODAY : ./COVID19.py todayRecovered

TO GET SPECIFIC COUNTRY'S STATICS : ./COVID19.py COUNTRY COUNTRY-NAME

IF YOU WANT TO GET CHINA'S STATICS : ./COVID19.py COUNTRY "mainland china"
    '''
    print(useage)