# Members: Liming Zheng, Juntong liu, Pengkai Fang

# In the github.py, it import the repo.py, pr.py, loader.py ,graph.py file data
# We create a user interface in terminal, user use the parameter we set to choose which user(login) and the user(login) repository they want to scrape
# We also calculate the correlation in this file
# We can run the code in the terminal use the parameter we set in the OptionParser function
# parameter: -c user(login) repository
#            -r
#            -p
#            -s
#            -g user(login) repository
#            -a
#            -u
#            -i
# eg: user input the "python3 github.py -c Jabref jabref" in the terminal window

from optparse import OptionParser

from repo import Repository
from pr import PullRequest
from loader import Loader
from graph import Graph

import numpy as np

parser = OptionParser()

def parse_args():
    # parse arguments
    global options, args
    parser.add_option("-c", "--collect", action="append", dest="collect", help="scrape a repository and collect everything (repository, pull request, users). User input username (login) and repository name")
    parser.add_option("-r", "--repos", action="store_true", dest="repos", help="list all repos collected")
    parser.add_option("-p", "--pullrequest", action="store_true", dest="pullrequest", help="list all pull requests from a repo (choose what repository you want to see)")
    parser.add_option("-s", "--summary", action="store_true", dest="summary", help="list the summary of a repo(choose what repository you want to see)")
    parser.add_option("-g", "--graph", action="append", dest="graph", help="create graphics given a repo. User input username (login) and repository name")
    parser.add_option("-a", "--allpr", action="store_true", dest="allpr", help="create graphics considering all pull requests from all repos")
    parser.add_option("-u", "--usercorrelation", action="store_true", dest="usercorrelation", help="calculate the correlation between the data collected for a user")
    parser.add_option("-i", "--inprcorrelation", action="store_true", dest="inprcorrelation", help="calculate the correlation between all the numeric data in the pull requests for a repo")
    (options, args) = parser.parse_args()

def execute():
    # request the system to collect data for a specific repository
    if options.collect:
        # scrape repository specified
        repo = Repository(options.collect[0], args[0])
        repo.scrape()

        # scrape pull requests for this repository, including users
        pr = PullRequest(options.collect[0], args[0])
        pr.scrape()
        return

    # list all repos collected
    loader_repos = Loader('repo')
    data_repos = loader_repos.load_data()
    if options.repos:
        for data_repo in data_repos:
            description = data_repo['login'] + '/' + data_repo['name'] + ': ' + data_repo['description'] + ' (' + \
                          data_repo['watchers'] + ' of stars)'
            print(description)

    # list all pull requests from a repo (or summary)
    if options.pullrequest or options.summary:
        # list all repos for choosing
        print("Repositories: ")
        for data_repo in data_repos:
            description = data_repo['login'] + '/' + data_repo['name']
            print(description)

        # choose and list pull requests
        login_chosen = input("\nUsername (login): ")
        name_chosen = input("Repository Name: ")
        loader_prs = Loader('pr')
        loader_prs.set_login(login_chosen)
        loader_prs.set_name(name_chosen)
        data_prs = loader_prs.load_data()

        # output the detail
        if options.pullrequest:
            for data_pr in data_prs:
                description = 'title: ' + data_pr['title'] + ', number: ' + data_pr['number'] + ', state: ' + data_pr['state'] + ', by user: ' + data_pr['user'] + ', commits: ' + data_pr['commits']
                print(description)

        # output summary
        if options.summary:
            pr_open = 0
            pr_closed = 0
            pr_users = []
            smallest_number = 999999
            oldest_date = ''
            for data_pr in data_prs:
                if data_pr['state'] == 'open':
                    pr_open += 1
                if data_pr['state'] == 'closed':
                    pr_closed += 1
                pr_users.append(data_pr['user'])
                if int(data_pr['number']) < smallest_number:
                    smallest_number = int(data_pr['number'])
                    oldest_date = data_pr['created_at']
            pr_users = len(set(pr_users))
            print("\nRepository Summary:\n")
            print("number of pull requests in 'open' state:", pr_open)
            print("number of pull requests in 'closed' state:", pr_closed)
            print("number of users:", pr_users)
            print("date of the oldest pull request:", oldest_date)
            # twitter data is located in user class

    # create graphics given a repo, or create graphics considering all pull requests from all repos
    if options.graph or options.allpr:
        graph = Graph()
        if options.graph:
            graph.set_repo(options.graph[0], args[0])
        graph.display()

    # calculate the correlation between the data collected for a user
    if options.usercorrelation:
        loader_repos = Loader('user')
        data_users = loader_repos.load_data()
        for user in data_users:
            co = np.corrcoef([int(user['followers']), int(user['following']), int(user['commit_last_year'])])
            print("Correlation: ", co)

    # calculate the correlation between all the numeric data in the pull requests for a repo
    if options.inprcorrelation:
        loader_repos = Loader('repo')
        data_repos = loader_repos.load_data()
        for repo in data_repos:
            loader_prs = Loader('pr')
            loader_prs.set_login(repo['login'])
            loader_prs.set_name(repo['name'])
            data_prs = loader_prs.load_data()
            for data_pr in data_prs:
                co = np.corrcoef([int(data_pr['number']), int(data_pr['commits']), int(data_pr['additions']), int(data_pr['deletions']), int(data_pr['changed_files'])])
                print("Correlation: ", co)

def main():
    parse_args()
    execute()

if __name__ == '__main__':
    main()
