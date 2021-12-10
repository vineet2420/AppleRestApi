from flask import Flask, request
import csv
import datetime
import time

app = Flask(__name__)

fileContents = []

with open('Data/AAPL.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        fileContents.append(dict(row))
        # print(dict(row))


@app.route('/')
def main():
    return "Server is on"

import GetRoutes
import PostRoutes
import PutRoutes
import DeleteRoutes