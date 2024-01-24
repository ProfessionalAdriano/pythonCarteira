**************************************************************************************************************************************************************************************************************************************************************************
*****************************************************************************************************************CONTEXTO DO PROJETO**************************************************************************************************************************************
**************************************************************************************************************************************************************************************************************************************************************************
1 - Instalar bibliotecas: Pandas, Numpy, pyarrow

2 - Verificar se as dependências do projeto já foram instaladas, se sim, imprimir mensagem informando a versão, e em caso negativo efetuar a instalação.

3 - Criar "pipeline de dados" que contemple os seguintes cenários: 
  **Validação dos itens acima(1 e 2).**
  **criar uma estrutura de dados(dataframe) para simular uma carteira de ativos**
  **Criar função que vai inserir uma nova coluna(MELHOR_COTACAO_DIA) com dados calculados das colunas(COTACAO, PRECO_TETO)**        
  **Criar um processo para persisitir os dados em um diretório qualquer na máquina host**

4 - Rodar o projeto utilizando container
5 - Utilizar o docker compose para gerenciar o container




**************************************************************************************************************************************************************************************************************************************************************************
*******************************************************************************************COMANDOS UTILIZADOS PARA HABILITAR O AMBIENTE**********************************************************************************************************************************
**************************************************************************************************************************************************************************************************************************************************************************
docker build -t adr-python .
docker run -e TZ=America/Sao_Paulo -p 5000:5000 --name carteira -v /home/adriano/eng/app/data/parquet:/home/adriano/eng/app/data/parquet --rm adr-python
docker-compose up
docker-compose down




