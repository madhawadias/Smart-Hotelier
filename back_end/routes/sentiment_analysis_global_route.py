from flask import Blueprint, jsonify
import pandas as pd
from back_end.helpers.sentiment_analysis_global_helper import SentimentAnalysisGlobalHelper
from back_end.helpers.google_entities_helper import GoogleEntitiesHelper
from back_end.helpers.google_translate_helper import TranslateHelper

sentiment_analysis_global_endpoint = Blueprint("sentiment_analysis_global", __name__)


@sentiment_analysis_global_endpoint.route("/report/sentimentAnalyse", methods=['GET'])
def get_sentiment_analyse_report():
    _sentiment_analysis_global_helper = SentimentAnalysisGlobalHelper()
    _google_translate_helper = TranslateHelper()
    _google_entities_helper = GoogleEntitiesHelper()

    # df = pd.read_csv("C:/Users/ashen/Documents/kaliso/Smart-Hotelier/back_end/data/kingsbury-tripadvisor.csv")
    # df = df.dropna(subset=['review'])
    #
    # #limites the dataframe
    # df = df[:250]
    #
    # df = _google_translate_helper.runner(df, "review")
    # df = df.dropna(subset=['translated'])
    # df = _google_entities_helper.runner(df, "translated")
    # df = _sentiment_analysis_global_helper.runner(df, "translated")
    # df.to_csv(r'temp_data/kingsbury-tripadvisor-analyzed.csv', index=False)

    df = pd.read_csv(
        "C:/Users/ashen/Documents/kaliso/Smart-Hotelier/back_end/temp_data/kingsbury-tripadvisor-analyzed.csv")
    # df = df.dropna(subset=['sentiment'])

    positive = df[df['sentiment'] == 'positive'].shape[0]
    negative = df[df['sentiment'] == 'negative'].shape[0]
    neutral = df[df['sentiment'] == 'neutral'].shape[0]
    total = df['sentiment'].shape[0]

    negative = (negative / total) * 100
    neutral = (neutral / total) * 100
    positive = (positive / total) * 100

    data = [round(negative, 2), round(neutral, 2), round(positive, 2)]

    wordcloud = []

    for index, row in df.iterrows():
        entities = eval(str(row['entities']))['name']
        for entity in entities:
            item = {'text': '', 'value': 0}

            if wordcloud:
                index = 0
                for word in wordcloud:
                    if word['text'].casefold() == entity.casefold():
                        wordcloud[index]['value'] = wordcloud[index]['value'] + 1
                        break

                    index = index + 1

                item['text'] = entity
                item['value'] = 1
                wordcloud.append(item)

            else:
                item['text'] = entity
                item['value'] = 1
                wordcloud.append(item)

        print(wordcloud)

    result = [{
        'name': 'Kingsbury',
        'data': data,
        'wordcloud': wordcloud
    }]

    return jsonify(result)
