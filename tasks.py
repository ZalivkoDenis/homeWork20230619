import random


def task_11_120():
    """1
    11.120. В массиве хранится информация о росте 35 человек. Определить, сколько человек имеют самый большой рост.
    """
    heights = []

    # Подготовка данных
    for _ in range(0, 35):
        heights.append(random.randint(160, random.randint(170, 180)))
    print(f'Список:\n{heights}\nКоличество элементов: {len(heights)}')

    count = 0
    maxHeight = max(heights)
    print(f'Самый большой рост: {maxHeight}\nКоличество человек с таким ростом: {heights.count(maxHeight)}')
    return None


def task_11_132():
    """2
    11.132. Дан массив. Определить:
        а) максимальный элемент массива и элемент, являющийся максимальным без учета этого элемента;
        б) минимальный элемент массива и элемент, являющийся минимальным без учета этого элемента;
        в) номера максимального элемента массива и элемента, являющегося максимальным без учета этого элемента;
        г) номера минимального элемента массива и элемента, являющегося минимальным без учета этого элемента.
    """
    someList = []

    # Подготовка данных
    countItems = random.randint(20, 50)
    for _ in range(0, countItems):
        someList.append(random.randint(0, 100))
    print(f'Список:\n\t{someList}\nКоличество элементов: {len(someList)}')

    sortList = list(someList)
    sortList.sort()

    # Подготовка данных для анализа
    # Удаление повторяющихся элементов
    index = 1
    while index < len(sortList):
        if sortList[index] == sortList[index - 1]:
            del sortList[index]
        index += 1
    print(f'\nОтсортированный список без повторений:\n\t{sortList}\n')

    # Решение
    print('а)в) максимальный элемент массива и элемент, являющийся максимальным без учета этого элемента и их номера:')
    print(f'\tsomeList[{someList.index(sortList[-1])}] = {sortList[-1]}, '
          f'someList[{someList.index(sortList[-2])}] = {sortList[-2]}')
    print('б)г) минимальный элемент массива и элемент, являющийся минимальным без учета этого элемента и их номера:')
    print(f'\tsomeList[{someList.index(sortList[0])}] = {sortList[0]}, '
          f'someList[{someList.index(sortList[1])}] = {sortList[1]}')

    return None


def task_11_145():
    """3
    11.145. Дан массив из четного числа элементов. Поменять местами:
        а) его половины;
        б) первый элемент со вторым, третий — с четвертым и т. д.;
        в) его половины следующим способом: первый элемент поменять с последним, второй — с предпоследним и т. д.
    """

    someList = []

    # Подготовка данных
    countItems = random.randint(10, 25) * 2
    for _ in range(0, countItems):
        someList.append(random.randint(0, 100))
    print(f'Список:\n\t{someList}\nКоличество элементов: {len(someList)}')

    halfIndex = countItems // 2
    listA = list(someList)
    listB = list(someList)
    listC = list(someList)

    for index in range(0, halfIndex):
        listA[index], listA[index + halfIndex] = listA[index + halfIndex], listA[index]
        listB[index * 2], listB[index * 2 + 1] = listB[index * 2 + 1], listB[index * 2]
        listC[index], listC[-index - 1] = listC[-index - 1], listC[index]
    print(f'а) Поменять местами его половины:'
          f'\n\t{listA}')
    print(f'а) Поменять местами первый элемент со вторым, третий — с четвертым и т. д.:'
          f'\n\t{listB}')
    print(f'а) Поменять местами его половины следующим способом: первый элемент поменять с последним, '
          f'второй — с предпоследним и т. д.:'
          f'\n\t{listC}')

    return None


def task_11_173():
    """4
    11.173. Переставить последний элемент массива на место первого. При этом первый, второй, ..., предпоследний элементы
    сдвинуть вправо на 1 позицию.
    """
    someList = []

    # Подготовка данных
    countItems = random.randint(20, 50)
    for _ in range(0, countItems):
        someList.append(random.randint(0, 100))
    print(f'Список:\n\t{someList}\nКоличество элементов: {len(someList)}')

    someList.insert(0, someList.pop())

    print(
        f'Переставить последний элемент массива на место первого. При этом первый, второй, ..., предпоследний элементы'
        f' сдвинуть вправо на 1 позицию:\n\t{someList}')

    return None
