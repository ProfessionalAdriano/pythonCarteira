
<style>
  .centro {
    text-align: center;
  }
</style>
<div class="centro">

# **REQUISITOS NECESSÁRIO** 

</div>


## 1. Linguagem:
Python
  - Versão: 3.8.10 

Comandos de Instalação:
  - sudo apt-get update
  - sudo apt-get upgrade
  - sudo apt-get install python3
  

## 2. Gerenciador de pacotes do Python
pip 

Comando de Instalação:  
  - sudo apt-get install python3-pip


## 3. Bibliotecas:
Pandas 
  - Versão: 2.0.3 

Comando de Instalação:
  - pip install pandas


Pyarrow
  - Versão:  15.0.0 

Comando de Instalação:  
  - pip install pyarrow



<style>
  .centro {
    text-align: center;
  }
</style>
<div class="centro">

# **CONTEXTO DO PROJETO** 

</div>


## 1 - Criar pipeline de dados que contemple os seguintes requisitos:
 - criar estrutura de dados(dataframe) em Python para simular uma carteira de ativos.
 - Criar função para inserir uma nova coluna(MELHOR_COTACAO_DIA) com dados calculados das colunas(COTACAO, PRECO_TETO).
 - Criar processo para persisitir os dados em formato parquet em um diretório app/data/parquet.



## 2 - Rodar o projeto utilizando container
 
## 3 - Utilizar o docker compose para gerenciar o container 



<style>
  .centro {
    text-align: center;
  }
</style>
<div class="centro">

# **DOCKER** 
## COMANDOS UTILIZADOS PARA HABILITAR O AMBIENTE

</div>

**Criar a imagem** \
 docker build -t adr-python .

**Executar um contêiner Docker com base em uma imagem** \
 docker run -e TZ=America/Sao_Paulo --name carteira -v /home/adriano/ed/app/data/parquet:/home/adriano/ed/app/data/parquet --rm adr-python


<style>
  .centro {
    text-align: center;
  }
</style>
<div class="centro">

# **DOCKER COMPOSE** 
## COMANDOS UTILIZADOS PARA HABILITAR O AMBIENTE

</div>

**Iniciar os serviços definidos em um arquivo docker-compose.yaml** \
docker-compose up

**Parar e remover os serviços definidos em um arquivo docker-compose.yaml** \
docker-compose down