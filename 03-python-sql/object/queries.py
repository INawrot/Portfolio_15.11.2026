from sqlalchemy import create_engine, distinct, func
from sqlalchemy.orm import sessionmaker
from object.models import ORM_DB_PATH, CountryDim, ShoesDim, ShoesFact

def run_queries_orm():
    engine = create_engine(ORM_DB_PATH)
    Session = sessionmaker(bind=engine)
    session = Session()

    cw_count = session.query(ShoesDim).filter(ShoesDim.dominant_color == "Cloud White").count()
    
    de_44_rows_count = session.query(ShoesFact).filter(
        ShoesFact.size == "44", 
        ShoesFact.country_code == 'DE'
    ).count()
    
    de_44_distinct_count = session.query(distinct(ShoesFact.id)).filter(
        ShoesFact.size == "44", 
        ShoesFact.country_code == 'DE'
    ).count()

    euro_44_count = session.query(
        func.count(distinct(ShoesFact.id))
    ).join(
        CountryDim, ShoesFact.country_code == CountryDim.country_code
    ).filter(
        ShoesFact.size == "44", 
        CountryDim.currency == 'euro'
    ).scalar()

    expensive_cw_count = session.query(func.count(ShoesFact.id.distinct()))\
    .join(ShoesDim, ShoesFact.id == ShoesDim.id)\
    .join(CountryDim, ShoesFact.country_code == CountryDim.country_code)\
    .filter(
        ShoesDim.dominant_color == "Cloud White", 
        CountryDim.currency == "euro", 
        ShoesFact.price >= 100
    ).scalar()



    print(f"Liczba butów w kolorze Cloud White: {cw_count}")
    print(f"Unikalne ID produktów (rozmiar 44, DE): {de_44_distinct_count}")
    print(f"Unikalne ID w rozmiarze 44 w strefie EURO: {euro_44_count}")
    print(f"Cloud White w strefie EURO (cena >= 100 EUR): {expensive_cw_count}")
    
    session.close()