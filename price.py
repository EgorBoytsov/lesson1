def format_price(price):
    price = int(price)
    print(f'Цена: {price} руб.')

price = float(input("Введите число: "))
print(format_price(price))
