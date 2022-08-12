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