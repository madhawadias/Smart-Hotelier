from ..services.sentiment_analysis_global import SentimentAnalysisGlobal
import threading
import time

progress = 0


def get_sentiment_progress():
    return progress


class SentimentAnalysisGlobalHelper:

    def __init__(self):
        self._sentiment_analysis_global = SentimentAnalysisGlobal()

    def get_sentiment_client(self, df, index, input_column, output_column_sentiment_value, _output_column_magnitude,
                             output_column_sentiment, row):
        input_cell = str(row[input_column])
        _result = self._sentiment_analysis_global.analyze_global_sentiment(input_cell)

        try:
            df.at[index, output_column_sentiment_value] = _result[0]
            df.at[index, _output_column_magnitude] = _result[1]

            if _result[0] > 0.25:
                df.at[index, output_column_sentiment] = 'positive'
            elif _result[0] < -0.25:
                df.at[index, output_column_sentiment] = 'negative'
            else:
                df.at[index, output_column_sentiment] = 'neutral'
        except Exception as e:
            print(e)

    def runner(self, df, input_column, results=[]):
        _output_column_sentiment_value = "sentiment value"
        _output_column_magnitude = "sentiment magnitude"
        _output_column_sentiment = 'sentiment'

        df[_output_column_sentiment_value] = None
        df[_output_column_magnitude] = None
        df[_output_column_sentiment] = None

        try:
            count = 0
            global progress
            total_data_count = df.shape[0]
            quota = (total_data_count % 580)
            _threads = []
            n = 1

            print('sentiment', total_data_count)

            for index, row in df.iterrows():
                print(count)
                count = count + 1
                quota = quota + 1
                progress = (count / total_data_count) * 100

                if quota == (n * 580):
                    time.sleep(60)
                    n = n + 1
                try:
                    thread1 = threading.Thread(target=self.get_sentiment_client,
                                               args=(
                                                   df, index, input_column, _output_column_sentiment_value,
                                                   _output_column_magnitude,
                                                   _output_column_sentiment, row))
                    _threads.append(thread1)
                    thread1.start()
                except Exception as err:
                    print('sentiment helper 2', err)

            for _thread in _threads:
                _thread.join()
                results.append(df)

            return df
        except Exception as err:
            print('sentiment helper 2', err)
