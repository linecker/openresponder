#!/usr/bin/env python

import csv
import os

def process(countrycode):
    countrycode = countrycode.lower()
    if not os.path.exists(countrycode):
        os.makedirs(countrycode)

with open('3166-1-country-codes.csv') as f:
    c = csv.reader(f)
    for row in c:
        cc = row[1]
        process(cc)


