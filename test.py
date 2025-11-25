from prettytable import PrettyTable

receipt = PrettyTable()
receipt.field_names = ["№", 'Продукт',"цена", 'Количество', 'стоимость']

for i in range(3):
    product = input("укажите название продукта:")
    price = int(input("укажите цену:"))
    col = int(input("укажите количество:"))
    receipt.add_row([i+1, product, price, col, price*col])

print(receipt)
