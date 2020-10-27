from ..services.sentiment_analysis_global import SentimentAnalysisGlobal
import threading
import time


class SentimentAnalysisGlobalHelper:

    def __init__(self):
        self._sentiment_analysis_global = SentimentAnalysisGlobal()

    def get_sentiment_client(self, df, index, input_column, output_column_sentiment, _output_column_magnitude, row):
        input_cell = str(row[input_column])
        _result = self._sentiment_analysis_global.analyze_global_sentiment(input_cell)
        df.at[index, output_column_sentiment] = _result[0]
        df.at[index, _output_column_magnitude] = _result[1]

    def runner(self, df, input_column, results=[]):
        _output_column_sentiment = "sentiment"
        _output_column_magnitude = "sentiment magnitude"

        df[_output_column_sentiment] = None
        df[_output_column_magnitude] = None
        count = 0
        _threads = []
        for index, row in df.iterrows():
            count = count + 1
            if count == 400:
                time.sleep(60)
                count = 0
            thread1 = threading.Thread(target=self.get_sentiment_client,
                                       args=(
                                           df, index, input_column, _output_column_sentiment, _output_column_magnitude,
                                           row))
            _threads.append(thread1)
            thread1.start()
        for _thread in _threads:
            _thread.join()
        results.append(df)
        return df
