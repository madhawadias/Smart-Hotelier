from flask import Flask
from flask_cors import CORS
from back_end.routes.sentiment_analysis_global_route import sentiment_analysis_global_endpoint
from back_end.routes.report_progress_global_route import report_progress_global_endpoint

app = Flask(__name__)
CORS(app)
url_prefix = '/api'

app.register_blueprint(sentiment_analysis_global_endpoint, url_prefix=url_prefix)
app.register_blueprint(report_progress_global_endpoint, url_prefix=url_prefix)

if __name__ == '__main__':
    app.run(debug=True)
