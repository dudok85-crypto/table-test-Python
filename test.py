from prettytable import PrettyTable

receipt = PrettyTable()
receipt.field_names = ["№", 'Продукт',"цена", 'Количество', 'стоимость']

print(receipt)