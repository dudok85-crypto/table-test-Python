from prettytable import PrettyTable
import matplotlib.pyplot as plt

receipt = PrettyTable()
receipt.field_names = ["№", 'Продукт',"цена", 'Количество', 'стоимость']

#списки для заполнения диаграммы
prod = [] 
pay = []

for i in range(3):
    product = input("укажите название продукта:")
    price = int(input("укажите цену:"))
    col = int(input("укажите количество:"))
    receipt.add_row([i+1, product, price, col, price*col])
    prod.append(product)
    pay.append(price*col)


plt.bar(prod, pay, label = "общая цена продукта")
plt.xlabel("название продукта(ов)")
plt.ylabel("цена продукта(ов)")

print(receipt)
plt.show()
