import pandas as pd
from sqlalchemy import create_engine
import datetime

connection_string = (
    'mssql+pyodbc://consulta_Lamonica:ZL0jEoyRfr@52.67.211.242\\ROD_LAMONICA,12554/db_visual_lamonica'
    '?driver=ODBC+Driver+18+for+SQL+Server'
)
source_engine = create_engine(connection_string)
query = "SELECT * FROM VW_RCT_RESUMO_OPERACAO_STATUS"
df = pd.read_sql(query, source_engine)

df['DATA_HISTORICO'] = datetime.datetime.now()

destination_connection_string = (
    'mssql+pyodbc://serverbd\\SQLBDSASCAR/db_sascar'
    '?driver=ODBC+Driver+18+for+SQL+Server;trusted_connection=yes'
)
destination_engine = create_engine(destination_connection_string)

df.to_sql('RCT_HISTORICO_LOG', destination_engine, if_exists='append', index=False)
