#!/usr/bin/env python

#
# Output:
# 1.) An XML document in the following form:
#
#  <xml>
#      <country name="Afghanistan" code="AF">
#          <sub name="Balkh" code="AF-BAL"/>
#          <sub name="Bamyan" code="AF-BAM"/>
#          ---
#  </xml>
#
# 2.) A folder structure in the following form:
#  data
#    AF
#      AF-BAL
#      AF-BAM
#
import csv
import os

xml = '<xml>'
currentCountry = ''

def addToXml(country, countryCode, sub, subCode):
    global currentCountry, xml
    if (country != currentCountry):
        if (currentCountry != ''):
            xml +='\n    </country>'
        xml += '\n    <country name=\"' + country + '\" code=\"' + countryCode + '\">'
        currentCountry = country
    xml += '\n        <sub name=\"' + sub + '\" code=\"' + subCode + '\"/>'

def createFolder(root, countryCode, subCode):
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(root + '/' + countryCode):
        os.makedirs(root + '/' + countryCode)
    if not os.path.exists(root + '/' + countryCode + '/' + subCode):
        os.makedirs(root + '/' + countryCode + '/' + subCode)
    placeholder = root + '/' + countryCode + '/' + subCode + '/empty'
    if not os.path.exists(placeholder):
        open(placeholder, 'a').close()


with open('3166-2-country-codes.csv') as f:
    root = '../data'
    c = csv.reader(f)
    for row in c:
        country = row[0]
        country = country.replace('&','&amp;');
        countryCode = row[4]
        sub = row[2]
        subCode = row[1]
        addToXml(country, countryCode, sub, subCode)
        createFolder(root, countryCode, subCode)
    xml += '\n    </country>'
    xml += '\n</xml>\n\n'
    f = open(root + '/index.xml', 'w')
    f.write(xml)
    f.close()

