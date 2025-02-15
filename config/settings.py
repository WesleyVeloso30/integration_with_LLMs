from dotenv import load_dotenv
import os

load_dotenv('../config/.env')  # Carrega as variáveis de ambiente

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
