from llm_clients import get_qwen_response, get_gemma_response, get_llama3_response
from evaluator import evaluate_responses

if __name__ == '__main__':
    questions = [
        'Se dois LLMs fossem colocados para conversar indefinidamente, como essa conversa evoluiria ao longo do tempo?',
        'Qual foi o primeiro país a adotar uma constituição escrita?',
        'Se você fosse transformar todo o conhecimento humano em um único conceito ou princípio fundamental, qual seria?',
        'Qual é a origem da expressão “cair a ficha” e como ela se popularizou?',
        'Quais são as maiores diferenças entre a maneira como você “pensa” e a maneira como os humanos pensam?',
    ]
    
    for i, question in enumerate(questions):
        responses = {
            'Qwen': get_qwen_response(question),
            'Gemma': get_gemma_response(question),
            'Llama3': get_llama3_response(question)
        }
    
        ranking_result = evaluate_responses(question, responses)

        print(f'---- Pergunta {i + 1} ----\n')
        print(question)
        print('\n---- Respostas obtidas de cada LLM ----\n')
        print(f'-- Qwen --:\n{responses["Qwen"]}')
        print(f'\n-- Llama3 --:\n{responses["Llama3"]}')
        print(f'\n-- Gemma --:\n{responses["Gemma"]}')
        print('-' * 80)
        print('\n\n---- Ranking elencado de acordo com a clareza, coerência e precisão das respostas feito pelas próprias LLMs que responderam as perguntas ----\n')
        print('-- Ranking do Qwen --:\n', ranking_result['Qwen'], '\n')
        print('-- Ranking do Llama3 --:\n', ranking_result['Llama3'], '\n')
        print('-- Ranking do Gemma --:\n', ranking_result['Gemma'], '\n\n\n')
