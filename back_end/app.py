from flask import Flask,jsonify
from flask_restplus import Api, Resource, fields, reqparse
from flask_cors import CORS, cross_origin
import werkzeug
import os

app = Flask(__name__)
CORS(app)

file_upload = reqparse.RequestParser()
file_upload.add_argument('file',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True)


api = Api(app, version='1.0', title='SymptomDoc',
    description='Predict diseases using symptoms',
)

sentiment_api = api.namespace('api', description='Sentiment Analysis')

# symptom_model = api.model('Questions',{
#     'Answers': fields.List(fields.Integer, description='Answers for the all questions', required=True),
#     'Type': fields.String(required=True, description='Type of the symptom')
# })

@sentiment_api.route('/predict')
class SentimentAnalysis(Resource):
    """[]

    Arguments:
        Resource {[Object]} -- [packecge of the flask_restplus]
    """

    @sentiment_api.doc('sentiment_values')
    @sentiment_api.expect(file_upload)
    def post(self):
        '''Sentiment analysis'''
        try:
            args = file_upload.parse_args()
            destination = 'uploads/'
            filename, file_extension = os.path.splitext(args['file'].filename)
            if not os.path.exists(destination):
                os.makedirs(destination)
            file = '%s%s' % (destination, filename + file_extension)
            args['file'].save(file)
            return jsonify("Madhawa")
        except Exception as e:
            return jsonify(str(e))

if __name__ == '__main__':
    app.run(debug=True)