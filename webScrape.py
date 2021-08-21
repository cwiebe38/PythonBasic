import requests
from requests import get
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
import numpy as np

url = "https://www.insidelacrosse.com/team/duke/2021"
results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

duke_table = soup.find('table', "table table-striped m-b-0")

number = []
name = []
year = []
points = []

team = duke_table.find('tbody')
rows = team.find_all('tr')

for row in rows:
    columns = row.find_all('td')
    number.append(columns[0].text.strip())
    name.append(columns[1].text.strip())
    year.append(columns[3].text.strip())
    points.append(columns[7].text.strip())

duke_data = pd.DataFrame({
    'Number' : number,
    'Name' : name,
    'Year' : year,
    'Points' : points
})
print(duke_data)
