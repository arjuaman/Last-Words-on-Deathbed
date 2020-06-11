import pandas as pd
import sqlite3 as sq
data = "E:\Python\Projects\capstone\pagerank\statements.csv"
sql_data = 'E:\Python\Projects\capstone\pagerank\SA.sqlite' #- Creates DB names SQLite
conn = sq.connect(sql_data)
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS SA''')
data.to_sql('SA', conn, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
pd.read_sql('select * from Statements', conn)
conn.commit()
conn.close()
