"""
python to sqlite: https://www.runoob.com/sqlite/sqlite-python.html
"""

import sqlite3
import pandas as pd
pd.set_option("display.max_columns", 20)

def check_table_exist(name:str, the_db_connection):
    """
    docstring
    """
    # if table exists, return True
    # if table does not exist, return False
    pass

def create_table(name:str, the_db_connection):
    """
    docstring
    """


    pass

# Import csv and clean it
df = pd.read_csv('csv_data/masterstudies_data.csv')
print(df.columns.tolist())
df = df.rename(columns={'_id': 'id'})
# df = df.drop(columns=['id'])
print(df.columns.tolist())
# print(df)

conn = sqlite3.connect('db.sqlite3')
print("Opened database successfully")
c = conn.cursor()

# c.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')

# Save dataframe to SQLite table
df.to_sql('study', conn, if_exists='replace', index = False)
print("Table created successfully")
conn.commit()
conn.close()