from datetime import datetime as dt
from platform import python_version

print("Python Version: ", python_version())
#print("\n")
###########################################################################################################################################################################################################################################
                                                                                        # INSTALAÇÃO DE BIBLIOTECAS NECESSÁRIAS
###########################################################################################################################################################################################################################################
import importlib
import subprocess
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def check_install_pandas():
    try:
        # Check Pandas
        importlib.import_module('pandas')                         
        #print("Pandas já está instalado!")
        
        def obter_versao_pandas():
            return pd.__version__
        versao_pandas = obter_versao_pandas()
        print(f"Pandas já está instalado! Version: {versao_pandas}")
        
    except ImportError:
        print("Pandas não encontrado. Instalando agora...")
        
        # Instala o pandas usando o pip
        subprocess.run(['pip', 'install', 'pandas'], check=True)
        print("Pandas foi instalado com sucesso.")


def check_install_pyarrow():
    try:
        import pyarrow
        #print("PyArrow está instalado! ")
        
        def obter_versao_pyarrow():
            return pa.__version__
        
        versao_pyarrow = obter_versao_pyarrow()
        print(f"PyArrow está instalado! Version: {versao_pyarrow}")
        
    except ImportError:
        print("PyArrow não está instalado. Por favor, instale utilizando 'pip install pyarrow'.")
 

# Call
check_install_pandas()
check_install_pyarrow()
###########################################################################################################################################################################################################################################
                                                                # CRIAR DATAFRAME 
###########################################################################################################################################################################################################################################
# DADO DE ORIGEM
def create_dataframe():                 
        header = ["CODIGO", "SEGMENTO",               "INICIO_COBERTURA",  "PRECO_ENTRADA",     "PRECO_TETO", "DATA_COTACAO",                          "COTACAO",  "QTDE_APORTE", "ORIGEM APORTE"]
        data = [["PSSA3",   "Seguradora",             "30/06/2022",         18.16,               25.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  27.19,      0,  " ",  ],            
                ["B3SA3",   "Mercado Financeiro",     "30/06/2022",         10.82,               18.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  13.80,      0,  " ",  ],
                ["BBAS3",   "Setor Financeiro",       "30/06/2022",         33.08,               45.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  55.94,      0,  " ",  ],
                ["ALSO3",   "Setor Financeiro",       "30/06/2022",         16.14,               25.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  23.54,      0,  " ",  ],
                ["TAEE11",  "Energia Elétrica",       "30/06/2022",         38.54,               42.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  37.52,      0,  " ",  ],
                ["NEOE3",   "Energia Elétrica",       "30/06/2022",         15.73,               20.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  15.00,      0,  " ",  ],
                ["LEVE3",   "Indústria Automotiva",   "30/06/2022",         23.28,               25.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  21.23,      0,  " ",  ],
                ["TUPY3",   "Metalúrgica",            "30/06/2022",         22.47,               35.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  26.41,      0,  " ",  ],
                ["KEPL3",   "Bens Industriais",       "30/06/2022",         7.22,                12.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  9.97,       0,  " ",  ],
                ["FESA4",   "Mineradora",             "30/06/2022",         49.52,               55.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  43.70,      16, "DY", ],
                ["MELK3",   "Construção Civil",       "14/07/2022",         3.71,                4.50,         dt.now().strftime('%Y-%m-%d %H:%M:%S'),  4.38,       0,  " ",  ],
                ["EVEN3",   "Construção Civil",       "14/07/2022",         4.54,                7.37,         dt.now().strftime('%Y-%m-%d %H:%M:%S'),  7.69,       0,  " ",  ],
                ["SAPR4",   "Saneamento",             "14/07/2022",         3.60,                4.00,         dt.now().strftime('%Y-%m-%d %H:%M:%S'),  5.89,       0,  " ",  ],
                ["AGRO3",   "Agronegócio",            "14/07/2022",         22.51,               30.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  25.13,      0,  " ",  ],
                ["SMTO3",   "Alimentos Processados",  "27/11/2022",         27.72,               35.00,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  26.82,      0,  " ",  ],
                ["PETR4",   "Petróleo",               "10/04/2023",         26.96,               73.03,        dt.now().strftime('%Y-%m-%d %H:%M:%S'),  38.02,      0,  " ",  ],
                ["KLBN4",   "Papel E Celulose",       "26/07/2023",         4.40,                0.00,         dt.now().strftime('%Y-%m-%d %H:%M:%S'),  4.41,       5,  "DY"  ]   
                ]          
        df = pd.DataFrame(columns=[header], data=data)
        return df

###########################################################################################################################################################################################################################################
                                                                                            # ADD NOVAS COLUNA AO DATAFRAME
###########################################################################################################################################################################################################################################
print("\n")
def add_custom_columns(df):
    for index, row in df.iterrows():
        df.at[index, "MELHOR_COTACAO_DIA"] = row["COTACAO"] - row["PRECO_TETO"]

###########################################################################################################################################################################################################################################
                                                                                            # FUNCTION CREATED TO PERSIST DATA
###########################################################################################################################################################################################################################################
def persistir_dataframe_parquet(dataframe, caminho_arquivo):

    try:
        # Convertendo o DataFrame para um objeto Table do pyarrow
        tabela_arrow = pa.Table.from_pandas(dataframe)

        # Escrevendo a tabela no formato Parquet
        pq.write_table(tabela_arrow, caminho_arquivo)

        print(f"DataFrame persistido com sucesso em {caminho_arquivo} em formato Parquet")
    except Exception as e:
        print(f"Erro ao persistir DataFrame em formato Parquet: {e}")


# PATH
delta = dt.now().strftime('%Y-%m-%d-%H-%M-%S')
#path = f'datalake/parquet/carteita-{delta}.parquet'
path = f'/home/adriano/eng/app/data/parquet/carteita-{delta}.parquet'
         
        


###########################################################################################################################################################################################################################################                                             
###########################################################################################################################################################################################################################################
                                                                                            # EXECUTION SESSION
###########################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################
create_dataframe()
add_custom_columns(create_dataframe())
persistir_dataframe_parquet(create_dataframe(), path)

