def steal_exhibits(m, k, exhibits):
    total_value = 0
    stolen_exhibits = []
    sorted_exhibits = sorted(exhibits, key=lambda exhibit: exhibit[1] / exhibit[0], reverse=True)
    for i in range(m):
        remaining_weight = k
        exhibit_index = 0
        can_steal = False

        while remaining_weight > 0 and exhibit_index < len(sorted_exhibits):
            exhibit_weight = sorted_exhibits[exhibit_index][0]

            if exhibit_weight <= remaining_weight:
                remaining_weight -= exhibit_weight
                total_value += sorted_exhibits[exhibit_index][1]
                stolen_exhibits.append(sorted_exhibits[exhibit_index])
                can_steal = True
            exhibit_index += 1

        if can_steal:
            continue

        exhibit_index = 0
        for j in range(len(sorted_exhibits)):
            exhibit_weight = sorted_exhibits[j][0]
            if exhibit_weight <= remaining_weight:
                exhibit_index = j
            else:
                break
        if exhibit_weight <= remaining_weight:
            remaining_weight -= exhibit_weight
            total_value += sorted_exhibits[exhibit_index][1]
            stolen_exhibits.append(sorted_exhibits[exhibit_index])
    return total_value, stolen_exhibits



c = [(2, 3), (4, 3), (2, 1), (2, 4), (5, 6), (3, 2), (2, 5)]
print("Экспаноты(вес, цена)\n", c)
a = int(input("Сколько заходов: "))
b = int(input("Размер сумки вора в кг: "))
print(steal_exhibits(a, b, c))