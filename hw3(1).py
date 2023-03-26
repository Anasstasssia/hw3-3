N = int(input("Введите общую сдачу: "))
m1 = int(input("Введите номинал 1 монеты: "))
m2 = int(input("Введите номинал 2 монеты: "))
m3 = int(input("Введите номинал 3 монеты: "))
m4 = int(input("Введите номинал 4 монеты: "))
c1 = int(input("Введите количество 1 монеты: "))
c2 = int(input("Введите количество 2 монеты: "))
c3 = int(input("Введите количество 3 монеты: "))
c4 = int(input("Введите количество 4 монеты: "))

k = 0
mm_arr = [[m1, c1], [m2, c2], [m3, c3], [m4, c4]]
mm_arr.sort()
print(mm_arr)
m4_k, m3_k, m2_k, m1_k = 0, 0, 0, 0

if m1*c1 + m2*c2 + m3*c3 + m4*c4 < N:
    print('Недостаточно денег для сдачи')
else:
    while N - mm_arr[3][0] >= 0 and mm_arr[3][1] != 0:
        N -= mm_arr[3][0]
        mm_arr[3][1] = int(mm_arr[3][1]) - 1
        k += 1
        m4_k += 1

    while N - mm_arr[2][0] >= 0 and mm_arr[2][1] != 0:
        N -= mm_arr[2][0]
        mm_arr[2][1] -= 1
        k += 1
        m3_k += 1

    while N - mm_arr[1][0] >= 0 and mm_arr[1][1] != 0:
        N -= mm_arr[1][0]
        mm_arr[1][1] -= 1
        k += 1
        m2_k += 1

    while N - mm_arr[0][0] >= 0 and mm_arr[0][1]:
        N -= mm_arr[0][1]
        mm_arr[0][1] -= 1
        k += 1
        m1_k += 1
    print("всего монет:", k)
    print(m1_k, m2_k, m3_k, m4_k)