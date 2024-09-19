from python.public.crypticorn import Crypticorn

if __name__ == "__main__":
    client = Crypticorn(api_key="test1-KuNnYYz4s3kQagEaOV9MWAvt4EvCIg")
    #print(client.coins)
    # # Testing the methods with example prints
    #print("Testing create_model:")
    #print(client.create_model(4, "Tatooine"))
    #
    #print("\nTesting evaluate_model:")
    #data = pd.DataFrame([{"feature1": 10, "feature2": 20}])
    #print(client.evaluate_model(1, data))

    #print("\nTesting download_data with coin_id:")
    #client.download_data(coin_id=2, feature_size="all", version=1.2)
    #print("\nTesting download_data with model_id:")
    #client.download_data(model_id=17, version=1.2)


    #print("\nTesting help:")
    #print(client.help())

    # print("\nTesting data info")
    # data = client.data_info()
    # print(type(list(data.keys())[-1]))

    # print("\nCoins:")
    # print(client.coins)
    # print("\nTargets:")
    # print(client.targets)
    # print(client.create_model(2, "Tatooine"))