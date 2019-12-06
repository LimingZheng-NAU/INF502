# Members: Liming Zheng, Juntong liu, Pengkai Fang

# we use Jabref/jabref as an example to test
# test the user function

import unittest

from repo import Repository
from loader import Loader

class MyTestCase(unittest.TestCase):
    def test_repo(self):
        repo = Repository('Jabref', 'jabref')
        repo.scrape()
        loader_repos = Loader('user')
        i = 0
        data_repos = loader_repos.load_data()
        for x in data_repos:
            i += 1
            if i == 1:
                self.assertEqual("1", x['total_pr'])

if __name__ == '__main__':
    unittest.main()
