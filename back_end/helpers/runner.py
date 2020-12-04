import pandas as pd
from tabulate import tabulate
from back_end.helpers.google_translate_helper import TranslateHelper
from back_end.helpers.google_entities_helper import GoogleEntitiesHelper
from back_end.helpers.sentiment_analysis_global_helper import SentimentAnalysisGlobalHelper


df = pd.read_csv("../data/kingsbury-tripadvisor.csv")
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))


_google_translate_helper = TranslateHelper()
translate = _google_translate_helper.runner(df, "review")
print(translate)

print("completed translate")


_google_entities_helper = GoogleEntitiesHelper()
entities = _google_entities_helper.runner(df, "translated")
print(entities)
print("completed entities")

_sentiment_analysis_global_helper = SentimentAnalysisGlobalHelper()
sentimentAnalysis = _sentiment_analysis_global_helper.runner(df, "review")
print(sentimentAnalysis)
print("complete sentiment analysis")

print(tabulate(sentimentAnalysis, headers = 'keys', tablefmt = 'psql'))

