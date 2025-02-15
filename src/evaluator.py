# Código para análise e ranking das respostas
from llm_clients import get_anthropic_response, get_gemini_response, get_openai_response

def evaluate_responses(question, responses):
    evaluation_prompt = 'Compare as seguintes respostas para a pergunta e classifique-as com base em clareza, coerência e precisão.'
    evaluation_prompt += f'\n\nPergunta feita:\n{question}\n\nRespostas:\n'
    for model, response in responses.items():
        evaluation_prompt += f'\n\n{model}: {response}'

    ranking = {
        'ChatGPT': get_openai_response(evaluation_prompt),
        'Gemini': get_gemini_response(evaluation_prompt),
        'Claude': get_anthropic_response(evaluation_prompt)
    }
    
    return ranking