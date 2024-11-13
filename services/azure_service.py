import requests
from utils.config import Config

class AzureService:
    def __init__(self):
        self.endpoint = Config.ENDPOINT
        self.key = Config.KEY
        self.headers = {"Ocp-Apim-Subscription-Key": self.key}

    def process_document(self, file_path):
        """
        Envia um documento para o Azure Cognitive Services e retorna a resposta.
        """
        try:
            with open(file_path, "rb") as document:
                response = requests.post(
                    f"{self.endpoint}/formrecognizer/v2.1-preview.3/layout/analyze",
                    headers=self.headers,
                    files={"file": document}
                )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Erro ao processar o documento: {e}")
            return None
