import pandas as pd
from tabulate import tabulate
import json

# kingsbury

df = pd.read_csv("Kingsbury-Sentiment-analysis.csv")
ksentiment = df['sentiment'].values

ksentimentNegativeCount = sum(n < 0 for n in ksentiment)
ksentimentPositiveCount = sum(n > 0 for n in ksentiment)
ksentimentNeutralCount = sum(n == 0 for n in ksentiment)

print(ksentiment)
print(ksentimentNegativeCount)
print(ksentimentPositiveCount)
print(ksentimentNeutralCount)

ksentimentPositiveCount = str(ksentimentPositiveCount)
ksentimentNegativeCount = str(ksentimentNegativeCount)
ksentimentNeutralCount = str(ksentimentNeutralCount)

ksentimentCount = [ksentimentNegativeCount,ksentimentPositiveCount,ksentimentNeutralCount]


#cinnamon

df = pd.read_csv("cinnamongrand-Sentiment-analysis.csv")
csentiment = df['sentiment'].values

csentimentNegativeCount = sum(n < 0 for n in csentiment)
csentimentPositiveCount = sum(n > 0 for n in csentiment)
csentimentNeutralCount = sum(n == 0 for n in csentiment)

print(csentiment)
print(csentimentNegativeCount)
print(csentimentPositiveCount)
print(csentimentNeutralCount)

csentimentPositiveCount = str(csentimentPositiveCount)
csentimentNegativeCount = str(csentimentNegativeCount)
csentimentNeutralCount = str(csentimentNeutralCount)

csentimentCount = [csentimentNegativeCount,csentimentPositiveCount,csentimentNeutralCount]


 # creating json file

data = {}
data['series'] = []
data['series'].append({
    'name': 'kingsbury',
    'type': 'column',
    'data': ksentimentCount
})
data['series'].append({
    'name': 'cinnamongrand',
    'type': 'column',
    'data': csentimentCount
})




with open('data.json', 'w') as outfile:
    json.dump(data, outfile)




