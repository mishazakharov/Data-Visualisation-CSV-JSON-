from pygal.maps.world import COUNTRIES 

def get_code(country_name):
	'''Определяет код страны, вызывая его из модуля.'''
	for code,name in COUNTRIES.items():
		if name == str(country_name):
			return code
		# Если страница не найдена, возвращает None.			
	return None
