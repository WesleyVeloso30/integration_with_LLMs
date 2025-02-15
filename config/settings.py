from dotenv import load_dotenv
import os

load_dotenv('./config/.env')  # Carrega as variáveis de ambiente
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
