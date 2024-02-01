# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json
import config
from openai import OpenAI

## ChatGPT confguration
client = OpenAI(api_key=config.api_key) ## You must replace config.api_key with your own API Key
messages = [ {"role": "system", "content":
              "You are a intelligent assistant."} ]

app = Flask(__name__)



@app.route('/endpoint/<param_value>')## for request endpoint
def hello_world(param_value):  # put application's code here
    ## create message based on received parameter
    message = str(param_value) + ".Ilan aciklamasi yaaz. Maksimum 300 karakter kullan. utf-8 ve json formatinda yolla. JSON disinda baska birsey dondurme!"
    ## for debug
    print(message)
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages ## send prompt to ChatGPT
        )
    reply = chat.choices[0].message.content ## ChatGPT's reply is here
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    print(type(reply))
    return jsonify({'data': reply}) ## post to server

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=4000, debug=True) ## This is for start the server on your computer's IP address








