# Members: Liming Zheng, Juntong liu, Pengkai Fang

# we use Jabref/jabref as an example to test
# test the pull request function

import unittest

from repo import Repository
from loader import Loader

class MyTestCase(unittest.TestCase):
    def test_repo(self):
        repo = Repository('Jabref', 'jabref')
        repo.scrape()
        loader_repos = Loader('repo')
        i = 0
        data_repos = loader_repos.load_data()
        for repo in data_repos:
            loader_prs = Loader('pr')
            loader_prs.set_login(repo['login'])
            loader_prs.set_name(repo['name'])
            data_prs = loader_prs.load_data()
            for data_pr in data_prs:
                i += 1
                if i == 1:
                    self.assertEqual("24", data_pr['number'])
                if i == 2:
                    self.assertEqual("20", data_pr['number'])
                if i == 3:
                    self.assertEqual("16", data_pr['number'])
                if i == 4:
                    self.assertEqual("15", data_pr['number'])

if __name__ == '__main__':
    unittest.main()
