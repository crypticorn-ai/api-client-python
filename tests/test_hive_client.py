from api_client.python.client import HiveClient
import random
import pandas as pd

### Local Testing
# Run app.py locally
# comment these following lines
# response = api_client.verify(auth_token)
# user_id = response["sub"]

if __name__ == "__main__":
    client = HiveClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoicTdQMVh3WG9MdU5wbEJJNlFMVWMiLCJpYXQiOjE3Mjg4MTk1MDAsImV4cCI6MTcyODgyMzEwMCwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.zbV9fQUmIQ1yYwaaAHazc1eYm6kK9-YMorOcWyWiuYg")
    
    print("Testing create_account:")
    #print(client.create_account("test_user12"))

    #
    # for i in range(10):
    # #
    print("\nTesting create_model:")
    #print(client.create_model(1, "Tatooine"))
    #     #
    #     print("\nTesting evaluate_model:")
    #     data = pd.DataFrame(columns=["feature1"], data=[random.gauss(1,0.02) for _ in range(4000)])
    #     print(client.evaluate_model(i, data))
    print("\nTesting evaluate_model:")
    #data = pd.DataFrame(columns=["feature1"], data=[random.gauss(1,0.02) for _ in range(4986)])
    #print(client.evaluate_model(1, data))

    print("\nTesting get_specific_model:")
    #print(client.get_model(2))

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
    print(client.download_data(model_id=1, feature_size="small", version=1))

    print("\nTesting get_account_info:")
    #print(client.get_account_info(username="Mister Y"))
