# Members: Liming Zheng, Juntong liu, Pengkai Fang

# In the loader.py, we can extract data from projects.csv, user.csv, project-repository.csv

import csv

class Loader:
    def __init__(self, method):
        self.method = method

    def set_login(self, login):
        self.login = login

    def set_name(self, name):
        self.name = name

    def load_data(self):
        try:
            if self.method == 'repo':
                data = csv.DictReader(open('projects.csv'))
                return list(data)

            if self.method == 'pr':
                data = csv.DictReader(open('projects/' + self.login + '-' + self.name + '.csv'))
                return list(data)

            if self.method == 'user':
                data = csv.DictReader(open('users.csv'))
                return list(data)
        except Exception as e:
            print("Failed to read CSV file!")
            exit()
