from flask import Flask
from flask import render_template
from flask import request
from google.cloud import automl
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=(r"C:\Users\aleks\Downloads\key2.json")

project_id = "project-bigscale"
model_id = "TCN2353841089812627456"
prediction_client = automl.PredictionServiceClient()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    project_id = "project-bigscale"
    model_id = "TCN2353841089812627456"

    if request.method == 'POST':
        content = request.form['message']
        prediction_client = automl.PredictionServiceClient()
        model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)
        text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
        payload = automl.ExamplePayload(text_snippet=text_snippet)

        response = prediction_client.predict(name=model_full_id, payload=payload)

        def payload_info(predict):
            Result = predict.payload[0].display_name
            return Result

        my_prediction = payload_info(response)

    return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
    app.run()
