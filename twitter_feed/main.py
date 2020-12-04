import json
import pandas as pd
from tabulate import tabulate

with open('twitter.json', encoding="utf8") as f:
  data = json.load(f)

# print(data)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

df = pd.DataFrame(data["data"])
# print(df)


# print("\n")
# print( df['text'])
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

export_csv = df.to_csv (r'twitterfeed.csv', index = None, header=True)