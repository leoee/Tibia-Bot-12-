import os

path = os.getcwd()
parent = os.path.dirname(path)

def get_status_bar_in_percent(pixel_value):
  with open(parent + '\src/config_bar_values.json', 'r') as openfile: 
    configuration = json.load(openfile)
  
  value_90 = configuration['90']['value']
  value_70 = configuration['70']['value']
  value_50 = configuration['50']['value']

  if pixel_value >= value_50:
    percentage_value = 50
  elif pixel_value >= value_70:
    percentage_value = 70
  elif pixel_value > value_90:
    percentage_value = 90

  return percentage_value


  