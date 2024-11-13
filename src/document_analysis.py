import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Services.azure_service import AzureService

class DocumentAnalysis:
    def __init__(self):
        self.azure_service = AzureService()

    def analyze_document(self, file_path):
        """
        Analisa um documento utilizando o Azure Cognitive Services.
        """
        response = self.azure_service.process_document(file_path)
        return response
