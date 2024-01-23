
from flask import Flask,jsonify, request

API_KEY = "AIzaSyBcTjWj4lvncBirGPkSo4UhszdQlmOoMDw"
app = Flask(__name__)
"""
At the command line, only need to run once to install the package via pip:

"""

import google.generativeai as genai

genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["you are a medical chatbot"]
  },
  {
    "role": "model",
    "parts": ["ok"]
  },
  {
    "role": "user",
    "parts": ["i have   Sore throat \"Cough\",\n             \"Congestion\",\n             \"Slight body aches or a mild headache\",\n             \"Sneezing\",\n             \"Low-grade fever\",\n             \"Generally feeling unwell (malaise)"]
  },
  {
    "role": "model",
    "parts": ["seems like you have a common cold, Most people recover on their own within two weeks. so take rest and be hydrated"]
  },
  {
    "role": "user",
    "parts": ["i have              \"Lost interest\",\n             \"Increased fatigue\",\n             \"sleep problem\",\n             \"Anxiety\",\n             \"change in weight\",\n             \"Looking at death\"]\nwhat is my problem"]
  },
  {
    "role": "model",
    "parts": ["Looks like you suffering from depression, you must visit a medical professional as soon as possible."]
  },
  {
    "role": "user",
    "parts": ["i have coughing, thightness in chest, and fatigue what am i having"]
  },
  {
    "role": "model",
    "parts": ["It's likely that you have pneumonia. This is a lung infection that can cause coughing, tightness in the chest, and fatigue. It can also cause fever, chills, and shortness of breath. You should see a doctor as soon as possible so that you can get treatment."]
  },
])


@app.route('/', methods=['GET'])
def main():
    prompt = request.args.get('prompt')
    convo.send_message(prompt) 
    print(convo.last.text)
    return jsonify(response = convo.last.text)
@app.route('/test')
def check():
    return 'hello world'

