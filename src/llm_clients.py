# Código para chamadas às APIs dos LLMs     
import openai
import requests
from config.settings import OPENAI_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY

def get_openai_response(question):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{'role': 'user', 'content': question}],
        api_key=OPENAI_API_KEY
    )
    return response['choices'][0]['message']['content']

def get_gemini_response(question):
    url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateText'
    headers = {'Content-Type': 'application/json'}
    payload = {'prompt': {'text': question}, 'key': GEMINI_API_KEY}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()['candidates'][0]['output']

def get_anthropic_response(question):
    url = 'https://api.anthropic.com/v1/complete'
    headers = {'x-api-key': ANTHROPIC_API_KEY, 'Content-Type': 'application/json'}
    payload = {'model': 'claude-2', 'prompt': question, 'max_tokens': 500}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()['completion']