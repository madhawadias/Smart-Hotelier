import os

import google.auth.exceptions as google_auth_exceptions
from google.api_core import exceptions
from google.cloud import language_v1, vision, automl
from google.cloud import translate_v2 as translate
from google.cloud.language_v1 import enums
from google.oauth2 import service_account
from langdetect import detect


class GoogleEntities(object):
    def __init__(self):
        try:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/ashen/Documents/kaliso/Smart-Hotelier/back_end' \
                                                           '/temp_data/test.json '
            self.credentials = service_account.Credentials.from_service_account_file(
                'C:/Users/ashen/Documents/kaliso/Smart'
                '-Hotelier/back_end/temp_data/test.json')
            os.environ["PROJECT_ID"] = "quilt-apps"
            self.params = {'score_threshold': '0.1'}
            self.language_service_client = language_v1.LanguageServiceClient()
            self.prediction_client = automl.PredictionServiceClient(credentials=self.credentials)

            self.translate_client = translate.Client()
            self.vision_client = vision.ImageAnnotatorClient()
        except google_auth_exceptions.GoogleAuthError:
            pass
        except exceptions.ClientError:
            pass

    def extract_entities(self, text):
        type_ = enums.Document.Type.PLAIN_TEXT
        document = {"content": text, "type": type_}
        encoding_type = enums.EncodingType.UTF8
        entities_name = []
        entities_type = []
        try:
            response = self.language_service_client.analyze_entities(document, encoding_type=encoding_type)
            for entity in response.entities:
                entities_name.append(entity.name)
                entities_type.append(enums.Entity.Type(entity.type).name)
            results = {"name": entities_name, "type": entities_type}
            return results
        except Exception as err:
            print('entity 2', err)

    def translate_text(self, text):
        try:
            if text is not None:
                lang = detect(text)
                if lang != 'en':
                    translation = self.translate_client.translate(text, target_language='en')
                    return translation["translatedText"]
                else:
                    return text
            else:
                return text
        except:
            pass
