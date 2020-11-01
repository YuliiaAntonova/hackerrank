# candles = [3,2,1,3]
#
# print(len(candles))

# a = [1, 4, 5, 6, 9]
# b = [2, 1, 5, 10, 12]
# result = []
#
# for i in b:
#     if i in a:
#         result.append(i)
# print(len(result))
massiv = [1, 3, 5, 3, 1]

# for i in massiv:
#     if massiv.count(i) == 2:
#         print(i)
def birthdayCakeCandles(candles):
    # chars = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
    # check_string = input('Введите строку: ')
    n = len(candles)
    maxS = 0
    count = 0
    for i in range(n):
        # count = candles.count(i)
    if count > 1:
        print(count)


print(birthdayCakeCandles([3, 2, 1, 3]))
