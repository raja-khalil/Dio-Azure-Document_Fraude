class FraudDetection:
    def __init__(self, document_data):
        self.document_data = document_data

    def check_fraud(self):
        # Implementação de lógica de fraude, como análise de texto, dados ou padrões
        # Isso pode ser feito através de aprendizado de máquina ou regras predefinidas
        return "Fraude detectada" if "fraude" in self.document_data else "Nenhuma fraude"
