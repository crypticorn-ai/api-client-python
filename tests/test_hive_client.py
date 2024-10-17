from python.client import HiveClient
import random
import pandas as pd

### Local Testing
# Run app.py locally and use the token from the console to test the client

if __name__ == "__main__":
    client = HiveClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiamhXVXVDS0pNVjQ0ZmNiWEx4VmMiLCJpYXQiOjE3Mjg5OTc4ODksImV4cCI6MTcyOTAwMTQ4OSwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.oeJqCJ63kikLEgv83wrnicnBapz3dFujAmI5D3oGeTQ")
    
    print("Testing create_account:")
    #print(client.create_account())
    
    print("\nTesting create_model:")
    #print(client.create_model(1, "Alderaan"))
    #     #
    print("\nTesting evaluate_model:")
    #data = pd.DataFrame(columns=["feature1"], data=[random.gauss(1,0.02) for _ in range(4986)])
    #print(client.evaluate_model(1, data))

    print("\nTesting get_specific_model:")
    #print(client.get_model(id=1))
    
    print("\nTesting get_all_models:")
    #print(client.get_model())
    
    print("\nTesting delete_model:")
    #print(client.delete_model(id=1))

    print("\nTesting get_leaderboard:")
    #print(client.get_leaderboard())

    print("\nTesting generate_api_key:")
    #print(client.generate_api_key())

    print("\nTesting delete_api_key:")
    #print(client.delete_api_key())

    print("\nTesting data_info:")
    #print(client.data_info())

    print("\nTesting update_username")
    #print(client.update_username("Mister Y"))

    print("\nTesting download_data:")
    #print(client.download_data(model_id=1, feature_size="small", version=1))

    print("\nTesting get_account_info by id:")
    #print(client.get_account_info(id="nbZ05EjKfjXjWt0S07o9"))
    
    print("\nTesting get_account_info by username:")
    #print(client.get_account_info(id="mateh"))
    
    print("\nTesting get_account_info (current user):")
    #print(client.get_account_info())
