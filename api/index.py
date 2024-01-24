
from flask import Flask,jsonify, request
from flask_cors import CORS, cross_origin

API_KEY = "AIzaSyBcTjWj4lvncBirGPkSo4UhszdQlmOoMDw"
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
        "max_output_tokens": 512,
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
    "parts": ["i have Sore throat, Cough, Congestion, Slight body aches or a mild headache, Sneezing, Low-grade fever, Generally feeling unwell (malaise)"]
  },
  {
    "role": "model",
    "parts": ["i have Sore throat, Cough, Congestion, Slight body aches or a mild headache, Sneezing, Low-grade fever, Generally feeling unwell (malaise)"]
  },
  {
    "role": "user",
    "parts": ["\"i have Lost interest,Increased fatigue,sleep problem, Anxiety, change in weight, Looking at death, what is my problem"]
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
  {
    "role": "user",
    "parts": ["Which medicine to apply for Cuts?"]
  },
  {
    "role": "model",
    "parts": ["Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2minutes until bleeding stops. Apply Petroleum Jelly to make sure that the wound is moist for quick healing. Finally cover the cut with a sterile bandage. Pain relievers such as acetaminophen can be applied."]
  },
])
@app.route("/")
@cross_origin()
def main():
    prompt = request.args.get('prompt')
    convo.send_message(prompt) 
    return jsonify(response = convo.last.text)
