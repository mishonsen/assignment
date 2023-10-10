mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 107.25
}
def price_conversion(product, conversion_rate):
    price_usd = float(product["price"].split()[0])
    price_bdt = price_usd * conversion_rate
    return f"{product['name']} is made in {product['made']}. The price is {price_usd} USD which is almost equal to {price_bdt} BDT."

if mobile_data["status"]:
    for product in mobile_data["data"]:
        print(price_conversion(product, mobile_data["exchnage_rate"]))