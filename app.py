# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json

from openai import OpenAI


client = OpenAI(api_key='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')
messages = [ {"role": "system", "content":
              "You are a intelligent assistant."} ]

app = Flask(__name__)


@app.route('/endpoint/<param_value>')
def hello_world(param_value):  # put application's code here
    data = "hello world"
    '''param_value = request.args.get('param_name')'''
    message = str(param_value) + ".Ilan aciklamasi yaaz. Maksimum 300 karakter kullan. utf-8 ve json formatinda yolla. JSON disinda baska birsey dondurme!"
    print(message)
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    '''print(jsonify({'data': reply}))'''
    print(type(reply))
    return jsonify({'data': reply})

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=4000, debug=True)
'''while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})'''







