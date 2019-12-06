# Members: Liming Zheng, Juntong liu, Pengkai Fang

# In the graph.py, it import loader.py
# In the loader.py, we can extract data from projects.csv, user.csv, project-repository.csv
# When get the data, it can plot the required image

import matplotlib.pyplot as plt
from loader import Loader


class Graph:
    def __init__(self):
        self.__allpr = True

    def set_repo(self, login, repo):
        self.login = login
        self.repo = repo
        self.__allpr = False

    def display(self):
        # create graphics given a repo
        if not self.__allpr:
            loader_prs = Loader('pr')
            loader_prs.set_login(self.login)
            loader_prs.set_name(self.repo)
            data_prs = loader_prs.load_data()

            # boxplot comparing closed and open pull requests in terms of number of commits
            # close prs
            data = []
            for data_pr in data_prs:
                if data_pr['state'] == 'closed':
                    data.append(int(data_pr['commits']))
            fig1, ax1 = plt.subplots()
            ax1.set_title('boxplot comparing closed and open pull requests in terms of number of commits')
            ax1.boxplot(data)
            # open prs
            data = []
            for data_pr in data_prs:
                if data_pr['state'] == 'open':
                    data.append(int(data_pr['commits']))
            fig1, ax1 = plt.subplots()
            ax1.set_title('boxplot comparing open and open pull requests in terms of number of commits')
            ax1.boxplot(data)

            # boxplot comparing closed and open pull requests in terms of additions and deletions
            # close prs in terms of additions
            data = []
            for data_pr in data_prs:
                if data_pr['state'] == 'closed':
                    data.append(int(data_pr['additions']))
            fig1, ax1 = plt.subplots()
            ax1.set_title('boxplot comparing closed and open pull requests in terms of additions')
            ax1.boxplot(data)
            # open prs in terms of additions
            data = []
            for data_pr in data_prs:
                if data_pr['state'] == 'open':
                    data.append(int(data_pr['additions']))
            fig1, ax1 = plt.subplots()
            ax1.set_title('boxplot comparing open and open pull requests in terms of additions')
            ax1.boxplot(data)

            # close prs in terms of deletions
            data = []
            for data_pr in data_prs:
                if data_pr['state'] == 'closed':
                    data.append(int(data_pr['deletions']))
            fig1, ax1 = plt.subplots()
            ax1.set_title('boxplot comparing closed and open pull requests in terms of deletions')
            ax1.boxplot(data)
            # open prs in terms of deletions
            data = []
            for data_pr in data_prs:
                if data_pr['state'] == 'open':
                    data.append(int(data_pr['deletions']))
            fig1, ax1 = plt.subplots()
            ax1.set_title('boxplot comparing open and open pull requests in terms of deletions')
            ax1.boxplot(data)

            # scatterplot: additions x deletions
            x = []
            y = []
            for data_pr in data_prs:
                x.append(int(data_pr['additions']))
            for data_pr in data_prs:
                y.append(int(data_pr['deletions']))
            plt.scatter(x, y)
            plt.title('additions x deletions')
            plt.show()

            # histogram: number of commits per pull request
            z = []
            for data_pr in data_prs:
                z.append(int(data_pr['commits']))
            plt.hist(x)
            plt.title('number of commits per pull request')
            plt.show()

        # create graphics considering all pull requests from all repos
        else:
            # line graph showing the total number of pull requests per day
            loader_repos = Loader('repo')
            data_repos = loader_repos.load_data()
            x = [1]
            y = [0]
            for repo in data_repos:
                loader_prs = Loader('pr')
                loader_prs.set_login(repo['login'])
                loader_prs.set_name(repo['name'])
                data_prs = loader_prs.load_data()
                for data_pr in data_prs:
                    x.append(x[-1] + 1)
                    y.append(data_pr['commits'])
            plt.plot(x, y)
            plt.xlabel('day')
            plt.ylabel('PR')
            plt.show()

            # bars comparing the number of users per repo
            loader_repos = Loader('repo')
            data_repos = loader_repos.load_data()
            y = []
            for repo in data_repos:
                loader_prs = Loader('pr')
                loader_prs.set_login(repo['login'])
                loader_prs.set_name(repo['name'])
                data_prs = loader_prs.load_data()
                z = []
                for data_pr in data_prs:
                    z.append(data_pr['user'])
                y.append(len(set(z)))
            plt.bar(y, height=max(y))
            plt.ylabel('users')
            plt.title('number of users per repo')
            plt.show()

            # histogram: number of commits per pull request
            loader_repos = Loader('repo')
            data_repos = loader_repos.load_data()
            y = []
            for repo in data_repos:
                loader_prs = Loader('pr')
                loader_prs.set_login(repo['login'])
                loader_prs.set_name(repo['name'])
                data_prs = loader_prs.load_data()
                for data_pr in data_prs:
                    y.append(data_pr['commits'])
            plt.hist(y)
            plt.title('number of commits per pull request')
            plt.show()