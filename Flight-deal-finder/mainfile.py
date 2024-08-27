
sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                         {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                         {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                         {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
                         {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                         {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
                         {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                         {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                         {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}


for price in sheet_data["prices"]:
    if price["iataCode"] == "":
        print("null")
