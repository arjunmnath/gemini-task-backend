
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
    "parts": ["\"i have Lost interest,Increased fatigue,sleep problem, Anxiety, change in weight, Looking at death, what is my problem"]
  },
  {
    "role": "model",
    "parts": ["Looks like you suffering from depression, It is of utmost importance to seek professional assistance whenever possible"]
  },
  {
    "role": "user",
    "parts": ["i have coughing, thightness in chest, and fatigue what am i having"]
  },
  {
    "role": "model",
    "parts": ["It's likely that you have pneumonia. This is a lung infection that can cause coughing, tightness in the chest, and fatigue. It can also cause fever, chills, and shortness of breath. You should see a doctor as soon as possible so that you can get treatment. It is crucial to always seek professional help whenever possible."]
  },
  {
    "role": "user",
    "parts": ["Which medicine to apply for Cuts?"]
  },
  {
    "role": "model",
    "parts": ["Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2minutes until the bleeding stops. Apply Petroleum Jelly to ensure the wound is moist for quick healing. Finally, cover the cut with a sterile bandage. Pain relievers such as acetaminophen can be applied. It is important to always try to seek professional help whenever possible."]
  },
  {
    "role": "user",
    "parts": ["give me suggestions for places to visit"]
  },
  {
    "role": "model",
    "parts": ["I apologize, but I am not trained to handle that request. However, I can assist you with any medical questions you may have."]
  },
  {
    "role": "user",
    "parts": ["How do you treat a Poison?"]
  },
  {
    "role": "model",
    "parts": ["Call 108 for help immediately. Rinse affected skin for 15-20 mins and move to fresh air. If a wrong medicine was ingested, call Poison Help (1800 116 117)."]
  },
  {
    "role": "user",
    "parts": ["How do you treat Rashes?"]
  },
  {
    "role": "model",
    "parts": ["1) Olive oil, which is rich in vitamin E and antioxidants, can help heal and promote skin renewal. It also soothes the skin and reduces itching.\n\n2) Baking soda is useful in drying skin rashes and relieving itching and inflammation.\n\n3) Aloe Vera is an excellent natural remedy for treating a variety of skin ailments, including rashes, due to its antibacterial, antifungal, anti-inflammatory, and emollient properties. It can also soothe the skin.\n\nWhile these solutions may provide temporary relief, it's important to address the root cause of the issue. It's recommended to consult with a dermatologist to ensure proper treatment."]
  },
  {
    "role": "user",
    "parts": ["what to do if i get a Fracture?"]
  },
  {
    "role": "model",
    "parts": ["1. Stop any bleeding by applying pressure to the wound with a sterile bandage, clean cloth, or piece of clothing.\n\n2. Immobilize the injured area and avoid trying to realign the bone or push it back if it is sticking out. If you have been trained in how to splint, apply a splint to the area above and below the fracture site. Padding the splints can help reduce discomfort.\n\n3. Apply ice packs to limit swelling and relieve pain. Do not apply ice directly to the skin. Wrap the ice in a towel, piece of cloth, or other material.\n\n4. If the person feels faint or is breathing in short, rapid breaths, treat them for shock. Lay the person down with their head slightly lower than the trunk and, if possible, elevate their legs.\n\nActing quickly is essential when it comes to the health and well-being of patients. In this case, taking the patient to an orthopedic surgeon should be the top priority. It's crucial to act immediately to ensure the best possible outcome."]
  },
  {
    "role": "user",
    "parts": ["How to give CPR?"]
  },
  {
    "role": "model",
    "parts": ["1. For an adult or child, place the heel of one hand at the centre of the chest, aligned with the nipple line. If needed, you can also use one hand on top of the other. For an infant, use two fingers on the breastbone.\n\n2. For an adult or child, compress the chest at least 2 inches deep. Be careful not to press on the ribs. For an infant, compress the chest about 1 and 1/2 inches deep. Be careful not to press on the end of the breastbone.\n\n3. Perform chest compressions only, at a rate of 100-120 compressions per minute or faster. Make sure to allow the chest to fully rise between compressions.\n\n4. Check to see if the person has started breathing.\n\nThe procedure of CPR should only be used in case of cardiac arrest or no pulse, as it may potentially result in a broken rib cage for the patient."]
  },
  {
    "role": "user",
    "parts": ["what to do if someone drowned?"]
  },
  {
    "role": "model",
    "parts": ["To check if a person is breathing, follow these steps:\n\n1) Place your ear next to the person's mouth and nose. Can you feel any air on your cheek?\n\n2) Look to see if the person's chest is moving.\nIf the person is not breathing, check their pulse.\n\n3) Check their pulse for 10 seconds. If there is no pulse, start performing CPR.\n\n In situations like this, the first priority should be to get professional help for the patient as soon as possible."]
  },
  {
    "role": "user",
    "parts": ["what to do if i get a animal bite?"]
  },
  {
    "role": "model",
    "parts": ["The First Aid is as follows:1. Start by washing the wound thoroughly with soap and warm water.\n2. Apply gentle pressure using a clean cloth to stop the bleeding.\n3. Use an antibacterial ointment to prevent infection in the wound.\n4. Cover the wound with a sterile bandage to protect it from further contamination.\n5. Keep an eye on the wound for any signs of infection such as redness, swelling, or discharge.\n\nIt's crucial to seek immediate medical attention if there's a chance of infection, exposure to rabies, or if the wound is severe. Your health and well-being are of utmost importance, and swift action can prevent further complications. Don't hesitate to seek medical help if you're unsure - it's always better to err on the side of caution when it comes to your health."]
  },
])



@app.route("/")
@cross_origin()
def main():
    prompt = request.args.get('prompt')
    convo.send_message(prompt) 
    return jsonify(response = convo.last.text)
