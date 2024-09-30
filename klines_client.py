import pandas as pd
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data_from_postgres(query, params=None):
    # Construct the connection parameters
    db_params = {
        'dbname': os.getenv('KLINES_DB_NAME'),
        'user': os.getenv('KLINES_DB_USER'),
        'password': os.getenv('KLINES_DB_PASSWORD'),
        'host': os.getenv('KLINES_DB_HOST', 'eu.crypticorn.dev'),
        'port': os.getenv('KLINES_DB_PORT')
    }
    
    try:
        # Establish a connection
        conn = psycopg2.connect(**db_params)
        
        # Create a cursor
        with conn.cursor() as cur:
            # Execute the query
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            
            # Fetch all results
            results = cur.fetchall()
            
            # Get column names
            column_names = [desc[0] for desc in cur.description]
            
        # Create a pandas DataFrame
        df = pd.DataFrame(results, columns=column_names)
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        if conn:
            conn.close()

def fetch_ohlcv_data(pair, timeframe, market_type, limit=100):
    query = sql.SQL("SELECT * FROM {} WHERE pair = %s ORDER BY timestamp DESC LIMIT %s").format(
        sql.Identifier(f"ohlcv_{market_type}_{timeframe}")
    )
    params = (pair, limit)
    df = fetch_data_from_postgres(query, params)
    if df is not None:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].astype(int) // 10 ** 9
    return df

def fetch_funding_rate_data(pair, limit=100):
    query = sql.SQL('SELECT * FROM funding_rate WHERE "Symbol" = %s ORDER BY "FundingTime" DESC LIMIT %s')
    params = (pair, limit)
    return fetch_data_from_postgres(query, params)

if __name__ == "__main__":
    spot_df = fetch_ohlcv_data('BTCUSDT', '1m', 'spot')
    if spot_df is not None:
        print(spot_df.head())
    
    futures_df = fetch_ohlcv_data('BTCUSDT', '1m', 'futures')
    if futures_df is not None:
        print(futures_df.head())

    funding_rate_df = fetch_funding_rate_data('BTCUSDT')
    if funding_rate_df is not None:
        print(funding_rate_df.head())