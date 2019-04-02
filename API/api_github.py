import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

my_style = LS('#336699',base_style=LCS)
my_config = pygal.Config() 
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

url = 'https://api.github.com/search/repositories?q=language:haskell&sort=star'
r = requests.get(url)
print('Status code:',str(r.status_code))
response_dict = r.json()
repo_dicts = response_dict['items']
names,plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict = {
				'value':repo_dict['stargazers_count'],
				'label':str(repo_dict['description']),
				'xlink':repo_dict['html_url'],
				}
	plot_dicts.append(plot_dict)

top = pygal.Bar(my_config,style=my_style)
top.title = 'The most popular project on GitHub'
top.x_labels = names
top.add('', plot_dicts)
top.render_to_file('projects.svg')

