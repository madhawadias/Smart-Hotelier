import google.auth.exceptions as google_auth_exceptions
from google.api_core import exceptions
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
from langdetect import detect


class TranslationService(object):
    def __init__(self):
        try:
            credentials = service_account.Credentials.from_service_account_file('C:/Users/ashen/Documents/kaliso/Smart'
                                                                                '-Hotelier/back_end/temp_data/test.json')
            self.translate_client = translate.Client(credentials=credentials)
        except google_auth_exceptions.GoogleAuthError:
            pass
        except exceptions.ClientError:
            pass

    def get_language(self, text):
        try:
            lang = detect(text)
            return lang
        except Exception as err:
            if err == 'Need to load profiles.':
                lang = 'unknown'
                return lang
            print('get_language', lang, err)

    def translate_text(self, text):
        try:
            if text is not None:
                language = self.get_language(text)
                if language not in ["en", "und"]:
                    translation = self.translate_client.translate(text, target_language='EN')
                    return translation['translatedText']
                else:
                    return text
        # except Exception as err:
        #     if str(err)[:3] == "403":
        #         try:
        #             print('translate error 403')
        #             time.sleep(60)
        #             translation = self.translate_client.translate(text, target_language='EN')
        #             return translation['translatedText']
        #         except Exception as err:
        #             pass
        except Exception as err:
            print('translate', err)
