# Use a imagem oficial do Python como base 
FROM python:3.9 

# Crie e defina o diretório de trabalho
WORKDIR /app

# Copie todos os arquivos para o diretório de trabalho
COPY . .

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt ./

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000 para que a aplicação possa ser acessada externamente
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "pipeline.py"]

