import time

start = time.time()
from crypticorn import ApiClient

elapsed = time.time() - start
print(f"Import time: {elapsed:.4f} seconds")
