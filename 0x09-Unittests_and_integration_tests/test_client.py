#!/usr/bin/env python3

'''
test client module classses
'''
from client import GithubOrgClient
from unittest.mock import PropertyMock, patch, Mock, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    '''test suite for github client class'''

    @parameterized.expand([
        ('google', 200),
        ('abc', 200)
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get):
        '''test by ord'''
        test_class = GithubOrgClient(org)
        test_class.org()
        mock_get.assert_called_once_with('"https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        '''public repo mock'''
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)
        as mock:
            test_class = GithubOrgClient('the_org')
            mock.return_value = {"reops_url": "https://the_org.url"}
            r = test_class._public_repos_url()
            self.assertEqual(mock.return_value.get('repos_url'), r)

    @patch('client.GithubOrgClient.pget_json')
    def test_public_repos(self, mock_get):
        '''test public repos'''
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = [{"name": "PyTorch"},
                                 {"name": "Twitter"}]
            test_class = GithubOrgClient("google")
            r = test_class._public_repos_url()
            repo_names = [i["name"] for i in mock.return_value]
            self.assertEqual(r, repo_names)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}})
    ])
    def test_has_license(self, repo, license, license_name):
        '''check if repo has license'''
        r = GithubOrgClient.has_license(repo, license)
        self.assertEqual(r, license_name)
