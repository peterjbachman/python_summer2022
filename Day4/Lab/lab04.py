# Go to https://polisci.wustl.edu/people/88/all
#   OR https://polisci.wustl.edu/people/list/88/all
# Go to the page for each of the professors.
# Create a .csv file with the following information for each professor:
# - Specialization
# Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
#   Professor Aksoy’s research is motivated by an interest in
#   comparative political institutions and political violence.
# - Name
# - Title
# - E-mail
# - Web page

from random import uniform
from bs4 import BeautifulSoup
import urllib.request
import csv
import time

webAddress = 'https://polisci.wustl.edu/people/88/all'

# Steps:
# 1. Get list of all professors
# 2. Get specialization, Name, Title, E-mail, and Web Page from each professor
# 3. Save it all as a .csv

# STEP 1.
webPage = urllib.request.urlopen(webAddress)
soup = BeautifulSoup(webPage.read())

# Professors are in range 19 - 43
# soup.find_all("a")[21]

url = "https://polisci.wustl.edu"

with open('profWUSTL.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=("name",
                                      "title",
                                      "specialization",
                                      "email",
                                      "website"))
    w.writeheader()

    # STEP 2
    for i in range(19, 43):
        professor = {}
        try:
            # Get url
            time.sleep(uniform(2, 5))
            professor["website"] = url + soup.find_all("a")[i].attrs["href"]

            # Access new url
            profPage = urllib.request.urlopen(professor["website"])
            profSoup = BeautifulSoup(profPage.read())

            # Get Name
            professor["name"] = profSoup.find("h1").text

            # Get Title
            if professor['name'] in ['Randall Calvert', 'James L. Gibson']:
                professor["title"] = profSoup.find("div",
                                                   {'class': 'award'}).text
            else:
                professor["title"] = profSoup.find("div",
                                                   {'class': 'title'}).text

            # Get Specialization
            professor["specialization"] = profSoup.find("div",
                                                        {'class': 'post-excerpt'}).text

            # Get email
            if professor['name'] == "Lucia Motolinia":
                professor["email"] = "NA"
            else:
                professor["email"] = profSoup.find('ul',
                                                  {'class': 'detail contact'}).find("a").text

        except AttributeError:
            professor["website"] = 'NA'
            professor["name"] = 'NA'
            professor["title"] = 'NA'
            professor["specialization"] = 'NA'
            professor["email"] = 'NA'

        # STEP 3
        w.writerow(professor)
