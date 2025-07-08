import pandas as pd
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import io

load_dotenv()

db_params = {
    'dbname': os.getenv('KLINES_DB_NAME'),
    'user': os.getenv('KLINES_DB_USER'),
    'password': os.getenv('KLINES_DB_PASSWORD'),
    'host': os.getenv('KLINES_DB_HOST', 'hz.crypticorn.dev'),
    'port': os.getenv('KLINES_DB_PORT')
}

def fetch_data_from_postgres(query, params=None):    
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

def fetch_data_with_copy(query, csv_path=None):
    output = io.StringIO()
    try:
        conn = psycopg2.connect(**db_params)
        with conn.cursor() as cur:
            copy_sql = f"COPY ({query}) TO STDOUT WITH CSV HEADER"
            cur.copy_expert(copy_sql, output)
        output.seek(0)
        if csv_path:
            with open(csv_path, 'w', encoding='utf-8') as f:
                f.write(output.getvalue())
        df = pd.read_csv(output)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

def fetch_ohlcv_data(pair, timeframe, market_type, limit=280000, csv_path=None):
    table_name = f"ohlcv_{market_type}_{timeframe}"
    query = f"SELECT timestamp, pair, open, high, low, close, volume FROM {table_name} WHERE pair = '{pair}' ORDER BY timestamp DESC LIMIT {limit}"
    df = fetch_data_with_copy(query, csv_path=csv_path)
    if df is not None:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].astype(int) // 10 ** 9
    return df

def fetch_funding_rate_data(pair, limit=100, csv_path=None):
    query = f"SELECT EXTRACT(EPOCH FROM funding_time)::BIGINT AS timestamp, symbol AS pair, funding_rate FROM funding_rate WHERE symbol = '{pair}' ORDER BY funding_time DESC LIMIT {limit}"
    return fetch_data_with_copy(query, csv_path=csv_path)

if __name__ == "__main__":
    spot_df = fetch_ohlcv_data('BTCUSDT', '15m', 'spot', csv_path='btc_15m_spot_klines.csv')
    if spot_df is not None:
        print(spot_df.head())
    
    futures_df = fetch_ohlcv_data('BTCUSDT', '15m', 'futures', csv_path='btc_15m_futures_klines.csv')
    if futures_df is not None:
        print(futures_df.head())
    
    funding_rate_df = fetch_funding_rate_data('BTCUSDT', csv_path='btc_funding_rates.csv')
    if funding_rate_df is not None:
        print(funding_rate_df.head())