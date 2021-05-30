from flask import Flask
from flask import render_template
from flask import request
from google.cloud import automl
from google.api_core import exceptions
import os
import spacy
from spacy import displacy
from deep_translator import GoogleTranslator
nlp = spacy.load('fr_core_news_sm')
#from flaskext.markdown import Markdown

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key2.json"

project_id = "project-bigscale"
model_id = "TCN2353841089812627456"
prediction_client = automl.PredictionServiceClient()

app = Flask(__name__)
#Markdown(app)

class Error(Exception):
    pass

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])

def predict():
    project_id = "project-bigscale"
    model_id = "TCN2353841089812627456A"

    docx = nlp(content)
    html = displacy.render(docx, style='dep', options={'bg':'fbb54b', 'offset_x':150})
    p_html = html

    if content:
        translate = GoogleTranslator(source='fr', target='en').translate(content)
    else:
        translate = ''

    if request.method == 'POST':
        content = request.form['message']
        prediction_client = automl.PredictionServiceClient()
        model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)
        text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
        payload = automl.ExamplePayload(text_snippet=text_snippet)

        response = prediction_client.predict(name=model_full_id, payload=payload)

        def payload_info(predict):
            result_cat_0 = predict.payload[0].display_name
            result_prob_0 = round(float(predict.payload[0].classification.score) * 100, 2)
            result_cat_1 = predict.payload[1].display_name
            result_prob_1 = round(float(predict.payload[1].classification.score) * 100, 2)
            result_cat_2 = predict.payload[2].display_name
            result_prob_2 = round(float(predict.payload[2].classification.score) * 100, 2)
            result_cat_3 = predict.payload[3].display_name
            result_prob_3 = round(float(predict.payload[3].classification.score) * 100, 2)
            result_cat_4 = predict.payload[4].display_name
            result_prob_4 = round(float(predict.payload[4].classification.score) * 100, 2)
            result_cat_5 = predict.payload[5].display_name
            result_prob_5 = round(float(predict.payload[5].classification.score) * 100, 2)

            return result_cat_0, result_prob_0, result_cat_1, result_prob_1, result_cat_2, result_prob_2, result_cat_3, result_prob_3, result_cat_4, result_prob_4, result_cat_5, result_prob_5

        my_prediction = payload_info(response)

    return render_template('result.html', prediction=my_prediction, my_sentence=content, result_html=p_html, translate=translate)
    #result_html=result_html

#@app.errorhandler(Exception)
@app.errorhandler(exceptions.InvalidArgument)
def input_error(e):
    return render_template('null.html')

@app.errorhandler(Exception)
def general_error(e):
    return render_template('down.html')

if __name__ == '__main__':
    app.run()