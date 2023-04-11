import yaml
from pprint import pprint

data = yaml.load(open("test.yml"), Loader=yaml.FullLoader)
pprint(data)
for element in data:
    for element2 in element:
        print(element2)
