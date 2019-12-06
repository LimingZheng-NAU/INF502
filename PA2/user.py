# Members: Liming Zheng, Juntong liu, Pengkai Fang

# In the user.py, it scrape the user page content

from bs4 import BeautifulSoup
import requests
import json
import os
import csv
import pandas as pd


class User:
    def __init__(self, users):
        # user list with repeated entries
        self.__users = users
        # scraped users information
        self.users = {}

    @staticmethod
    def __user_has_twitter(user):
        if requests.get('https://twitter.com/' + user).status_code == 200:
            return 1
        else:
            return 0

    def to_CSV(self):
        # write header
        filename = os.path.join('users.csv')
        if not os.path.isfile(filename):
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['user', 'total_pr', 'user_has_twitter', 'public_repos', 'followers', 'following', 'commit_last_year'])
                writer.writeheader()

        # write new entry
        with open('users.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for user in self.users:
                entry = list(self.users[user].values())
                entry.insert(0, user)
                writer.writerow(entry)

        # remove duplicated entries and keep the last
        df = pd.read_csv(filename, header=0, index_col=False)
        df.drop_duplicates(subset='user', keep='last', inplace=True)
        df.to_csv(filename, index=False)

    def scrape(self):
        users = set(self.__users)
        for user in users:
            print("scraping user", user)
            self.users[user] = {}

            # PRs
            self.users[user]['total_pr'] = self.__users.count(user)

            # does user has twitter account
            self.users[user]['user_has_twitter'] = self.__user_has_twitter(user)

            # load contents
            url = 'https://api.github.com/users/' + user
            try:
                repodata = requests.get(url).text
                data = json.loads(repodata)
            except Exception as e:
                print("Error Occurred!")
                exit()

            # set values
            self.users[user]['public_repos'] = data['public_repos']
            self.users[user]['followers'] = data['followers']
            self.users[user]['following'] = data['following']

            # fetch contributions number in the last year
            url = 'https://github.com/users/' + user + '/contributions'
            try:
                html_content = requests.get(url).text
                soup = BeautifulSoup(html_content, features="html.parser")
                text = soup.findAll('h2', {'class': 'f4 text-normal mb-2'})[0].text
                total = int(''.join(filter(str.isdigit, text)))
                self.users[user]['commit_last_year'] = total
            except Exception as e:
                print("Error Occurred!")
                exit()

        try:
            self.to_CSV()
        except Exception as e:
            print("Failed to write to CSV file!")
            exit()
