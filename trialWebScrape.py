# Cody Wiebe
# trialWebScrape.py
# Attempting to write my first web scraping program using a tutorial from:
# https://betterprogramming.pub/the-only-step-by-step-guide-youll-need-to-build-a-web-scraper-with-python-e79066bd895a

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#getting the website that I want to scrape from
url = "https://stats.premierlacrosseleague.com/player-table"
results = requests.get(url)

#getting the url data in a readable manner
soup = BeautifulSoup(results.text, "html.parser")

#Initializing my storage
names = []
gp = []
goals = []
points = []
assists = []
turnovers = []
gb = []

#getting each line of the player data
player_stats = soup.find_all('tr', class_='MuiTableRow-root')


#iterating through every line of player stats gathered
for container in player_stats :

    name = container.find('td', class_='MuiTableCell-root MuiTableCell-body jss58 MuiTable Cell-alignLeft')
    names.append(name)

print(names)
