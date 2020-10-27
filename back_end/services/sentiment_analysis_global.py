import re

from google.api_core import exceptions
from google.cloud import language_v1
from google.cloud import translate_v2 as translate
from google.cloud.language_v1 import enums
from google.oauth2 import service_account


class SentimentAnalysisGlobal:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file('../temp_data/test.json')
        self.client = language_v1.LanguageServiceClient(credentials=credentials)
        self.translate_client = translate.Client(credentials=credentials)

    def translate_text(self, text):
        try:
            if text is not None:
                translation = self.translate_client.translate(text, target_language='EN')
                return translation['translatedText']
        except Exception as err:
            print(err)

    def analyze_global_sentiment(self, text_content):
        """
        Analyzing Sentiment in a String

        Args:
          text_content The text content to analyze
        """
        try:
            try:
                # Available types: PLAIN_TEXT, HTML
                type_ = enums.Document.Type.PLAIN_TEXT
                # Optional. If not specified, the language is automatically detected.
                document = {"content": text_content, "type": type_}
                # Available values: NONE, UTF8, UTF16, UTF32
                encoding_type = enums.EncodingType.UTF8
                try:
                    response = self.client.analyze_sentiment(document, encoding_type=encoding_type)
                    # Get overall sentiment of the input document
                    text_sentiment = round(response.document_sentiment.score, 2)
                    text_magnitude = round(response.document_sentiment.magnitude, 2)
                    return (text_sentiment, text_magnitude)
                except exceptions.ClientError:
                    pass


            except:
                # text_content_translated = self.translate_text(text_content)
                text_content_translated = text_content
                type_ = enums.Document.Type.PLAIN_TEXT
                document = {"content": text_content_translated, "type": type_}
                encoding_type = enums.EncodingType.UTF8
                try:
                    response = self.client.analyze_sentiment(document, encoding_type=encoding_type)
                    text_sentiment = round(response.document_sentiment.score, 2)
                    text_magnitude = round(response.document_sentiment.magnitude, 2)
                    return (text_sentiment, text_magnitude)
                except:
                    pass
        except:
            pass

    def clean_text(self, message):
        try:
            # remove "http"+link
            message = re.sub(r'http\S+', '', message)
            # remove "RT"
            message = re.sub(r'RT', '', message)
            # remove "@"+name
            message = re.sub(r'@\S+', '', message)
            # remove white space when there are more than one
            message = re.sub(r'\s+', ' ', message)
            # remove white space at the beginning of the string
            message = re.sub(r'\A\s', '', message)
            return message
        except:
            return message
