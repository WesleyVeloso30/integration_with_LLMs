# 🤖 Comparador de Modelos de IA (LLMs) via GroqCloud  

Este projeto envia 5 perguntas para **três Modelos de Linguagem de Grande Escala (LLMs)** diferentes, compara as respostas e avalia sua qualidade. A integração é feita através da **API do GroqCloud**, que fornece acesso a modelos como **Llama 3, Qwen e Gemma**.  

---

## 🚀 **Funcionalidades**
- Consulta simultânea a **3 LLMs diferentes** (Llama 3, Qwen, Gemma).
- **Comparação automática** das respostas dos modelos.
- **Autoavaliação por IA**, onde os próprios modelos classificam as respostas.

---

## 🛠 **Tecnologias Utilizadas**
- **Python 3.10+**  
- **OpenAI SDK** (compatível com GroqCloud)  
- **Dotenv** (para gerenciamento seguro da API Key)  

---

## 📂 **Estrutura do Projeto**
```
INTEGRATION_WITH_LLMS/
│── config/            # Configurações do projeto
|   ├── __init__.py    # Torna 'config' um pacote Python
|   ├── .env           # Armazena variáveis de ambiente (API Keys)
|   ├── settings.py    # Configurações gerais (ex: carregamento de API Keys)
│── src/               # Código-fonte principal
│   │── __init__.py    # Torna 'src' um pacote Python
│   │── evaluator.py   # Código para análise e ranking das respostas
│   │── llm_clients.py # Código para chamadas às APIs dos LLMs
│   │── main.py        # Código principal (ponto de entrada)
│── .gitignore         # Arquivos que não devem ser versionados (ex: venv, .env)
│── README.md          # Documentação do projeto
│── requirements.txt   # Lista de dependências para instalação via pip
```

## 🏗 Como Instalar
1. Clone o repositório

    ```bash
    git clone https://github.com/WesleyVeloso30/integration_with_LLMs.git
    cd integration_with_LLMs
    ```

2. Crie um ambiente virtual e ative:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as chaves da API:

    🔑 **Como Obter e Configurar a API Key do GroqCloud**  

    Para utilizar os LLMs utilizados nesse projeto, você precisa de uma **API Key** do **GroqCloud**. Siga os passos abaixo para obter a sua.  

    #### ✅ **Passo 1: Criar uma Conta no GroqCloud**
    1. Acesse o site do GroqCloud: 👉 [https://console.groq.com/](https://console.groq.com/)  
    2. Clique em **"Sign Up"** (ou **"Login"**, se já tiver uma conta).  
    3. Complete o cadastro com seu e-mail e senha ou use login social (Google/GitHub).  
    4. Confirme seu e-mail, caso solicitado.  

    ---

    #### ✅ **Passo 2: Gerar a API Key**
    1. Após o login, vá até o painel de controle.  
    2. No menu lateral, clique em **API Keys**.  
    3. Clique no botão **"Create API Key"** para gerar uma nova chave.  
    4. **Copie a API Key** gerada e guarde-a em um local seguro (você não poderá vê-la novamente depois).  

    ---

    #### ✅ **Passo 3: Configurar a API Key no Projeto**
    Agora que você tem sua **API Key**, é necessário configurá-la no projeto.  

    1. **Crie um arquivo chamado `.env` dentro da pasta `config/`**  
    2. Adicione a seguinte linha no arquivo:  
    ```ini
    GROQ_API_KEY=SUA_CHAVE_AQUI
    ```

## 🚀 Como Executar

Após a configuração, rode o script principal:

```bash
python src/main.py
```

## 📊 Comparação de Respostas
O projeto avalia as respostas dos modelos com base nos critérios:
- Clareza e coerência
- Precisão da informação
- Criatividade e profundidade
- Consistência gramatical

Além disso, há um modo de autoavaliação, onde os próprios LLMs classificam as respostas!

## 🤝 Contribuição
Se quiser contribuir:

1. Faça um fork do projeto
2. Crie um branch ```(git checkout -b feature-nova)```
3. Envie um PR com as alterações

## 📝 Licença
Este projeto está sob a licença **MIT**. Sinta-se livre para utilizá-lo e modificá-lo! 🚀
