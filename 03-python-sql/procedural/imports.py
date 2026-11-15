import sqlite3
import pandas as pd
import os

DB_PATH = "adidas_database.db"

def import_data_procedural():
    conn = sqlite3.connect(DB_PATH)
    
    country_path = os.path.join("data", "country_dim.csv")
    shoes_dim_path = os.path.join("data", "shoes_dim.csv")
    shoes_fact_path = os.path.join("data", "shoes_fact.csv")
    
    print("Importowanie danych...")
    
    df_country = pd.read_csv(country_path).drop_duplicates(subset=['country_code'])
    df_country.to_sql('country_dim', conn, if_exists='replace', index=False)
    
    df_shoes = pd.read_csv(shoes_dim_path).drop_duplicates(subset=['id'])
    df_shoes.to_sql('shoes_dim', conn, if_exists='replace', index=False)
    
    df_fact = pd.read_csv(shoes_fact_path)
    df_fact.to_sql('shoes_fact', conn, if_exists='replace', index=False)
    
    conn.close()