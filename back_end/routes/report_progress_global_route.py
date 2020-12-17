from flask import Blueprint, jsonify
from back_end.helpers.sentiment_analysis_global_helper import get_sentiment_progress
from back_end.helpers.google_entities_helper import get_entity_progress
from back_end.helpers.google_translate_helper import get_translate_progress

report_progress_global_endpoint = Blueprint("report_progress_global", __name__)


@report_progress_global_endpoint.route("/report/progress", methods=['GET'])
def get_analyse_report_progress():
    translate_progress = get_translate_progress()
    entity_progress = get_entity_progress()
    sentiment_progress = get_sentiment_progress()

    total_progress = (translate_progress + entity_progress + sentiment_progress) / 3

    if (entity_progress == 0) and (sentiment_progress == 0) and (translate_progress >= 0):
        current_process = 'Translating'
    elif (entity_progress >= 0) and (sentiment_progress == 0) and (translate_progress >= 0):
        current_process = 'Extracting Entities...'
    else:
        current_process = 'Analysing Sentiment...'

    result = {
        'current_process': current_process,
        'progress': round(total_progress)
    }

    return jsonify(result)
