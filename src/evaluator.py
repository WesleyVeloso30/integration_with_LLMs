# Código para análise e ranking das respostas
from llm_clients import get_gemma_response, get_llama3_response, get_qwen_response

def evaluate_responses(question, responses):
    evaluation_prompt = 'Compare as seguintes respostas para a pergunta e classifique-as com base em clareza, coerência e precisão.'
    evaluation_prompt += f'\n\nPergunta feita:\n{question}\n\nRespostas:\n'
    for model, response in responses.items():
        evaluation_prompt += f'\n\n{model}: {response}'

    ranking = {
        'Qwen': get_qwen_response(evaluation_prompt),
        'Gemma': get_gemma_response(evaluation_prompt),
        'Llama': get_llama3_response(evaluation_prompt)
    }
    
    return ranking