import pandas as pd

users = pd.read_csv('../raw/olist_customers_dataset.csv')
orders = pd.read_csv('../raw/olist_orders_dataset.csv')
items = pd.read_csv('../raw/olist_order_items_dataset.csv')

max_User = len(users)


for user in users['customer_id']:
    temp =orders.loc[orders['customer_id'] == user]

    print("UserID:")
    print(user)

    print("join Date:")
    print(temp['order_purchase_timestamp'].min())

    total_Worth =0.0
    for order in temp['order_id']:
        item = items.loc[items['order_id']== order]
        for price in item['price']:
            total_Worth+= price
    print("Total worth:")
    print(total_Worth)

    










