"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
av_quantity = 0
for phone in sales:
    quantity_sales = sum(phone['items_sold'])
    print(f'Суммарное количество продаж по {phone["product"]}: {quantity_sales}')
    av_quantity += quantity_sales
print(f'Суммарное количество всех продаж: {av_quantity}')

def count_phone_avg(phone_sold):
    scores_sum = 0
    for score in phone_sold:
        scores_sum += score
    return scores_sum / len(phone_sold)

phone_avg_sum = 0
for one_sales in sales:
    phone_avg = count_phone_avg(one_sales['items_sold'])
    print(f'Среднее количество продаж {one_sales["product"]}: {round(phone_avg)}')
    phone_avg_sum += phone_avg
print(f'Среднее количество продаж всех товаров: {phone_avg_sum}')

if __name__ == "__main__":
    main()
