import openai
import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import GROQ_API_KEY

# Configuração da API GroqCloud
client = openai.OpenAI(api_key=GROQ_API_KEY, base_url='https://api.groq.com/openai/v1')

# Função genérica para chamar modelos no GroqCloud
def get_llm_response(question, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': question}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f'Erro ao obter resposta do {model}: {str(e)}'

# Funções específicas para cada modelo
def get_llama3_response(question):
    return get_llm_response(question, 'llama3-8b-8192')

def get_qwen_response(question):
    return get_llm_response(question, 'qwen-2.5-32b')

def get_gemma_response(question):
    return get_llm_response(question, 'gemma2-9b-it')
