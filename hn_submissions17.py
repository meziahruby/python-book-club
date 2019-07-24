# Use the Hacker News API
import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission
# Using the url with top stories, create new urls finding each story to get info
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	# Make a separate API call for each submission.
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()
	submission_dict = {
		'title': response_dict['title'],
		'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
		'comments': response_dict.get('descendants', 0),
		'id': response_dict['id']
		}
	submission_dicts.append(submission_dict)
	
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
							reverse=True)
							
for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])
	print("ID #:", submission_dict['id'])
		
# With what I have, figure out a way for:
#	bar = # comments (submission_dict['comments'])
#	xlink = link to page (submission_dict['link'])
#	label = submission's title (submission_dict['title'])
#	



# Store the names and number of stars together to plot, from most popular repos
names, plot_dicts = [],[]
for submission_dict in submission_dicts:
	names.append(submission_dict['id'])
	plot_dict = {
			'value': submission_dict['comments'],
			'label': str(submission_dict['title']),
			'xlink': submission_dict['link'],
#Note- here, had to define the label as a string, maybe because of other language characters
			}
	plot_dicts.append(plot_dict)
#	plot_dicts.append({'value': repo_dict['stargazers_count'],
#				'label': repo_dict['description']})
	# print('\nSelected information about the first repository:')
	# print('Name:', repo_dict['name'])
	# print('Owner:',repo_dict['owner']['login'])
	# print('Stars:', repo_dict['stargazers_count'])
	# print('Repository:', repo_dict['html_url'])
	# print('Created:', repo_dict['created_at'])
	# print('Updated:', repo_dict['updated_at'])
	# print('Description:', repo_dict['description'])
# Make a visualization
# Make a style (color) and configuration (arrangement)
my_style = LS('#333366', base_style = LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most-Commented Articles on Y Combinator'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('popular_ycomb_articles.svg')
