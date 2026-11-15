import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from object.models import Base, ORM_DB_PATH, CountryDim, ShoesDim, ShoesFact

def import_data_orm():
    engine = create_engine(ORM_DB_PATH)
    Base.metadata.drop_all(engine) 
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("Importowanie danych przez ORM...")
    
    df_country = pd.read_csv(os.path.join("data", "country_dim.csv"))
    df_country = df_country.drop_duplicates(subset=['country_code'])
    for _, row in df_country.iterrows():
        session.add(CountryDim(country_code=row['country_code'], currency=row['currency'], shoe_metric=row.get('shoe_metric')))
        
    df_shoes = pd.read_csv(os.path.join("data", "shoes_dim.csv"))
    df_shoes = df_shoes.drop_duplicates(subset=['id'])
    for _, row in df_shoes.iterrows():
        session.add(ShoesDim(id=str(row['id']), name=row.get('name'), best_for_wear=row.get('best_for_wear'), gender=row.get('gender'), dominant_color=row['dominant_color']))
        
    df_fact = pd.read_csv(os.path.join("data", "shoes_fact.csv"))
    for _, row in df_fact.iterrows():
        session.add(ShoesFact(id=str(row['id']), size=str(row['size']), price=float(row['price']), country_code=row['country_code'], date=row.get('date')))
        
    session.commit()
    session.close()
    print("Import ORM zakończony sukcesem.\n")