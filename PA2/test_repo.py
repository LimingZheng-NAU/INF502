# Members: Liming Zheng, Juntong liu, Pengkai Fang

# we use Jabref/jabref as an example to test
# test the repository function

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
        for x in data_repos:
            i += 1
            if i == 1:
                self.assertEqual("jabref", x['name'])
                self.assertEqual("Jabref", x['login'])

if __name__ == '__main__':
    unittest.main()
