import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    ENDPOINT = os.getenv("Ponto-de-extremidade")
    KEY = os.getenv("CHAVE-1")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("storage-connect-string")
