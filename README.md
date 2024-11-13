# **Projeto de Análise Automatizada de Documentos com AzureAI**

## **Descrição**

Este projeto utiliza o Azure Cognitive Services e Azure Blob Storage para criar uma solução automatizada de análise de documentos. O principal objetivo é identificar padrões de fraude, validar a autenticidade de documentos e aumentar a segurança em processos empresariais que dependem de dados sensíveis.

O projeto foi desenvolvido com Python e organiza as funções em módulos para facilitar a escalabilidade e a manutenção. Ele inclui serviços para upload de arquivos no Azure Blob Storage e para análise de documentos com o Azure Form Recognizer.

---

## **Funcionalidades**

1. **Upload de Documentos**:
   - Envio de documentos para o Azure Blob Storage.
   - Armazenamento seguro e organizado em containers.

2. **Análise Automatizada**:
   - Utilização do Azure Form Recognizer para processar e extrair informações dos documentos enviados.

3. **Identificação de Padrões de Fraude**:
   - Implementação de algoritmos (ou regras) para verificar inconsistências ou identificar fraudes.

---

## **Estrutura do Projeto**

```plaintext
proj.2/
├── Services/
│   ├── __init__.py
│   ├── storage_service.py       # Lógica de upload para Azure Blob Storage
│   ├── azure_service.py         # Lógica para interação com Azure Form Recognizer
│
├── src/
│   ├── __init__.py
│   ├── document_analysis.py     # Análise de documentos utilizando os serviços do Azure
│   ├── main.py                  # Ponto de entrada do projeto
│
├── utils/
│   ├── __init__.py
│   ├── config.py                # Carrega variáveis de ambiente do arquivo .env
│
├── .env                         # Variáveis sensíveis do projeto
├── requirements.txt             # Dependências do projeto
├── README.md                    # Documentação do projeto

## **Pré-requisitos**

- Python 3.8 ou superior.
- Conta no Azure com os seguintes serviços configurados:
  - Azure Blob Storage
  - Azure Form Recognizer (Cognitive Services)
- Ambiente virtual Python (recomendado).

---

## **Instalação**

1. **Clone o repositório para a sua máquina local**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd proj.2


## **Crie um ambiente virtual e ative-o**

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows


## **Instale as dependências**
pip install -r requirements.txt


## **Configure o arquivo .env com suas credenciais do Azure**
container-name="cartoes"
storage-connect-string="sua_string_de_conexao"
cadeia-de-conexao="sua_cadeia_de_conexao"
Ponto-de-extremidade="seu_endpoint_do_cognitive_services"
CHAVE-1="sua_chave_do_cognitive_services"

## **Como Executar**

Execute o projeto diretamente da raiz do diretório utilizando o comando:

python -m src.main

Acompanhe os resultados no terminal:

Upload do arquivo no Azure Blob Storage.
Análise do documento no Azure Form Recognizer.

# **Problemas Conhecidos**

## **Erro de Importação em `main.py`**

Durante o desenvolvimento, foi identificado o seguinte erro:

```plaintext
ModuleNotFoundError: No module named 'Services'

## **Causa**

O erro ocorre porque o Python não consegue localizar o pacote `Services`. Mesmo após ajustes na configuração de caminhos, como o uso de `sys.path` e execução com o comando `python -m src.main`, o problema persiste.

---

## **Observação**

Apesar de ter seguido boas práticas de estruturação e configurado o ambiente adequadamente, **não foi possível solucionar este problema com os recursos técnicos disponíveis até o momento.**

Se você identificar uma solução ou quiser contribuir com melhorias, por favor, abra uma issue ou envie um pull request no repositório.

---

## **Contribuições**

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Esse conteúdo está formatado corretamente para ser salvo como `README.md`. Caso precise de ajustes adicionais, é só avisar! 😊
