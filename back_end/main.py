from .helpers.google_entities_helper import GoogleEntitiesHelper
from .helpers.google_translate_helper import TranslateHelper
from .helpers.sentiment_analysis_global_helper import SentimentAnalysisGlobalHelper
import pandas as pd

_sentiment_analysis_global_helper = SentimentAnalysisGlobalHelper()
_google_translate_helper = TranslateHelper()
_google_entities_helper = GoogleEntitiesHelper()

df = pd.read_csv("../data/kingsbury-tripadvisor.csv")
df = df.dropna(subset=['review'])

df = _google_translate_helper.runner(df, "review")
df = _google_entities_helper.runner(df, "translated")
df = _sentiment_analysis_global_helper.runner(df, "translated")

df.to_csv(r'temp_data/kingsbury-tripadvisor-analized.csv', index=False)
print(df)
