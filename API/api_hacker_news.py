import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code: ',r.status_code)
# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts,names = [], []
for submission_id in submission_ids[:10]:
	# Создание отдельного вызова API для каждой статьи
	url = ('https://hacker-news.firebaseio.com/v0/item/' + 
						str(submission_id) + '.json')
	submission_r = requests.get(url)
	response_dict = submission_r.json()
	names.append(response_dict['title'])
	submission_dict = {
				'value':response_dict.get('descendants',0),
				'xlink':('http://news.ycombinator.com/item?id=' + 
												str(submission_id)),
					  }
	submission_dicts.append(submission_dict)

 # Визуализация статей.
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

top = pygal.Bar(my_config,style=my_style)
top.title = 'Articles'
top.x_labels = names
top.add('',submission_dicts)
top.render_to_file('articles.svg')