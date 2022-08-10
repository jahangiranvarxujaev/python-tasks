"""""Стоимость заказа
Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции \t разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 1 шт. (целое число).
Напишите программу, подсчитывающую общую стоимость заказа."""""
multipliers = []
overall_sum = 0


with open("price-list", encoding="utf-8") as price:
    initial_pricelist = price.read().split("\n")
    final_pricelist = []

    for line in initial_pricelist:
       final_pricelist.append(line.split("\\t"))

    for line in final_pricelist:
        multiplier = int(line[1]) * int(line[2])
        multipliers.append((multiplier))
    for x in multipliers:
        overall_sum += x
    print(overall_sum)
