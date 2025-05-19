# Usa uma imagem base do Python slim
FROM python:3.12.3-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt /app/requirements.txt

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . /app

# Define as variáveis de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta 5000 para acesso externo
EXPOSE 5000

# Comando para iniciar o servidor Flask
CMD ["flask", "run"]
