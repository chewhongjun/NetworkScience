import json
import pandas as pd
import csv

# Read the data from file
# We now have a Python dictionary
with open('database/article.json') as f:
    data_listofdict = json.load(f)
    
# Writing a list of dicts to CSV
keys = data_listofdict[0].keys()
with open('database/article.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_listofdict.encode())