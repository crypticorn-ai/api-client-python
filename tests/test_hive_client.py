from python.client import HiveClient
import random
import pandas as pd

### Local Testing
# Run app.py locally
# comment these following lines
# response = api_client.verify(auth_token)
# user_id = response["sub"]

if __name__ == "__main__":
    client = HiveClient(token="your_bearer_token_here")

    print("Testing create_account:")
    #print(client.create_account("test_user1"))
    #
    print("\nTesting get_account_info:")
    #response = client.get_account_info()
    #print(response)

    #
    print("\nTesting create_model:")
    #print(client.create_model(1, "Tatooine"))
    #
    print("\nTesting evaluate_model:")
    #data = pd.DataFrame(columns=["feature1"], data=[random.gauss(1,0.02) for _ in range(4000)])
    #print(client.evaluate_model(1, data))

    print("\nTesting help:")
    #print(client.help())

    print("\nTesting get_all_models:")
    #print(client.get_models())

    print("\nTesting get_specific_model:")
    #print(client.get_models(1))

    print("\nTesting generate_api_key:")
    #print(client.generate_api_key())

    print("\nTesting delete_api_key:")
    #print(client.delete_api_key())

    print("\nTesting data_info:")
    #print(client.data_info())

    print("\nTesting update_username")
    #print(client.update_username("Mister Y"))

    print("\nTesting download_data:")
    print(client.download_data(model_id=1, feature_size="small"))
