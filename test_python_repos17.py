import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import unittest

class TestAPICall(unittest.TestCase):
	"""Tests the API call for GitHub"""
	
	def setUp(self):
		"""Create an API call for use in test methods"""
		# Make an API call and store the response.
		self.language = 'python'
		self.url = 'https://api.github.com/search/repositories?q=language:'+str(self.language)+'&sort=stars'
		self.r = requests.get(self.url)
		self.status_code = self.r.status_code
		print('Status code:', self.r.status_code)

		# Store API response in a variable.
		self.response_dict = self.r.json()
		self.total_repositories = self.response_dict['total_count']
		print("Total repositories:", self.response_dict['total_count'])

		# Explore information about the repositories
		self.repo_dicts = self.response_dict['items']
		print("Repositories returned:", len(self.repo_dicts))
		self.returned_repositories = len(self.repo_dicts)
		
	def test_status_code(self):
		"""Test that the status code is equal to 200"""
		self.assertEqual(self.status_code,200)
		
	def test_returned_repositories(self):
		"""Test that the returned repositories < total repositories"""
		self.assertTrue(self.returned_repositories<self.total_repositories)

unittest.main()






# def github_pull():
	# def __init__(self,language='javascript'):
		# self.language = language
		# self.url = 'https://api.github.com/search/repositories?q=language:'+str(language)+'&sort=stars'
		# self.r = requests.get(url)
		# self.status_code = self.r.status_code
		# self.response_dict = r.json()
		# self.total_repositories = self.response_dict['total_count']
		# self.repo_dicts = self.response_dict['items']
		# self.returned_repositories = len(self.repo_dicts)
		
	# def get_status_code(self):
		# return self.status_code
	
	# def get_total_repositories(self):
		# return self.total_repositories
		
	# def get_returned_repositories(self):
		# return self.returned_repositories
		


	# # Make an API call and store the response.
	# url = 'https://api.github.com/search/repositories?q=language:'+str(language)+'&sort=stars'
	# r = requests.get(url)
	# print('Status code:', r.status_code)

	# # Store API response in a variable.
	# response_dict = r.json()
	# print("Total repositories:", response_dict['total_count'])

	# # Explore information about the repositories
	# repo_dicts = response_dict['items']
	# print("Repositories returned:", len(repo_dicts))

	# # Examine the first repository.
	# repo_dict = repo_dicts[0]
	# print("\nKeys:", len(repo_dict))
	# for key in sorted(repo_dict.keys()):
		# print(key)
# # This means that each of repo_dicts contains all of the keys just printed.
