# Configuração do Ambiente (Setup)

Siga os passos abaixo para configurar o ambiente de desenvolvimento do ColorTradutor.

## Pré-requisitos

- Python 3.11 ou superior.
- [Poetry](https://python-poetry.org/docs/#installation) instalado.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/joao-carlos-eng/ColorTradutor.git
   cd ColorTradutor
   ```

2. Instale as dependências com Poetry:
   ```bash
   poetry install
   ```

3. (Opcional) Baixe os recursos necessários do NLTK caso utilize o tokenizador:
   ```python
   import nltk
   nltk.download('punkt')
   ```

## Como Rodar

Para iniciar a interface gráfica:
```bash
poetry run python app.py
```

Para testar o tradutor avançado via terminal:
```bash
poetry run python tradutor.py
```
