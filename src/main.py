import openai
import requests
from config.settings import OPENAI_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY


def get_openai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]

def get_gemini_response(question):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateText"
    headers = {"Content-Type": "application/json"}
    payload = {"prompt": {"text": question}, "key": GEMINI_API_KEY}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["candidates"][0]["output"]

def get_anthropic_response(question):
    url = "https://api.anthropic.com/v1/complete"
    headers = {"x-api-key": ANTHROPIC_API_KEY, "Content-Type": "application/json"}
    payload = {"model": "claude-2", "prompt": question, "max_tokens": 500}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["completion"]


if __name__ == "__main__":
    print("Digite sua pergunta (ou 'sair' para encerrar):")
    
    while True:
        question = input("Pergunta: ")
        
        if question.lower() == "sair":
            print("Encerrando...")
            break
        
        print("\nObtendo respostas...\n")
        
        responses = {
            "ChatGPT": get_openai_response(question),
            "Gemini": get_gemini_response(question),
            "Claude": get_anthropic_response(question)
        }


# Comparação baseada em clareza, coerência e precisão
def evaluate_responses(responses):
    evaluation_prompt = "Compare as seguintes respostas para a pergunta e classifique-as com base em clareza, coerência e precisão."
    evaluation_prompt += f"\n\nPergunta feita:\n{question}\n\nRespostas:\n"
    for model, response in responses.items():
        evaluation_prompt += f"\n\n{model}: {response}"
    
    ranking = get_openai_response(evaluation_prompt)  # Pode usar qualquer LLM para ranquear
    return ranking

ranking_result = evaluate_responses(responses)


print("\n--- Avaliação das respostas ---")
print(ranking_result)
