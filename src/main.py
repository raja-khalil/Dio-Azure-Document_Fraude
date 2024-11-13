import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Services.storage_service import StorageService
from src.document_analysis import DocumentAnalysis

def main():
    # Instanciar os serviços necessários
    storage_service = StorageService()
    document_analysis = DocumentAnalysis()

    # Caminho do arquivo a ser processado
    file_path = "documentos/exemplo.pdf"

    # 1. Upload do arquivo para o Azure Blob Storage
    print("Fazendo upload do arquivo...")
    upload_result = storage_service.upload_file("cartoes", file_path)
    print(upload_result)

    # 2. Análise do documento
    print("Analisando o documento...")
    document_data = document_analysis.analyze_document(file_path)
    print(f"Dados do documento: {document_data}")

if __name__ == "__main__":
    main()
