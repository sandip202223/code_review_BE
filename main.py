from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Set your OpenAI API key
openai.api_key = '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'

@app.route('/generate_response', methods=['POST'])
def generate_response():
    data = request.get_json()
    messages = data['messages']
    app.config['CORS_HEADERS'] = 'Content-Type'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/generate_chat', methods=['POST'])
def generate_chat():
    try:
        data = request.get_json()
        messages = data['messages']

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return jsonify({"response": response.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
