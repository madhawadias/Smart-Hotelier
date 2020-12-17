from ..services.google_entities import GoogleEntities
import threading
import time

progress = 0


def get_entity_progress():
    return progress


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
            global progress
            _threads = []
            total_data_count = df.shape[0]
            n = 1

            print('entity')

            for index, row in df.iterrows():
                print(count)
                count = count + 1
                progress = (count / total_data_count) * 100

                if count == (n * 580):
                    time.sleep(60)
                    n = n + 1

                thread1 = threading.Thread(target=self.extract_google_entities_client,
                                           args=(df, index, input_column, _output_column, row))
                _threads.append(thread1)
                thread1.start()

            for _thread in _threads:
                _thread.join()

            results.append(df)
            return df
        except Exception as err:
            print("entity helper", err)
