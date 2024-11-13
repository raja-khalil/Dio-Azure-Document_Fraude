from azure.storage.blob import BlobServiceClient
from utils.config import Config

class StorageService:
    def __init__(self):
        self.connection_string = Config.AZURE_STORAGE_CONNECTION_STRING
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def upload_file(self, container_name, file_path):
        """
        Faz upload de um arquivo para o Azure Blob Storage.
        """
        try:
            container_client = self.blob_service_client.get_container_client(container_name)
            blob_name = file_path.split("/")[-1]
            with open(file_path, "rb") as data:
                container_client.upload_blob(blob_name, data)
            return f"Arquivo {blob_name} enviado com sucesso!"
        except Exception as e:
            print(f"Erro ao enviar arquivo: {e}")
            return None
