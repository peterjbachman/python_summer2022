# Each Spoken Address by President Biden since 01/20/2021
# Following Information:
# - Date of Spoken Address
# - Title
# - Full Text
# - Citation/Footnote if it exists
# Make this a .csv file
# Make sure to be polite

from bs4 import BeautifulSoup
from random import uniform
import urllib.request
import csv
import time

# Steps
# Start with the writing a .csv file
# Load the main page
# For each Address:
# - Check if date is Jan 19, 2021
# - If it is, stop the script.
# - If not, load the new page
# - Grab the date, title, full text, and citation
# - Write the .csv file

# https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks
# https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?page=1

with open('bidenAddress.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=("date", 'title', 'text', 'footnote'))
    w.writeheader()

    j = 0
    biden = True
    # Doing this one so the outer link doesn't have to loop so many times
    baseLink = "https://www.presidency.ucsb.edu/documents/app-categories/" + \
        "presidential/spoken-addresses-and-remarks?items_per_page=60"
    # Append the link with the page number
    while biden:
        if j == 0:
            page = baseLink
        else:
            page = baseLink + "&page=" + str(j)
        print("Page " + str(j))
        page = urllib.request.urlopen(page)
        soup = BeautifulSoup(page.read())
        # For loop for each individual page
        for i in range(0, 60):
            remark = {}
            # Get title, link, and date from base page
            pageLinks = soup.find_all("div",
                                      {"class": "field-title"})[i]
            remark["title"] = pageLinks.find("a").text
            remark["date"] = soup.find_all("h4")[i].text
            link = "https://www.presidency.ucsb.edu" + \
                pageLinks.find("a")["href"]
            # If the title is the one after Biden's inagural address, end the
            # loops.
            if remark["title"] == "Remarks at a Departure Ceremony at " + \
                    "Joint Base Andrews, Maryland":
                biden = False
                break
            # Load in the individual page
            remarkPage = urllib.request.urlopen(link)
            remarkPage = BeautifulSoup(remarkPage.read())

            # Get text and footnote
            try:
                remark["text"] = remarkPage.find(
                    "div", {"class": "field-docs-content"}).text
            except AttributeError:
                remark["text"] = "NA"
            # field-docs-footnote p
            try:
                remark["footnote"] = remarkPage.find(
                    "div", {"class": "field-docs-footnote"}).text
            except AttributeError:
                remark["footnote"] = "NA"

            # Write the row to the .csv
            print("Writing %s to the .csv" % remark["title"])
            print("Number: %i" % i)
            w.writerow(remark)
            # Sleep at the end to prevent issues with scraping
            time.sleep(uniform(2, 5))
        j += 1
        time.sleep(uniform(2, 5))


# # Trying to figure out how to capture these sites
# print(soup.prettify())

# soup.find_all("div", {"class": "field-title"})[9].find("a")["href"]

# # Link
# titles[9].find("a")["href"]

# # Title
# titles[9].find("a").text

# # Date
# soup.find_all("h4")[9].text
