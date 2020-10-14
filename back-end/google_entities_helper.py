from services.google_entities import GoogleEntities
import threading
import time


class GoogleEntitiesHelper:

    def __init__(self):
        self._google_entities = GoogleEntities()

    def extract_google_entities_client(self, df, index, input_column, output_column, row):
        input_cell = str(row[input_column])
        _result = self._google_entities.extract_entities(input_cell)
        df.at[index, output_column] = _result

    def runner(self, df, input_column, results=[]):
        _output_column = 'entities'
        try:
            df[_output_column] = None
            count = 0
            _threads = []
            for index, row in df.iterrows():
                count = count + 1
                if count == 400:
                    time.sleep(60)
                    count = 0
                thread1 = threading.Thread(target=self.extract_google_entities_client,
                                           args=(df, index, input_column, _output_column, row))
                _threads.append(thread1)
                thread1.start()
            for _thread in _threads:
                _thread.join()
            results.append(df)
            return df
        except:
            pass
