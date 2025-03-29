from crypticorn import ApiClient

client = ApiClient(base_url="https://api.crypticorn.dev", jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiRDVFUVpjQVN1VVV2cnpVc3VXd3UiLCJpYXQiOjE3NDI5MzQ4MjYsImV4cCI6MTc0MjkzODQyNiwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.IdYOFGl8Xbi1n6SEeW4U6EzbbTXVDlZt7Vi-tZeHjaE")

# json response 
response = client.trade.bots.get_bots_without_preload_content()
print(10 * "=" + "This is the raw json response" + 10 * "=")
print(response.json())

# serialized response with pydantic models
response = client.trade.bots.get_bots()
print(10 * "=" + "This is the serialized response with pydantic models" + 10 * "=")
print(response)

# json response with http info
response = client.trade.bots.get_bots_with_http_info()
print(10 * "=" + "This is the json response with http info" + 10 * "=")
print(response)



