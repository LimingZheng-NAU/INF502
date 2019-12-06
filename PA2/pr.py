# Members: Liming Zheng, Juntong liu, Pengkai Fang

# In the pr.py, it scrape the pull request content

import requests
import json
import os
import csv
import pandas as pd

from user import User


class PullRequest:
    def __init__(self, user, repo):
        self.__user = user
        self.__repo = repo
        self.content = {'title': [], 'number': [], 'body': [], 'state': [], 'created_at': [], 'closed_at': [], 'user': [], 'commits': [], 'additions': [], 'deletions': [], 'changed_files': []}

    def to_CSV(self):
        # create directory
        if not os.path.isdir('projects'):
            os.mkdir('projects')

        # write header
        filename = os.path.join('projects', self.__user + '-' + self.__repo + '.csv')
        if not os.path.isfile(filename):
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['title', 'number', 'body', 'state', 'created_at', 'closed_at', 'user', 'commits', 'additions', 'deletions', 'changed_files'])
                writer.writeheader()

        # convert data format
        content = list(self.content.values())
        entries = tuple(zip(*content))
        entries = [list(entry) for entry in entries]

        # write new entries
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(entries)

        # remove duplicated entries and keep the last
        df = pd.read_csv(filename, header=0, index_col=False)
        df.drop_duplicates(subset='number', keep='last', inplace=True)
        df.to_csv(filename, index=False)

    def scrape(self):
        print("scraping pull requests")

        # load contents
        url = 'https://api.github.com/search/issues?q=is:pr+repo:' + self.__user + '/' + self.__repo
        try:
            repodata = requests.get(url).text
            data = json.loads(repodata)
        except Exception as e:
            print("Error Occurred!")
            exit()

        if data['total_count'] is not 0:
            # set values
            for pr in data['items']:
                # check for real users
                if pr['user']['type'] == 'User':
                    self.content['title'].append(pr['title'])
                    self.content['number'].append(pr['number'])
                    self.content['body'].append(pr['body'])
                    self.content['state'].append(pr['state'])
                    self.content['created_at'].append(pr['created_at'])
                    self.content['closed_at'].append(pr['closed_at'])
                    self.content['user'].append(pr['user']['login'])

                    # load specific PR contents
                    url = 'https://api.github.com/repos/' + self.__user + '/' + self.__repo + '/pulls/' + str(
                        pr['number'])
                    try:
                        repodata = requests.get(url).text
                        pr_data = json.loads(repodata)
                    except Exception as e:
                        print("Error Occurred!")
                        exit()

                    # set PR values
                    self.content['commits'].append(pr_data['commits'])
                    self.content['additions'].append(pr_data['additions'])
                    self.content['deletions'].append(pr_data['deletions'])
                    self.content['changed_files'].append(pr_data['changed_files'])

            # scrape user information
            user = User(self.content['user'])
            user.scrape()

            # output to file
            try:
                self.to_CSV()
            except Exception as e:
                print("Failed to write to CSV file!")
                exit()
