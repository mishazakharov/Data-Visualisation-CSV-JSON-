import json
import pygal
from get_codes import get_code as gc
from pygal.style import RotateStyle


# Список заполняется данными.
file_name = 'vvp.json'
with open(file_name) as f:
	pop_date = json.load(f)
	completed = {}
	# Вывод ввп каждой строны за 2001 год.
	for pop_dict in pop_date:
		if pop_dict['Year'] == 2010:
			country_name = pop_dict['Country Name']
			vvp = int(float(pop_dict['Value']))
			code = gc(country_name)
			if code:
				completed[code] = vvp

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'VVP'
wm.add('2010',completed)
wm.render_to_file('vvp.svg')













