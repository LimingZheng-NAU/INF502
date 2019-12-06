# Members: Liming Zheng, Juntong liu, Pengkai Fang

# In the repo.py, scrape the repo content

import requests
import json
from datetime import date
import os
import csv
import pandas as pd


class Repository:
    def __init__(self, user, repo):
        self.__user = user
        self.__repo = repo

    def to_CSV(self):
        # write header
        if not os.path.isfile('projects.csv'):
            with open('projects.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['name', 'login', 'description', 'homepage', 'license', 'forks', 'watchers', 'date_of_collection'])
                writer.writeheader()

        # write new entry
        with open('projects.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.name, self.login, self.description, self.homepage, self.license, self.forks, self.watchers, self.date_of_collection])

        # remove duplicated entries and keep the last
        df = pd.read_csv('projects.csv', header=0, index_col=False)
        df.drop_duplicates(subset='name', keep='last', inplace=True)
        df.to_csv('projects.csv', index=False)

    def scrape(self):
        print("scraping repository", self.__user + '/' + self.__repo)

        # load contents
        url = 'https://api.github.com/repos/' + self.__user + '/' + self.__repo
        try:
            repodata = requests.get(url).text
            data = json.loads(repodata)
        except Exception as e:
            print("Error Occurred!")
            exit()

        # set values
        self.name = data['name']
        self.login = data['owner']['login']
        self.description = data['description']
        self.homepage = data['homepage']
        self.license = data['license']['name']
        self.forks = data['forks']
        self.watchers = data['watchers']
        self.date_of_collection = date.today()

        # output to file
        try:
            self.to_CSV()
        except Exception as e:
            print("Failed to write to CSV file!")
            exit()
