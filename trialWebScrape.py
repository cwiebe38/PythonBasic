# Cody Wiebe
# trialWebScrape.py
# Attempting to write my first web scraping program using a tutorial from:
# https://betterprogramming.pub/the-only-step-by-step-guide-youll-need-to-build-a-web-scraper-with-python-e79066bd895a
# had trouble using the method above and switched to https://www.youtube.com/watch?v=15f4JhJ8SiQ for the reading in

import requests
from requests import get
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
import numpy as np

#getting the website that I want to scrape from
url = "https://www.insidelacrosse.com/team/tufts/2021"
results = requests.get(url)
#print(results.status_code)

#getting the url data in a readable manner
soup = BeautifulSoup(results.text, "html.parser")
#print(soup)

# Finding the data table in the HTML code
tufts_table = soup.find('table', class_= "table table-striped m-b-0")
#print(tufts_table)

#Looping throug rows and then individual cells to gather desired information
for team in tufts_table.find_all('tbody') :
    rows = team.find_all('tr')
    for row in rows :
        number = row.find('td').text.strip()
        name = row.find_all('td')[1].text.strip()
        position = row.find_all('td')[2].text.strip()
        goals = row.find_all('td')[5].text.strip()
        assists = row.find_all('td')[6].text.strip()
        points = row.find_all('td')[7].text.strip()
        #print(number, name, position, points, goals, assists)


tufts_stats = pd.DataFrame({
    'Number' : number,
    'Name' : name,
    'Position' : position,
    'Points' : points,
    'Goals' : goals,
    'Assists' : assists
})

print(tufts_stats)