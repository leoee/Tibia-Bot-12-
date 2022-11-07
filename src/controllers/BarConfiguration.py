import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

class BarConfiguration():
	def get_bar_locations(self):
		locations = None
		with open(parent + '\src/config_location.json', 'r') as openfile:
			locations = json.load(openfile)

		return locations

	def get_status_bar_in_percent(self, pixel_value):
		with open(parent + '\src/config_bar_values.json', 'r') as openfile: 
			configuration = json.load(openfile)

		value_90 = configuration['90']['value']
		value_70 = configuration['70']['value']
		value_50 = configuration['50']['value']
		percentage_value = 100

		if pixel_value >= int(value_50):
			percentage_value = 50
		elif pixel_value >= int(value_70):
			percentage_value = 70
		elif pixel_value > value_90:
			percentage_value = 90

		return percentage_value

	def save_config_screen(self, width, height, location_life, location_mana, location_statuses, location_party_list):
		if location_life == None or location_life == None or location_statuses == None:
			raise Exception('Invalid value')

		if location_party_list == None:
			location_party_list = [0, 0, 0, 0]

		locations = {
			"life": {
				"left": int(location_life[0]),
				"top": int(location_life[1]),
				"width": int(location_life[2] * 1.3),
				"height": int(location_life[3])
			},
			"mana": {
				"left": int(location_mana[0]),
				"top": int(location_mana[1]),
				"width": int(location_mana[2] * 1.3),
				"height": int(location_mana[3])
			},
			"statuses": {
				"left": int(location_statuses[0] + width * 0.7),
				"top": int(location_statuses[1]),
				"width": int(location_statuses[2] * 2),
				"height": int(location_statuses[3] * 1.2)
			},
			"status_fight": {
				"left": int((location_statuses[0] + width * 0.7) * 0.99),
				"top": int(0),
				"width": int(location_statuses[0] * 1.1),
				"height": abs(int(height * 0.4))
			},
			"party_list": {
				"left": int(location_party_list[0]),
				"top": int(location_party_list[1]),
				"width": int(location_party_list[2]),
				"height": int(location_party_list[3] * 3)
			},
		}
	
		json_object = json.dumps(locations, indent=4)
		
		with open("config_location.json", "w") as outfile:
				outfile.write(json_object)