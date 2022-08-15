import re
import os
# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
    obama = f.readlines()
os.chdir('/Users/peter/Code/python_summer2022/Day5/Lab')

# TODO: print lines that do not contain 'the' using what we learned
# (although you ~might~ think you could do something like
# [l for l in obama if "the" not in l]
print(obama)
obama = ''.join(obama)
re.findall(r"^(?!.*\bthe\b).*", obama, re.MULTILINE)

# TODO: print lines that contain a word of any length starting with s and
#       ending with e
re.findall(r"^.*\ss\w*e\s.*", obama, re.MULTILINE)

# TODO: Print the date input in the following format
# Month: MM
# Day: DD
# Year: YY
date = 'Please enter a date in the following format: 08.18.21'

dict = re.search(r"(?P<Month>\d{2})\.(?P<Day>\d{2})\.(?P<Year>\d{2})", date)
dict = dict.groupdict()

text = "Month: " + str(dict["Month"]) + "\nDay: " + \
    str(dict["Day"]) + "\nYear: " + str(dict["Year"])
print(text)
