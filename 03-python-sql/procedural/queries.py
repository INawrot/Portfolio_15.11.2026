import sqlite3
from procedural.imports import DB_PATH

def run_queries_procedural():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) 
        FROM shoes_dim 
        WHERE dominant_color = 'Cloud White'
    """)
    print(f"Liczba butów w kolorze Cloud White: {cursor.fetchone()[0]}")
    
    cursor.execute("""
        SELECT COUNT(DISTINCT id) 
        FROM shoes_fact \
        WHERE size = '44' AND country_code = 'DE'
    """)
    print(f"Unikalne ID produktów (rozmiar 44, DE): {cursor.fetchone()[0]}")

    cursor.execute("""
        SELECT COUNT(DISTINCT f.id) 
        FROM shoes_fact f
        JOIN country_dim c ON f.country_code = c.country_code
        WHERE f.size = '44' AND c.currency = 'euro'
    """)
    print(f"Unikalne ID w rozmiarze 44 w strefie EURO: {cursor.fetchone()[0]}")
    
    cursor.execute("""
    SELECT COUNT(DISTINCT(d.id)) 
    FROM shoes_fact f
    JOIN shoes_dim d ON f.id = d.id
    JOIN country_dim c ON f.country_code = c.country_code
    WHERE d.dominant_color = 'Cloud White' 
      AND c.currency = 'euro'
      AND CAST(f.size AS INTEGER) >= 49
        
    """)

    wynik = cursor.fetchone()[0]
    print(f"Liczba butów Cloud White w strefie EURO (rozmiar >= 49): {wynik}")
    
    conn.close()